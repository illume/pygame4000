Let's write a unit test!
========================

| A unit test is a piece of code which tests one thing works well in
  isolation from other parts of software. In this guide, I'm going to
  explain how to write one using the standard python unittest module,
  for the `pygame <https://www.pygame.org/>`__ game library. You can
  apply this advice to most python projects, or free/libre open source
  projects in general.

A minimal test.
---------------

| **What pygame.draw.ellipse should do**:
  http://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse
| **Where to put the test**:
  https://github.com/pygame/pygame/blob/master/test/draw_test.py

   |

   ::

      def test_ellipse(self):
          import pygame.draw
          surf = pygame.Surface((320, 200))
          pygame.draw.ellipse(surf, (255, 0, 0), (10, 10, 25, 20))

|
| All the test does is call the draw function on the surface with a
  color, and a rectangle. That's it. A minimal, useful test. If you have
  a github account, you can even edit the test file in the browser to
  submit your PR. If you have email, or internet access you can email me
  or someone else on the internet and ask them to do add it to pygame.

But why write a unit test anyway?
---------------------------------

| Unit tests help pygame make sure things don't break on multiple
  platforms. When your code is running on dozens of CPUs and just as
  many operating systems things get a little tricky to test manually. So
  we write a unit test and let all the build robots do that work for us.
| A great way to contribute to libre/free and open source projects is to
  contribute a test. Less bugs in the library means less bugs in your
  own code. Additionally, you get some public credit for your
  contribution.
| The best part about it, is that it's a great way to learn python, and
  about the thing you are testing. Want to know how graphics algorithms
  should work, in lots of detail? Start writing tests for them.

   The simplest test is to just call the function. Just calling it is a
   great first test. Easy, and useful.

|
| At the time of writing there are 39 functions that aren't even called
  when running the pygame tests. Why not join me on this adventure?

Let's write a unit test!
------------------------

| In this guide I'm going to write a test for an pygame.draw.ellipse to
  make sure a thick circle has the correct colors in it, and not lots of
  black spots. There's a bunch of tips and tricks to help you along your
  way. Whilst you can just edit a test in your web browser, and submit a
  PR, it might be more comfortable to do it in your normal development
  environment.

Grab a fork, and let's dig in.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| `Set up git for
  github <https://help.github.com/articles/set-up-git/>`__ if you
  haven't already. Then you'll want to 'fork' pygame on
  https://github.com/pygame/pygame so you have your own local copy.

   .. container::

      *Note, we also accept patches by email, or on github issues. So
      you can*\ **skip all this github business**\ *if you want
      to.*\ https://www.pygame.org/wiki/patchesandbugs

-  Fork the repository (see top right of the `pygame repo
   page <https://github.com/pygame/pygame>`__)

   .. container:: separator

      |image0|

-  Make the change locally. Push to your copy of the fork.
-  Submit a *pull request*

| So you've forked the repo, and now you can clone your own copy of the
  git repo locally.

   ::

      $ git clone https://github.com/YOUR-USERNAME/pygame
      $ cd pygame/
      $ python test/draw_test.py
      ...
      ----------------------------------------------------------------------
      Ran 3 tests in 0.007s

      OK

|
| You'll see all of the tests in the test/ folder.
| Browse the test folder online:
  https://github.com/pygame/pygame/tree/master/test
| |image1|
| If you have an older version of pygame, you can use this little
  program to see the issue.
| There is some more extensive documentation in the test/README file.
  Including on how to write a test that requires manual interaction.

Standard unittest module.
-------------------------

| pygame uses the standard python unittest module. With a few
  enhancements to make it nicer for developing C code.

   *Fun fact: pygame included the unit testing module before python
   did.*

| We will go over the basics in this guide, but for more detailed
  information please see:
| https://docs.python.org/3/library/unittest.html

How to run a single test?
-------------------------

| Running all the tests at once can take a while. What if you just want
  to run a single test?
| If we look inside draw_test.py, each test is a class name, and a
  function. There is a "DrawModuleTest" class, and there should be a
  "def test_ellipse" function.

So, let's run the test...
~~~~~~~~~~~~~~~~~~~~~~~~~

| ~/pygame/ $ python test/draw_test.py DrawModuleTest.test_ellipse
| Traceback (most recent call last):
| ...
| AttributeError: type object 'DrawModuleTest' has no attribute
  'test_ellipse'

================================================
|image2|
Starting with failure. Our test isn't there yet.
================================================

|
| Good. This fails. It's because we don't have a test called "def
  test_ellipse" in there yet. What there is, is a method called
  'todo_test_ellipse'. This is an extension pygame testing framework has
  so we can easily see which functionality we still need to write tests
  for.
| ~/pygame/ $ python tests/__main__.py --incomplete
| ...
| FAILED (errors=39)
| Looks like there are currently 39 functions or methods without a test.
  "Easy pickings".

