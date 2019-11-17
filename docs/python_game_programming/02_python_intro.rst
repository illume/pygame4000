Python game programming part 2 - Introduction to Python
=======================================================

What is Python?

Python has been accurately described as pseudo-code that runs.

Python is an interpreted language, which means that it is not converted
to machine code and is processed by a Python interpreter instead of your
computer's CPU. Python compiles into byte-code like Java, unlike Perl.
Python uses run-time dynamic typing, unlike Java or C++ which require
you to declare types before compiling.


Variables
~~~~~~~~~

Python variables work on references, and have automatic garbage
collection so you do not need to worry about allocating or freeing
memory. Python variables can be re-assigned at any time to different
types of data. For instance, this is perfectly legal:

::

   var = 5
   var = 5.5
   var = 'Five'

Some people who are familiar with other languages consider this
flexibility to be dangerous, but in practice it is very rarely a
problem.


Code Blocks
~~~~~~~~~~~

Python structures it's code based on whitespace (spaces or tabs). This
is unusual for programming languages, and is the biggest factor keeping
people who are currently programmers in other languages from giving
Python a good try. Some existing programmers can never get used to the
whitespace code blocks, but the majority of Python converts end up
liking whitespace codeblocks even better than the standard bracket
method of C++, Java, Perl.

Python accepts new commands on new lines, and accepts code blocks based
on the amount of whitespace before any non-whitespace charters. For
example:

::

   # layer variable used to describe what "layer" of code block indentation we are on
   layer = 1
   # Always true if statement to show nested code blocks
   if True:
      # Nested blocks are indented with 3-4 spaces or a tab character.
      layer = 2
   else:
      layer = 2
      if True:
         # Third "layer" of nesting.  2 code blocks deep.
         layer = 3

         # Blank lines can be inserted into code blocks, whitespace does not matter on blank lines
         layer = 3

      # After a code block is finished, you revert down to the next code block that you will continue from.
      # You could drop several could block "layers" at once
      layer = 2

Whitespace can consist of spaces or tabs, but it should be consistent
through your entire file. Mixing tabs and spaces in a codeblock will
cause an error, and mixing them in a file will cause later frustration.

In the example above, you can also see how code blocks are specified.
Any line that ends with a colon (:) will tell the Python compiler that
the next line should be a sub-code block. This means that the next line
should have more whitespace than it's parent line.

It does not matter how many whitespace characters are used, as long as
it is more than it's parent and consistent. Usually 3 or 4 spaces are
used, or 1 tab. Blank lines are ignored, and it doesn't matter how many
whitespace characters are on them.

