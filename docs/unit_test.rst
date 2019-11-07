Let's write a unit test!
========================

| A unit test is a piece of code which tests one thing works well in
  isolation from other parts of software. In this guide, I'm going to
  explain how to write one using the standard python unittest module,
  for the `pygame <https://www.pygame.org/>`__ game library. You can
  apply this advice to most python projects, or free/libre open source
  projects in general.

A minimal test
--------------

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
| An easy test to write... but it provides really good value.

-  Shows an example of using the code.
-  Makes sure the function arguments are correct.
-  Makes sure the code runs on 20+ different platforms and python
   versions.
-  No "regressions" (Code that starts failing because of a change) can
   be introduced in the future. The code for draw ellipse with these
   arguments should not crash in the future.

|

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

::

   ~/pygame/ $ python test/draw_test.py DrawModuleTest.test_ellipse
   Traceback (most recent call last):
   ...
   AttributeError: type object 'DrawModuleTest' has no attribute 'test_ellipse'

|

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

::

   ~/pygame/ $ python -m pygame.tests --incomplete

| ...
| FAILED (errors=39)
| Looks like there are currently 39 functions or methods without a test.
  Easy pickings.

Python 3 to the rescue.
-----------------------

| Tip: Python 3.7 makes it easier to run tests with the magic "-k"
  argument. With this you can run tests that match a substring. So to
  run all the tests with "ellipse" in their name you can do this:

::

   ~pygame/ $ python3 test/draw_test.py -k ellipse

|

Digression: Good first issue, low hanging fruit, and help wanted. 
-----------------------------------------------------------------

.. container::

      *Something that's easy to do.*

|
| A little digression for a moment... what is a good first issue?
| Low hanging fruit is easy to get off the tree. You don't need a
  ladder, or robot arms with a claw on the end. So I guess that's what
  people are talking about in the programming world when they say "low
  hanging fruit".

=============================================================================================================================
|image3|
`pygame low hanging fruit <https://github.com/pygame/pygame/issues?q=is%3Aissue+is%3Aopen+label%3A%22Low+Hanging+Fruit%22>`__
=============================================================================================================================

|
| Many projects keep a list of "good first issue", "low hanging fruit",
  or "help wanted" labeled issues. Like the `pygame "good first
  issue" <https://github.com/pygame/pygame/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`__
  list. Ones other people don't think will be all that super hard to do.
  If you can't find any on there labeled like this, then ask them.
  Perhaps they'll know of something easy to do, but haven't had the time
  to mark one yet.
| One little trick is that writing a simple test is quite easy for most
  projects. So if they don't have any marked "low hanging fruit", or
  "good first issue" go take a look in their test folder and see if you
  can add something in there.
| Don't be afraid to ask questions. If you look at an issue, and you
  can't figure it out, or get stuck on something, ask a nice question in
  there for help.

Digression: Contribution guide.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| There's usually also a contribution guide.  Like the `pygame
  Contribute <https://www.pygame.org/wiki/Contribute>`__ wiki page. Or
  it may be called developer docs, or there may be a CONTRIBUTING.md
  file in the source code repository. Often there is a separate place
  the developers talk on. For pygame it is the pygame mailing list, but
  there is also a chat server which is a bit more informal.

A full example of a test.
-------------------------

| The unittest module arranges tests inside functions that start with
  "test_" that live in a class.
| Here is a full example:

::

   import unittest


   class TestEllipse(unittest.TestCase):

       def test_ellipse(self):
           import pygame.draw
           surf = pygame.Surface((320, 200))
           pygame.draw.ellipse(surf, (255, 0, 0), (10, 10, 25, 20))


   if __name__ == '__main__':
       unittest.main()

|
| You can save that in a file yourself(test_draw1.py for example) and
  run it to see if it passes.

Committing your test, and making a Pull Request.
------------------------------------------------

| Here you need to make sure you have "git" setup. Also you should have
  "forked" the repo you want to make changes on, and done a 'git clone'
  of it.

::

   # create a "branch"
   git checkout -b my-draw-test-branch

   # save your changes locally.
   git commit test/draw_test.py -m "test for the draw.ellipse function"

   # push your changes
   git push origin my-draw-test-branch

