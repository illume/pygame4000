.. contents::
   :depth: 3
..

| |image0|
| Let's put the Research into R&D. I guess it should be called Shit
  Research to go along with the name of this `series
  (p1) <http://renesd.blogspot.com/2010/06/lets-make-shit-javascript-interpreter.html>`__
  of `articles
  (p2) <http://renesd.blogspot.com/2010/07/lets-make-shit-javascript-interpreter.html>`__
  I started one year ago. It takes a lot of time to read over hundreds
  of thousands of lines of undocumented C++ and java code, so part three
  took much longer than expected.

Let's explore existing JavaScript implementations.
==================================================

| In this part we are going to take a small digression to look over
  other JavaScript implementations. I'll provide a short description of
  how each JavaScript implementation is made. We can use the
  Architectural knowledge from each implementation to inspire our own
  implementation.
| Another benefit of researching each implementation is that we can find
  all the different tools they use. For example different test suites.
| Make sure to read the URL's for each implementation to find out more
  information about each one.
| `There is a list of ECMAScript implementations at
  wikipedia <http://en.wikipedia.org/wiki/List_of_ECMAScript_engines>`__.
  We will not cover all of the ones listed there. If like me, you may
  spend a few hours or even days reading through the links from there.

narcissus - js in js.
---------------------

| Narcissus is a javascript implementation written in javascript (with
  some SpiderMonkey language extensions). It is written by the same
  author as the original JavaScript implementation back in 2005-2007
  (`Brendan Eich <http://brendaneich.com/>`__). In mid 2010 the
  Narcissus code has been taken up again by the Mozilla project to make
  researching JavaScript changes easier.
| It is a good implementation to study, since it is fairly small, and is
  meant to be easy enough to read.
| It uses a hand written parser, not a generated one.
| `The original narcissus source
  repository <http://mxr.mozilla.org/mozilla/source/js/narcissus/>`__.
| The new `repository of
  narcissus <https://github.com/mozilla/narcissus/>`__, and
  `two <http://mozillalabs.com/zaphod/2010/09/18/28/>`__
  `articles <http://blog.mozilla.com/dherman/2010/09/22/zaphod-a-browser-language-lab-for-js/%20>`__
  about it.
| There is a port to python of the narcissus parser called
  `pynarcissus <http://code.google.com/p/pynarcissus/>`__. The authors
  of pynarcissus found it difficult to port the rest of the interpreter
  since it relies on JavaScript features itself.
| It weighs in at about 7000 lines of code counted with wc -l. I had to
  count lines in this way since my SLOC counter does not seem to count
  javascript.

Spider monkey.
--------------

| `Spider Monkey <http://www.mozilla.org/js/spidermonkey/>`__ is the
  original JavaScript implementation used by Netscape, and the Mozilla
  project.
| SpiderMonkey is a production grade, high quality JavaScript
  implementation.
| It also has excellent documentation. Especially the
  `js/src/README.html <http://mxr.mozilla.org/mozilla/source/js/src/README.html>`__
  file which includes a design walk through.
| """*The compiler consists of a recursive-descent parser and a
  random-logic rather than table-driven lexical scanner. Semantic and
  lexical feedback are used to disambiguate hard cases such as missing
  semicolons, assignable expressions ("lvalues" in C parlance), etc. The
  parser generates bytecode as it parses, using fixup lists for downward
  branches and code buffering and rewriting for exceptional cases such
  as for loops. It attempts no error recovery. The interpreter executes
  the bytecode of top-level scripts, and calls itself indirectly to
  interpret function bodies (which are also scripts). All state
  associated with an interpreter instance is passed through formal
  parameters to the interpreter entry point; most implicit state is
  collected in a type named JSContext. Therefore, all API and almost all
  other functions in JSRef take a JSContext pointer as their first
  argument.
  The decompiler translates postfix bytecode into infix source by
  consulting a separate byte-sized code, called source notes, to
  disambiguate bytecodes that result from more than one grammatical
  production.*"""

Google V8.
----------

| Written in C++, javascript and assembler. Uses hidden classes, and
  generates machine code at run time.
| The parser is hand written parser in C++. It's not generated.
| 'Preparses', which creates tokens. Then creates an AST by parsing.
  Finally compiling the AST. parser.css is where all the parsing
  happens.
| The projects documentation is quite limited - so reading the source is
  the best way to get in there. There are some videos which describe the
  architecture, and engineering decisions behind the choices taken.
| http://code.google.com/p/v8/
| V8 weighs in at a mighty 605,962 SLOC. Making it the largest, biggest,
  badest V8 JavaScript engine around.

JSLint.
-------

| JSLint is written in JavaScript and uses a TDOP approach to the parser
  like we are using. I won't discuss this, since it is documented well
  elsewhere.

Rhino
-----

| Rhino can run as either an interpreter or a java byte code generator.
  It's hosted by the mozilla project (who make firefox). It complements
  their C++ implementation (spidermonkey) and their JavaScript
  implementation (narcissus).