Comments are done by placing a hash character (#) not in a string. The
rest of the line is considered commented.


Why Python Code Blocks are Good
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Why change the standard way to format code? It's been in practice for
40 years, why change now?**

Everyone indents their code anyway. Why specify indentation with both
whitespace AND brackets? There are two religions to bracket code
blocking in C++/Java/Perl, compare with Python:

::

   if (something) {
      doStuff();
      while (1) {
         doMore();
      }
   }

or

::

   if (something)
   {
      doStuff();
      while (1)
      {
         doMore();
      }
   }

compared to Python:

::

   if something:
      do_stuff()
      while 1:
         do_more()

Each of these require you to different eye-gymnastics, and over large
file introduce errors. Especially when code block brackets are optional
for single line code blocks, making you potentially miss where a code
block was not properly specified.

Compare both of the C++/Java/Perl common code bracket methods with the
lower Python method of whitespace indentation. Which is easier to read?
Which uses the least vertical whitespace? Given 5 pages worth of code,
which would you be more likely to make a mistake reading or editing?

**Removing unnecessary characters.**

Python also promotes removing unnecessary characters from your code. If
every line of code is placed on a separate line, why do you need to end
every statement with a semi-colon?

Additionally, if parentheses are not necessary, you are not required to
have them and English equivalents are available instead of using symbols
for logical operations. As a C/C++ programmer for over 15 years, I
considered it no big deal to visually parse C symbols, but I noticed
after doing things the Python way for a year how much easier it is to
read. Compare:

C++/Java:

::

   if (a == b && c == d) {
      doStuff();
   }

Python:

::

   if a == b and c == d:
      doStuff()

**Everyone does it the same way.**

No more debates about code style on where to put the brackets, no more
having to read differently every file you go to.

Almost.

There is still a choice between spaces and tabs. I'm told spaces are
more usualy, but I prefer tabs. However, this is very easy to deal with,
and most editors can treat them both the same way if you configure them.

However, the differences between peoples code is greatly reduced.
Interestingly, Python code usually looks more alike than other
languages. Python coders tend to do things the same way, as it is easy,
works well, and is encouraged. This is a Good Thing.


Python Is About You
~~~~~~~~~~~~~~~~~~~

Everything about Python is created to make development easier for the
programmer, as opposed to making programming easier for the compiler or
CPU. You have probably heard the often repeated, but often ignored,
mantra of "optimize last". Python takes this mantra to heart, and the
optimizations of other languages to make their life easier at the
expense of you, the programmer, are avoided in Python.

To hear more about reasons why Python has made some smart choices, you
can read an interview with Bruce Eckel (author of Thinking in C++ and
Thinking in Java) about why he has chosen Python as his language of
choice: `Python and the Programmer: A Conversation with Bruce
Eckel <http://www.artima.com/intv/aboutme.html>`__


Zen of Python
~~~~~~~~~~~~~

This sums up Python's goals and aspirations nicely.

::

   The Zen of Python (by Tim Peters)

   Beautiful is better than ugly.
   Explicit is better than implicit.
   Simple is better than complex.
   Complex is better than complicated.
   Flat is better than nested.
   Sparse is better than dense.
   Readability counts.
   Special cases aren't special enough to break the rules.
   Although practicality beats purity.
   Errors should never pass silently.
   Unless explicitly silenced.
   In the face of ambiguity, refuse the temptation to guess.
   There should be one-- and preferably only one --obvious way to do it.
   Although that way may not be obvious at first unless you're Dutch.
   Now is better than never.
   Although never is often better than *right* now.
   If the implementation is hard to explain, it's a bad idea.
   If the implementation is easy to explain, it may be a good idea.
   Namespaces are one honking great idea -- let's do more of those!


Using Python
------------

Now that you have a little insight into what Python is, you will want to
see it in action a little. These lectures are not intended to be full
Python tutorials, because there are a lot of good resources out there
already for this. What we will do is show you how to use the basics of
Python, how to do interesting things with it, how to apply these techniques
to game development, and finally how to make games with this knowledge.


Python from the Interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

My first experience with interactively interpreted languages was using
Prolog many years ago, and it made a profound impact on me. I always
remember Prolog fondly, even though it was very cryptic and hard to do
simple things with, because I could watch my results change as I typed
them in.

Luckily, interactive interpretation is back, and this time is it now
easy to do practical things!

To load up your interpreter run the command "python.exe" on windows:

Start -> Run -> Type: "python"

Or go to the C:\Python38\\ and double-click "python.exe".

You should now see a window like this (but taller, I shrunk mine):

|interp_01|

If you get an error, or do not see something like this you may have a
problem with your installation, or you are clicking in the wrong place.
You may need to add the Python directories to your path. You can do this
from your Control Panel -> System -> Advanced -> Environment Variables.

To PATH, add C:\Python38\\ and C:\Python38\Scripts\\


Interpreter Conventions
~~~~~~~~~~~~~~~~~~~~~~~

In your interpreter the starting characters '>>> ' are telling you that
it is expecting a new line. The characters '... ' is telling you that it
expects a continuation of a code block. If you do not properly terminate
a command it will show you this '... ' prompt until you properly end the
command. Check for non-terminated strings or parentheses.

You can press the UP and DOWN keys to cycle through you command history,
and LEFT/RIGHT/HOME/END/CTRL+LEFT/CRTL+RIGHT will allow you to move over
your line and edit it.

To quit the Python interpreter, press CRTL+Z and then ENTER in Windows
or CRTL+D in Unix.


Live, from your living room... It's Python!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have the formalities out of the way, it's time to kick
things into gear and check out Python in action.

Let's set some variables:

::

   >>> i = 5

We have now set the variable 'i' to be bound to a object containing the
integer 5. If this makes no sense to you, thats ok! Just know that when
you assign things like "i = 5", 'i' now is equal to 5. The specifics of
what are going on will be explaned later, and in most cases, you will
never care.

We can inspect the variable by typing it alone:

::

   >>> i
   5

Here we see what the variable now contains. We can get any returned
value this way, like so:

::

   >>> i * 5
   25

As long as the value being returned is not being assigned to a variable,
then it is output to the interpreter screen. Let's assign it to a
variable now:

::

   >>> j = i * 5
   >>> j
   25

You can see that after the first operation nothing was printed out, but
when we specified 'j' by itself and did not assign it into a variable,
then it was output onto the screen. This will help you troubleshoot
different functions later on, by letting them fall through into the
interpreter so you can see them.


Basic Variable Types
~~~~~~~~~~~~~~~~~~~~

Let's cover a few different types of data that can be put into a Python
variable.

We have already seen that Python takes integers (whole numbers), and it
also takes floating point numbers (real numbers), and strings. This
makes up the standard set of variables:

::

   >>> a = 1
   >>> b = 1.0
   >>> c = 'One'
   >>> a
   1
   >>> b
   1.0
   >>> c
   'One'

Strings can either use single or double quotes, and the only difference
between them is which quote you will have to escape. Example:

::

   s1 = 'Test "single" quote.'
   s2 = "Test 'double' quote."
   s3 = 'Test \'single\' escaped quote.'
   s4 = "Test \"double\" escaped quote."

Everything in Python is an Object. This means that every variable has
functions associated with it that can operate on the variable in
different ways. You can see the functions by using the dir() function:

::

   >>> dir(1)
   ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__',
   '__divmod__', '__doc__', '__float__', '__floordiv__', '__getattribute__', '__hash__', '__hex__',
   '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__',
   '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
   '__rdiv__', '__rdivmod__', '__reduce__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
   '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
   '__rxor__', '__setattr__', '__str__', '__sub__', '__truediv__', '__xor__']

