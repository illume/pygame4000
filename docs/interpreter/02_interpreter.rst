.. contents::
   :depth: 3
..

| |image0|

Let's make a shit javascript interpreter! Part two.
===================================================

| As a learning exercise, I've begun writing a
  `JavaScript <http://en.wikipedia.org/wiki/JavaScript>`__
  `ECMAScript <http://en.wikipedia.org/wiki/ECMAScript>`__ interpreter
  in
  `python <http://en.wikipedia.org/wiki/Python_%28programming_language%29>`__.
  It doesn't even really exist yet, and when it does it will run really
  slowly, and not support all js features.

Homework from part One - A simple tokeniser.
--------------------------------------------

| We ended "`Let's make a shit JavaScript interpreter! Part
  One. <http://renesd.blogspot.com/2010/06/lets-make-shit-javascript-interpreter.html>`__"
  by setting some homework to create a tokeniser for simple expressions
  like "1 + 2 \* 4". Two readers sent in their versions of the
  tokenisers (ps, put a link to your home work results from Part One in
  the comments, and I'll link to it here).

-  http://pastebin.com/P0sXjr65
-  http://gist.github.com/460197

|

Our simple tokeniser
--------------------

::

   operators = ['/', '+', '*', '-']
   class ParseError(Exception):
       pass
   def is_operator(s):
       return s in operators
   def is_number(s):
       return s.isdigit()

   def tokenise(expression):
       pos = 0
       for s in expression.split():
           t = {}
           if is_operator(s):
               t['type'] = 'operator'
               t['value'] = s
           elif is_number(s):
               t['type'] = 'number'
               t['value'] = float(s)
           else:
               raise ParseError(s, pos)

           t.update({'from': pos, 'to': pos + len(s)})
           pos += len(s) + 1
           yield t

::

   >>> pprint(list(tokenise("1 + 2 * 4")))
   [{'from': 0, 'to': 1, 'type': 'number', 'value': 1.0},
    {'from': 2, 'to': 3, 'type': 'operator', 'value': '+'},
    {'from': 4, 'to': 5, 'type': 'number', 'value': 2.0},
    {'from': 6, 'to': 7, 'type': 'operator', 'value': '*'},
    {'from': 8, 'to': 9, 'type': 'number', 'value': 4.0}]

|

Code for shitjs.
----------------

| You can follow along with the code for shit js at:

-  http://pypi.python.org/pypi/shitjs
-  *pip install shitjs*
-  https://bitbucket.org/illume/shitjs
-  *hg clone https://illume@bitbucket.org/illume/shitjs*

| After you have installed it, shitjs.part1 is the package for the part1
  homework.

What next? Parsing with the tokens of our simple expression.
------------------------------------------------------------

| Since we have some tokens from the input, we can now move onto the
  parser. Remember that we are not making a parser for all of javascript
  to start with, we are starting on a simple expressions like "1 + 2 \*
  4". As mentioned in Part One, we are using an algorithm called "Top
  Down Operator precedence". Where actions are associated with tokens,
  and `an order of
  operations <http://en.wikipedia.org/wiki/Order_of_operations>`__. Here
  you can see the precedence rule (order of operations) with parenthesis
  around the (1 + 2) addition changes the result.

::

   >>> 1 + 2 * 4
   9
   >>> (1 + 2) * 4
   12

|
| A number is supplied for the left, and the right of each token. These
  numbers are used to figure out which order the operators are applied
  to each other. So we take our token structure from tokenise() above,
  and we create some Token objects from them, and depending on their
  binding powers evaluate them.

What's new is old is new.
-------------------------


| The "Top Down Operator precedence" paper is from the 70's. In the 70's
  lisp programmers loved to use three letter variable names, and
  therefore the algorithm and the variable names are three letter ones.
  They also wore flares in the 70's (which are back in this season) and
  I'm not wearing them, and I'm not using three letter variable names!
| Sorry, I digress... So we call 'nud' prefix, and 'led' infix. We also
  call rbp right_binding_power, and lbp left_binding_power.
| nud - prefix
| led - infix
| rbp - right_binding_power
| lbp - left_binding_power
| Prefix is to the left, and infix is to the right.

Manually stepping through the algorithm.
----------------------------------------

| Let's manually step through the algorithm for the simple expression "1
  + 2 \* 4".

::

       >>> pprint(list(tokenise("1 + 2 * 4")))
       [{'from': 0, 'to': 1, 'type': 'number', 'value': 1.0},
        {'from': 2, 'to': 3, 'type': 'operator', 'value': '+'},
        {'from': 4, 'to': 5, 'type': 'number', 'value': 2.0},
        {'from': 6, 'to': 7, 'type': 'operator', 'value': '*'},
        {'from': 8, 'to': 9, 'type': 'number', 'value': 4.0}]

|
| Let's give left binding powers to each of the token types.

-  number - 0
-  + operator - 10
-  \* operator - 20

| Ok, so first we have a number token, with the value of 1.0. This is
  because in our shitjs so far all numbers are floats. Here is a log
  obtained by stepping through the expression.

::

   ('token', Literal({'to': 1, 'type': 'number', 'value': 1.0, 'from': 0}))
   ('expression right_binding_power: ', 0)
      ('token', OperatorAdd({'to': 3, 'type': 'operator', 'value': '+', 'from': 2}))
      ('left from prefix of first token', 1.0)
      ('token', Literal({'to': 5, 'type': 'number', 'value': 2.0, 'from': 4}))
      ('expression right_binding_power: ', 10)
          ('token', OperatorMul({'to': 7, 'type': 'operator', 'value': '*', 'from': 6}))
          ('left from prefix of first token', 2.0)
          ('token', Literal({'to': 9, 'type': 'number', 'value': 4.0, 'from': 8}))
          ('expression right_binding_power: ', 20)
              ('token', End({}))
              ('left from prefix of first token', 4.0)
              ('leaving expression with left:', 4.0)
          ('left from previous_token.infix(left)', 8.0)
          right_binding_power:10: token.left_binding_power:0:
          ('leaving expression with left:', 8.0)
      ('left from previous_token.infix(left)', 9.0)
      right_binding_power:0: token.left_binding_power:0:
      ('leaving expression with left:', 9.0)

|
| You can see that it is a recursive algorithm. Each indentation is
  where it is entering a new expression.
| Also, see how it manages to use the binding powers to make sure that
  the multiplication of 2 and 4 is done first before the addition.
  Otherwise the answer might be (1 + 2) \* 4 == 12! Not the correct
  answer 9 that it gives at the end.
| The operations are ordered this way because the + operator has a lower
  left binding power than the \* operator.
| You should also be able to see from that trace that a tokens infix and
  prefix operators are used. The OperatorAdd for example, takes what is
  on the left and adds it to the expression of what is on the right with
  it's prefix operator.
| Here is an example Operator with prefix(left) and infix(right)
  methods.

::

   class OperatorAdd(Token):
       left_binding_power = 10
       def prefix(self):
           return self.context.expression(100)
       def infix(self, left):
           return left + self.context.expression(self.left_binding_power)

|
| Pretty simple right? You can see the infix method takes the value in
  from the left, and adds it to the expression of what comes on the
  right.

Exercises for next time
-----------------------

| Make this work:

::

   >>> evaluate("1 + 2 * 4")
   9.0

|
| (ps... if you want to cheat the code repository has my part 2 solution
  in it if you want to see. The code is very short).

Until next time... Further reading (for the train, or the bathtub).
-------------------------------------------------------------------

| |reading_in_bathtub_image|
| Below is some further reading about parsers for JavaScript, and
  parsers in python.

-  `simpleparse <http://simpleparse.sourceforge.net/>`__ and `a json
   parser using
   simpleparse <http://blog.dowski.com/2010/07/21/a-json-parser-using-simpleparse/>`__.
-  `codetalker <http://jaredforsyth.com/blog/2010/jul/8/announcing-codetalker/>`__
-  `comparing python parser
   generators <http://jaredforsyth.com/blog/2010/jul/17/comparing-parser-generators-python/>`__
-  `Extended Backus–Naur Form
   (EBNF) <http://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form%20>`__

After following some of those links you may realise that we could
probably make this shitjs interpreter in an easier way by reusing
libraries. However if we wanted to do that, we'd just use an existing
JavaScript implementation! Also our JavaScript wouldn't be shit, or from
scratch.

.. |image0| image:: lets-make-a-shit-javascript-interpreter.png
   :width: 384px
   :height: 253px
.. |reading_in_bathtub_image| image:: http://img.photobucket.com/albums/v30/kiyone/ami-mizuno-sailor-mercury-reading.jpg