|
| Here we see a screenshot of a terminal running these commands.

======================================================================
|image4|
Here we see the commands to commit something and push it up to a repo.
======================================================================

| When you push your changes, it will print out some progress, and then
  give you a URL at which you can create a "pull request".
| When you git push it prints out these instructions:

::

   remote: Create a pull request for 'my-draw-test-branch' on GitHub by visiting:
   remote:      https://github.com/YOURUSERNAME/pygame/pull/new/my-draw-test-branch

|
| You can also go to your online fork to create a pull request there.

Writing your pull request text.
-------------------------------

| When you create a pull request, you are saying "hey, I made these
  changes. Do you want them? What do you think? Do you want me to change
  anything? Is this ok?"
| It's usually good to link your pull request to an "issue". Maybe
  you're starting to fix an existing problem with the code.

============================================================================================
|image5|
Different "checks" are run by robots to try and catch problems before the code is merged in.
============================================================================================

|

Testing the result with assertEquals.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|
| How about it we want to test if the draw function actually draws
  something?
| Put this code into test_draw2.py

::

   import unittest


   class TestEllipse(unittest.TestCase):

       def test_ellipse(self):
           import pygame.draw
           black = pygame.Color('black')
           red = pygame.Color('red')

           surf = pygame.Surface((320, 200))
           surf.fill(black)

           # The area the ellipse is contained in, is held by rect.
           #
           # 10 pixels from the left,
           # 11 pixels from the top.
           # 225 pixels wide.
           # 95 pixels high.
           rect = (10, 11, 225, 95)
           pygame.draw.ellipse(surf, red, rect)

           # To see what is drawn you can save the image.
           # pygame.image.save(surf, "test_draw2_image.png")

           # The ellipse should not draw over the black in the top left spot.
           self.assertEqual(surf.get_at((0, 0)), black)

           # It should be red in the middle of the ellipse.
           middle_of_ellipse = (125, 55)
           self.assertEqual(surf.get_at(middle_of_ellipse), red)


   if __name__ == '__main__':
       unittest.main()

|

======================================
|image6|
Red ellipse drawn at (10, 11, 225, 95)
======================================

|

What is a git for? Jargon.
--------------------------

| `jargon <https://en.wikipedia.org/wiki/Jargon_File>`__ - internet
  slang used by programmers. Rather than use a paragraph to explain
  something, people made up all sorts of strange words and phrases.
| `git <https://en.wikipedia.org/wiki/Git>`__ - for sharing versions of
  source code. It lets people work together, and provides tools for
  people to.
| `pull
  request <https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests>`__
  (PR) - "Dear everyone, I request that you **git pull** my commits.". A
  pull request is a conversation starter. "Hey, I made a PR. Can you
  have a look?". When you "**git push**" your commits (upload your
  changes).
| `unit test <https://en.wikipedia.org/wiki/Unit_testing>`__ - **does
  this thing**\ (*unit*) **even work**\ (*test*)?!!? A program to test
  if another program works (how you think it should). Rather than test
  manually over and over again, a unit test can be written and then
  automatically test your code. A unit test is a nice example of how to
  use what you've made too. So when you do a pull request the people
  looking at it know what the code is supposed to do, and that the
  machine has already checked the code works for them.
| `assert <https://en.wikipedia.org/wiki/Assertion_(software_development)>`__
  - "assert 1 == 1". An assert is saying something is true. "I assert
  that one equals one!". You can also assert variables.

.. |image0| image:: https://web.archive.org/web/20191007225130im_/https://4.bp.blogspot.com/-gyvG9zFHcEk/Wor9d2kSQAI/AAAAAAAABFE/f2aTbAp4bcc9ySdgv0MGTaQ4TtLmpyq-QCLcBGAs/s320/Screen%2BShot%2B2018-02-19%2Bat%2B17.38.48.png
   :width: 320px
   :height: 122px
   :target: https://4.bp.blogspot.com/-gyvG9zFHcEk/Wor9d2kSQAI/AAAAAAAABFE/f2aTbAp4bcc9ySdgv0MGTaQ4TtLmpyq-QCLcBGAs/s1600/Screen%2BShot%2B2018-02-19%2Bat%2B17.38.48.png