That's a lot of functions inside of a "1" :)

This covers all of the operations that can be done on or against this
variable. So "1 \* 2" will actually call the function 1.mul(2). The ""
characters are used to describe private functions to an object, and
while they look a little ugly, you rarely need to use them directly, so
it doesn't matter.

You can use the dir() function

Now, let's see some interesting things we can do with strings.

We start out by setting our string variable 's'.

::

   >>> s = 'Hi, Im a Python string, and I am all powerful!'

Then we run the function upper() on the variable, and we see the result
that the string variable has now been returned as upper case. No change
is made to the variable 's', because it has not be re-assigned.

::

   >>> s.upper()
   'HI, IM A PYTHON STRING, AND I AM ALL POWERFUL!'

You may be wondering what the dot (.) is in the above command. Remember
how we used the dir() function before? Let's try it again:

::

   >>> dir(s)
   ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
   '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__',
   '__init__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
   '__reduce__', '__repr__', '__rmul__', '__setattr__', '__str__', 'capitalize',
   'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'index',
   'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join',
   'ljust', 'lower', 'lstrip', 'replace', 'rfind', 'rindex', 'rjust', 'rstrip', 'split',
   'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

Here are all the commands that are present in the string Object in
Python. An object can have functions (sometimes called methods)
associated with them. You can call any of these functions by using the
above "dot notation", so s.upper() or s.lower() are both available for
manipulating this string. In Python, functions that start with two
underscores () are private, and cannot be called directly.

Next we will search the string for the sub-string 'all'.

::

   >>> s.find('all')
   33

We receive the position 33 for the sub-string 'all', this means that the
string 'all' appears as the 33rd position in our string. Let's use that
and get an index from our string. This should be familiar to C++ people.

::

   >>> s[33]
   'a'

Now we will try something new that does not exist in the C++ style
worlds. We will use what is called a *slice* in Python. This can be used
on anything that is a *sequence*, which strings are. We will cover other
sequences shortly.

>>> s[33:] 'all powerful!'

We have gotten the slice "from position 33 to the end of the string"
with the above command. Now let's try the opposite.

>>> s\ `33 <33>`__ 'Hi, Im a Python string, and I am '

Here we have from the beginning of the string to position 33. Slicing is
very powerful, and there are several additional ways to use slicing that
we will cover later.