| There are a few things which show it is a very mature as well as
  modern implementation. The project was started in 1999, and has been
  developed ever since. It has partial support for JavaScript 1.8, and
  ECMAScript 5 standards. Weighing in at 50,551 source lines of Java
  code (SLOC), it can be considered a very large code base. Another
  modern feature is that it supports the CommonJS javascript module
  standard. Despite still being hosted in cvs, it's still being
  maintained, and features are being added regularly.
| The Rhino JavaScript team maintains a library of tests and other
  documentation for JavaScript. Tests are being shared with the other
  JavaScript implementations within the mozilla spidermonkey project.
  There have also been parts which have been ported from spidermonkey -
  such as the hand written parser.
| A handwritten scanner they call TokenStream creates tokens, and then
  parses those into an AST. Despite being mostly hand written, some
  parts are generated. Specifically the stringToKeyword method, which
  detects keywords is generated somehow.
| The documentation of the architecture of the project is limited. There
  is however some API documentation. With a couple of modifications to
  some ant build files I was able to build it, as well as even make a
  few small modifications.
| The `wikipedia
  Rhino <http://en.wikipedia.org/wiki/Rhino_%28JavaScript_engine%29>`__
  page has some great information on the rhino javascript engine.

KJS
---

| `KJS <http://en.wikipedia.org/wiki/KJS_%28KDE%29>`__ is the KDE
  JavaScript implementation for the konqueror browser. It was the parent
  of the JavaScript implementations done by Apple Computer, inc. I won't
  go into any detail on this one, since I'll cover JavaScriptCore
  instead. KJS is written in C++, for the QT library.

JavaScriptCore, Squirrelfish, Nitro
-----------------------------------

| You can browse the source here:
  http://trac.webkit.org/browser/trunk/Source/JavaScriptCore
| This uses a hand written lexer(tokeniser), and a hand written parser.
  The code structure of the parser and lexer looked eerily familiar. The
  code base is mostly written in C++ and is quite massive. 140,837 SLOC
| There is lots of platform specific code, but it also has a jit, uses
  byte code, and an interpreter. There is also lots of development code
  in there for things like debuggers, and profilers.

Closed source JavaScript implementations
----------------------------------------

|
| There are a few JavaScript implementations that are closed source. The
  two main ones in widespread use are the ones from Microsoft, and the
  ones from Opera.
| They have however published papers and blog posts about their
  implementations. I won't cover them any more, because not as much can
  be learned without the source code.

pypy javascript
---------------

| The pypy project started a javascript interpreter now too.
| https://bitbucket.org/pypy/lang-js/src/de89ec32a7dc/js/javascript-interpreter.txt
| The description of the project mentions it's currently using the
  spider monkey parser, but it appears to generate one using a parser
  generator provided by pypy. Using a EBNF grammar file. It also creates
  an AST.
| It works for some simple javascript programs that don't use the
  javascript standard library. I'm not sure of the future of the
  project, since it appears it was a GSOC project which has now
  finished, so there might not be any full time developers left on it.
| It's written in RPython (a restricted subset of python) and python.
  Running on top of pypy, it should theoretically be able to take
  advantage of that platforms jit and garbage collector.
| This project makes use of some JavaScript tests and benchmarks from
  other projects. Specifically some benchmarks from v8, and the language
  shootout website. It also includes the "ECMA 262 Edition 1" tests.
| It weighs in at 5452 Source Lines of Code (SLOC). Which is much
  smaller, but the implementation is also not complete, so that is to be
  expected.

So what have we learned then?
-----------------------------

|
| We see that most of the implementations use a hand written parser. We
  also see that the implementations in js and python are much smaller.
  So despite them being incomplete, I think it proves that it should be
  feasible to make our shit interpreter in python. We don't need half a
  million lines of C++ to do our project.
| We have also learned that there are test suites available, which
  should help us out a lot. In fact, many of the implementations share
  the test suites. Having a test suite already available makes it way
  easier to write an implementation of something yourself. It acts as a
  guide to development, and also reduces the time for testing since a
  lot of it can be automated.

Exercise for next time
----------------------

|
| Choose One(1) of the implementations, build it, run it, and modify it
  slightly to do something different. Try and run the tests that come
  with it.

Further reading.
----------------

| This whole article is "further reading", but we can never have too
  much to read. Can we!?
| This time, instead of reading it on the train or in the bath tub - may
  I suggest reading these on a couch?

-  `Functions and execution contexts in
   JavaScript <http://blog.tuenti.com/dev/functions-and-execution-contexts-in-javascript-2/>`__
-  `jslex, a javascript lexer written in
   python <http://nedbatchelder.com/blog/201104/a_javascript_lexer_in_python_and_the_saga_behind_it.html>`__
-  http://ruslanspivak.com/2011/05/02/slimit-a-javascript-minifier-to-be-is-released/
   (`pypi slimit <http://pypi.python.org/pypi/slimit>`__)
-  `UglifyJS <https://github.com/mishoo/UglifyJS>`__
-  `Closure Compiler <http://code.google.com/closure/compiler/>`__

.. |image0| image:: lets-make-a-shit-javascript-interpreter.png
   :width: 384px
   :height: 253px