.. |image1| image:: https://web.archive.org/web/20191007225130im_/https://2.bp.blogspot.com/-iz0rO6Hcols/WosBFD23pnI/AAAAAAAABFc/V0xlNrJtGyc33utyDR3csDI7HIRFq9M2ACLcBGAs/s320/Screen%2BShot%2B2018-02-19%2Bat%2B17.53.39.png
   :width: 150px
   :height: 320px
   :target: https://2.bp.blogspot.com/-iz0rO6Hcols/WosBFD23pnI/AAAAAAAABFc/V0xlNrJtGyc33utyDR3csDI7HIRFq9M2ACLcBGAs/s1600/Screen%2BShot%2B2018-02-19%2Bat%2B17.53.39.png
.. |image2| image:: https://web.archive.org/web/20191007225130im_/https://2.bp.blogspot.com/-xo9yW8cGce0/Wpz9n2OQAxI/AAAAAAAABIA/nZz5eqLvScA6l_LAEU1tAgFjI8OE4KmigCLcBGAs/s320/Screen%2BShot%2B2018-03-05%2Bat%2B09.20.52.png
   :width: 320px
   :height: 84px
   :target: https://2.bp.blogspot.com/-xo9yW8cGce0/Wpz9n2OQAxI/AAAAAAAABIA/nZz5eqLvScA6l_LAEU1tAgFjI8OE4KmigCLcBGAs/s1600/Screen%2BShot%2B2018-03-05%2Bat%2B09.20.52.png
.. |image3| image:: https://web.archive.org/web/20191007225130im_/https://4.bp.blogspot.com/-JTUSwRkfQaw/Wp0NboqPpoI/AAAAAAAABIc/JgmiFP9JXHw7DZnm0YZyG85KpzuUaLxBQCLcBGAs/s320/Screen%2BShot%2B2018-03-05%2Bat%2B10.28.10.png
   :width: 320px
   :height: 196px
   :target: https://github.com/pygame/pygame/issues?q=is%3Aissue+is%3Aopen+label%3A%22Low+Hanging+Fruit%22
.. |image4| image:: https://1.bp.blogspot.com/-PBgTIGajntM/XcByoZiWrrI/AAAAAAAABgM/D6PlY5nVBjc1PCfsOxvncfnTnZf9A64LACLcBGAsYHQ/s400/Screen%2BShot%2B2019-11-04%2Bat%2B19.48.45.png
   :width: 400px
   :height: 277px
   :target: https://1.bp.blogspot.com/-PBgTIGajntM/XcByoZiWrrI/AAAAAAAABgM/D6PlY5nVBjc1PCfsOxvncfnTnZf9A64LACLcBGAsYHQ/s1600/Screen%2BShot%2B2019-11-04%2Bat%2B19.48.45.png
.. |image5| image:: https://1.bp.blogspot.com/-ud2zAwHygoo/XcBlS1SCUbI/AAAAAAAABfY/nQvFaKw6RIEHwswR0eskSd8oV2aYmXqOgCLcBGAsYHQ/s320/Screen%2BShot%2B2019-11-04%2Bat%2B18.51.37.png
   :width: 320px
   :height: 167px
   :target: https://1.bp.blogspot.com/-ud2zAwHygoo/XcBlS1SCUbI/AAAAAAAABfY/nQvFaKw6RIEHwswR0eskSd8oV2aYmXqOgCLcBGAsYHQ/s1600/Screen%2BShot%2B2019-11-04%2Bat%2B18.51.37.png
.. |image6| image:: https://1.bp.blogspot.com/-nGgcx-0GkTY/XcBwYZ-srgI/AAAAAAAABfw/dr7mbMqU8cMVkea7tJDV-SdbScUrGFjKwCLcBGAsYHQ/s1600/test_draw2_image.png
   :target: https://1.bp.blogspot.com/-nGgcx-0GkTY/XcBwYZ-srgI/AAAAAAAABfw/dr7mbMqU8cMVkea7tJDV-SdbScUrGFjKwCLcBGAsYHQ/s1600/test_draw2_image.png