Introduction to Container Variable Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Up to now we have seen some pretty standard programming types, but
containers are where Python shines. If for no other reason, this feature
set was the one that really enamored me to Python. The simplicity and
elegance of Python containers is quite something, in my humble opinion.

Now that I have unreasonably (but correctly :) ) set expectations,
let's see what the containers are:

Sequence:

::

   >>> a = (1, 3, 5, 7)
   >>> a
   (1, 3, 5, 7)
   >>> a[1]
   3

A sequence is a series of variables that are contained together in...
sequence. They can be any variable types, including other sequence or
containers. Sequences are immutable, which means that you cannot add,
remove or change items once the sequence is created. This is very
similar to an Array in Java, and has some similarities to arrays in C,
except that you cannot change data in the elements.

List:

::

   >>> b = [2, 4, 6, 8]
   >>> b
   [2, 4, 6, 8]
   >>> b[1]
   4

A list is sequence that is mutable. You can add, remove and change
elements in it. Lists have methods (another name for a function inside
an Object) for sorting and reversing the list. Lists can be treated as
stacks or queues with append(), pop() and remove() functions.

Dictionary:

::

   >>> c = {'a':0, 'b':1, 'c':2}
   >>> c
   {'a': 0, 'c': 2, 'b': 1}
   >>> c['b']
   1

A dictionary is Python's version of a hash or map. It assigns a value to
a key, as is standard for "key-pair" stored data. This gives immediate
access to any data, so that you do not have to step through an entire
list to find something, provided you know it's key.

If you were wondering. While you can do:

::

   >>> c['b']
   1

You cannot do:

::

   >>> c[1]
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   KeyError: 1

Because dictionaries are not 2-way hashes. This isn't to say that this
cant be done, and in fact it is not very difficult at all to do, but it
is not default functionality. By the way, using integers for dictionary
keys is perfectly acceptable, this example failed simply because there
was no key of 1.


Using Container Variables
~~~~~~~~~~~~~~~~~~~~~~~~~

Feeling under whelmed by the Amazing Python Containers? Hopefully not
too much, but at first look they are not so much as amazing as simple
"readable" in my book. Their real power comes from Python's ability to
mix types together. For instance, this is valid:

::

   >>> d = [5, 5.5, 'Five to Five', (5, 6)]
   >>> d
   [5, 5.5, 'Five to Five', (5, 6)]
   >>> d[1]
   5.5
   >>> d[2]
   'Five to Five'

I have now mixed 4 different types of data into a single list. An
integer, a float, a string and a sequence are all living happily
together. What's more, they have all retained their normal state and did
not have to be turned into "generic objects" as they would have to be in
some other Object Oriented languages, so they can be extracted and used
as-is.

I believe in Data Driven Programming, so while I have named this section
to be able containers I am going to introduce you to various other
Python concepts for handling sequences. Let's see how we can use some of
this container goodness:

::

   >>> for item in d:
   ...    print(item)
   ...
   5
   5.5
   Five to Five
   (5, 6)

Introducing Python's version of the for loop. Python breaks tradition
once again, and instead of setting a starting variable, checking that it
is still in range, and incrementing, it simply iterates over a sequence.

'd' is a list, which is a mutable sequence. This sequence is then cycled
over, starting at the first item and assigning it into the variable
'item' and executing the code block. After the code block, the for loop
returns to the 'd' variable and retrieves the next 'item' in the
sequence. When it is out of items, it moves past the for loop. Elegant.

Let's see it work over our dictionary.

::

   >>> c
   {'a': 0, 'c': 2, 'b': 1}
   >>> c.keys()
   ['a', 'c', 'b']
   >>> for key in c.keys():
   ...    print('%s: %d' % (key, c[key]))
   ...
   a: 0
   c: 2
   b: 1

We start by checking the contents of 'c' again. A dictionary with string
keys attached to integer values.

We want to loop over the keys in this dictionary, so let's look at the
keys with the function keys(). Here we can see all the keys in the
dictionary returned in a list.

So now we will do a for loop over the 'c.keys()' returned list, and the
variable key will contain the key for each dictionary entry. We want to
print out the results, so we will use the print() command, again because
Python likes to conserve the use of symbols you can see that I do not
need to type the parentheses around print (but I could if I wanted to).

If you are familiar with sprintf() in C++, you may find this a pleasant
surprise. Any string can be formatted by the syntax sugar of: 'string %s
' % variable.