Digression: "Low hanging fruit", "help wanted". 
-----------------------------------------------

.. container::

      *Something that's easy to do.*

|
| A little digression for a moment... what is low hanging fruit?
| Low hanging fruit is easy to get off the tree. You don't need a
  ladder, or robot arms with a claw on the end. So I guess that's what
  people are talking about in the programming world when they say "low
  hanging fruit".

=============================================================================================================================
|image3|
`pygame low hanging fruit <https://github.com/pygame/pygame/issues?q=is%3Aissue+is%3Aopen+label%3A%22Low+Hanging+Fruit%22>`__
=============================================================================================================================

|
| Many projects keep a list of "low hanging fruit", or "help wanted"
  issues. Like the `pygame low hanging
  fruit <https://github.com/pygame/pygame/issues?q=is%3Aissue+is%3Aopen+label%3A%22Low+Hanging+Fruit%22>`__
  list. Ones other people don't think will be all that super hard to do.
  If you can't find any on there labeled like this, then ask them.
  Perhaps they'll know of something easy to do, but haven't had the time
  to mark one yet.
| One little trick is that writing a simple test is quite easy for most
  projects. So if they don't have any marked "low hanging fruit", go
  take a look in their test folder and see if you can add something in
  there.
| Don't be afraid to ask questions. If you look at an issue, and you
  can't figure it out, or get stuck on something, ask a nice question in
  there for help.

Digression: Contribution guide.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| There's usually also a contribution guide.  Like the `pygame
  Contribute <https://www.pygame.org/wiki/Contribute>`__ wiki page. Or
  it may be called developer docs, or there may be a CONTRIBUTING.md
  file in the source code repository. Often there is a separate place
  the developers talk on. For the pygame project discussion happens in
  three main places. First on the discord chat server in the
  "contributing" channel. Secondly on the pygame email mailing list, and
  also inside github issues, and pull requests.

Back to the test.
-----------------

| The unittest module arranges tests inside functions that start with
  "test_" that live in a class.
| class TestStuff:
|     def test_something_works(self):
|         ''' '''
| This is a draft remember? So what is there left to finish in this doc?
| [TODO: empty todo_test with whole class]
| [TODO: image of what is wrong, moire pattern]
| [TODO: show how we test that function]
| [TODO: show pull request travis/appveyor running tests]

.. |image0| image:: https://4.bp.blogspot.com/-gyvG9zFHcEk/Wor9d2kSQAI/AAAAAAAABFE/f2aTbAp4bcc9ySdgv0MGTaQ4TtLmpyq-QCLcBGAs/s320/Screen%2BShot%2B2018-02-19%2Bat%2B17.38.48.png
   :width: 320px
   :height: 122px
   :target: https://4.bp.blogspot.com/-gyvG9zFHcEk/Wor9d2kSQAI/AAAAAAAABFE/f2aTbAp4bcc9ySdgv0MGTaQ4TtLmpyq-QCLcBGAs/s1600/Screen%2BShot%2B2018-02-19%2Bat%2B17.38.48.png
.. |image1| image:: https://2.bp.blogspot.com/-iz0rO6Hcols/WosBFD23pnI/AAAAAAAABFc/V0xlNrJtGyc33utyDR3csDI7HIRFq9M2ACLcBGAs/s320/Screen%2BShot%2B2018-02-19%2Bat%2B17.53.39.png
   :width: 150px
   :height: 320px
   :target: https://2.bp.blogspot.com/-iz0rO6Hcols/WosBFD23pnI/AAAAAAAABFc/V0xlNrJtGyc33utyDR3csDI7HIRFq9M2ACLcBGAs/s1600/Screen%2BShot%2B2018-02-19%2Bat%2B17.53.39.png
.. |image2| image:: https://2.bp.blogspot.com/-xo9yW8cGce0/Wpz9n2OQAxI/AAAAAAAABIA/nZz5eqLvScA6l_LAEU1tAgFjI8OE4KmigCLcBGAs/s320/Screen%2BShot%2B2018-03-05%2Bat%2B09.20.52.png
   :width: 320px
   :height: 84px
   :target: https://2.bp.blogspot.com/-xo9yW8cGce0/Wpz9n2OQAxI/AAAAAAAABIA/nZz5eqLvScA6l_LAEU1tAgFjI8OE4KmigCLcBGAs/s1600/Screen%2BShot%2B2018-03-05%2Bat%2B09.20.52.png
.. |image3| image:: https://4.bp.blogspot.com/-JTUSwRkfQaw/Wp0NboqPpoI/AAAAAAAABIc/JgmiFP9JXHw7DZnm0YZyG85KpzuUaLxBQCLcBGAs/s320/Screen%2BShot%2B2018-03-05%2Bat%2B10.28.10.png
   :width: 320px
   :height: 196px
   :target: https://github.com/pygame/pygame/issues?q=is%3Aissue+is%3Aopen+label%3A%22Low+Hanging+Fruit%22
