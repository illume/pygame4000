Python game programming part 1 - Introduction
=============================================


What are these articles going to teach you?
-------------------------------------------

-  How to make games with python. Libraries we are going to use include:

   - pygame,
   - numpy

   We're going to start with showing you how to set up your python
   environment. In lecture two we'll move on to showing you the basics
   of python and pygame. Afterwards we'll build up to making some 2d,
   and 3d games. Space travel, monkey bashing, ball and block
   positioning will also be covered.


Why python for games?
---------------------

-  Pythons benefits include clear syntax, fast development, available on
   multiple platforms, quality free implementations, and open source
   code. Clear syntax is useful so you can understand what things do, so
   you can change things quickly. Python allows doesn't require many of
   the things which other computer languages do. Eg you do not need to
   type ';' at the end of every line. You do not need brackets for many
   things. The authors of python try very hard to make sure that python
   code written remains clear and understandable. Fast development with
   python is achieved by a few things. No compile times, lower amounts
   of typing you need to do. You don't need a lengthy compile before you
   can see your changes. There are even ways where you can change the
   program whilst it is running! This allows you to tweak your game
   quicker than compiled languages will allow.

   An `open source <https://www.opensource.org/>`__ implementation is
   pretty important too. The executable to big? Remove parts of python.
   Recompile it in ways which make your particular game faster. Make all
   sorts of changes. You don't have too do these things. But if you need
   to, it's good to have the option.

Python, and python gaming websites.
-----------------------------------

-  There's a few websites you should explore, to gain true mastery of
   the python game programming way ;)

   -  https://www.python.org/

   -  https://www.pygame.org/

   Although we will be teaching python as we go, you may want to check
   out some other tutorials. If you don't know python allready, you
   should work through one of these other python tutorials over the next
   two weeks. If python is your first programming language, this is an
   excellent tutorial to follow:

   -  https://docs.python.org/3/tutorial/

   Some gaming websites you should check out include:

   -  https://gamedev.net/

   -  https://gamasutra.com/

   -  https://ldjam.com/

   Of particular interest to new games programmers may be the `Glossary of video
   game terms <https://en.wikipedia.org/wiki/Glossary_of_video_game_terms>`__.
   If you come accross any words you don't know there might be the best place
   to look first for an explanation.


Installing your python programming environment.
-----------------------------------------------

-  Time to get into the programming.

https://www.pygame.org/wiki/GettingStarted

Many programming books and tutorials have an installation section.
Which are almost immediately out of date, and are sometimes not tested.

So the GettingStarted page was started where things are up to date.
pygame is backwards compatible. Code written 20 years ago works today.


Don't worry, relax, and check out https://www.pygame.org/wiki/GettingStarted


Test your python installation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Run python. In windows, go to the start bar find python, and select
   the IDLE(Python GUI) option. In linux, type python at the command
   line.

   Now you should see a prompt like >>> This is the interactive
   interpreter, you'll be able to type into here python code, and see it
   run. Fun. Now type in:

   ::

      import pygame
      print(dir(pygame))
      print(dir())

   That should print a bunch of stuff. The import command tells python
   to load that module. The print command is used to print stuff. duh.
   The dir command is really cool. It shows you what stuff is inside the
   pygame module. Now type:

   ::

      help(pygame.Rect)

   That shows you documentation on a particular object/

   `function <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>`__/
   `variable <https://docs.python.org/3/tutorial/introduction.html>`__.
   Try out help on a few other things inside of the pygame module. eg
   help(pygame.sprite) Check out the documentation for python, and
   pygame at these places.

   -  Documentation for pygame: https://pygame.org/docs/index.html

   -  Documentation for python: https://python.org/docs/

   It's good to know where to look for info when you get stuck, or need
   to know more details.


Running the chimp
-----------------

-  From the command prompt:

   ::

      python -m pygame.examples.chimp

   Now try running some of the other examples.

   ::

      python -m pygame.examples


Next after article introduction
-------------------------------

`Part Two <_02_python_intro>`__