Here we are substituting a string (%s) and a integer (%d), and so we
feed in a Sequence of the key and 'c' dictionary value at index 'key'
into the format command. This new formatted string is then passed to the
print() function and output to the interpreter.

If there was only one variable, you would not need the parentheses to
build a Sequence.


Return of the Slice
~~~~~~~~~~~~~~~~~~~

Remember slicing strings? Well, I said strings were sequences and any
sequences can be sliced, so let's try it out on a list:

::

   >>> b = [2, 4, 6, 8, 10, 12, 14, 16]
   >>> b
   [2, 4, 6, 8, 10, 12, 14, 16]

We start off with a basic list of even numbers.

::

   >>> b[4]
   10

We can get an index out of the list, this is like a 1 item slice.

::

   >>> b[4:]
   [10, 12, 14, 16]

Here we slice from position 4 to the end of the sequence.

::

   >>> b[:4]
   [2, 4, 6, 8]

And here we slice from the beginning of the sequence to the 5th
position. Something worth mentioning: computers do not start counting
from 1, they start from 0. So position 4, is actually the 5th position.
0, 1, 2, 3, 4.

::

   >>> b[4:6]
   [10, 12]

Here we slice from the 5th position to the before 7th position. The end
position is not returned, only up to it.

::

   >>> b[-1]
   16

Here we use a negative slice to select the last item in the sequence.

::

   >>> b[1:-1]
   [4, 6, 8, 10, 12, 14]

Here we select from the 2nd position to the 2nd to last position. Again,
the end position is not returned, since -1 gives us the "last element",
then doing a slice to -1 gives us up to the "2nd to last" element.

As you can see, slicing can give you powerful access to sequences.


Run-Time Type Checking
~~~~~~~~~~~~~~~~~~~~~~

Python may not require you to specify variable types in your code, but
that does not mean Python does not care what your variable types are.
Mixing variable types is only allowed in circumstances where it is seen
as a proper things to do, in all other situations you must first convert
the variables to a common type before they can be used together.

Integers and Floats are converted into Floats.

::

   >>> 5 + 5.0
   10.0

Lists may be added together. Sequences may be added together.

::

   >>> [1,3] + [3,4]
   [1, 3, 3, 4]
   >>> (1,2) + (3,4)
   (1, 2, 3, 4)

Lists and sequences must not be added together. Convert the sequence
into a list first.

::

   >>> (1,2) + [3,4]
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   TypeError: can only concatenate tuple (not "list") to tuple
   >>>
   >>> list((1,2)) + [3,4]
   [1, 2, 3, 4]

Lists and sequences may be multiplied by integers. They may not have
other operations done on them with integers.

::

   >>> (1,2) * 2
   (1, 2, 1, 2)
   >>>
   >>> (1,2) + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   TypeError: can only concatenate tuple (not "int") to tuple

Strings, as sequences, can also be multiplied by integers.

::

   >>> 'PYTHON! ' * 3
   'PYTHON! PYTHON! PYTHON! '

When formatting strings, converting from an integer to a string is
allowed. The opposite is not true.

::

   >>> 'Str: %s Num: %s' % ('python', 5)
   'Str: python Num: 5'
   >>>
   >>> 'Str: %s Num: %d' % ('python', 'Five')
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   TypeError: an integer is required

So if you refer back to the section containing the Zen of Python, you
will see it's explanations in effect here. Where things are expected,
they are performed. Where they are not expected, errors are thrown.


Exercises
---------


How do you get rid of the trailing space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   >>> 'PYTHON! ' * 3
   'PYTHON! PYTHON! PYTHON! '

What does this code do?
~~~~~~~~~~~~~~~~~~~~~~~

::

   a = {15:'dog', 22:'cat', 35:'beard', 99:'emu', 101:'llama'}
   b = (38, 22, 19, 99, 22, 14, 100, 101, 15)
   for item in b:
      if a.has_key(item):
         a[a[item]] = item

How do you find out what functions you can perform on a dictionary?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How would you find the 5th item from the last in a sequence of 20 items?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Without trying it first, is this legal?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   >>> (1,2) + [4,5]


Next
~~~~

`Part Three <_03_pygame_introduction>`__
