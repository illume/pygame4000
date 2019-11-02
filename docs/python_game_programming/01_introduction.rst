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

   An `open source <http://www.opensource.org/>`__ implementation is
   pretty important too. The executable to big? Remove parts of python.
   Recompile it in ways which make your particular game faster. Make all
   sorts of changes. You don't have too do these things. But if you need
   to, it's good to have the option.

Python, and python gaming websites.
-----------------------------------

-  There's a few websites you should explore, to gain true mastery of
   the python game programming way ;)

   -  http://www.python.org/

   -  http://www.pygame.org/

   Although we will be teaching python as we go, you may want to check
   out some other tutorials. If you don't know python allready, you
   should work through one of these other python tutorials over the next
   two weeks. If python is your first programming language, this is an
   excellent tutorial to follow:

   -  http://www.honors.montana.edu/%7Ejjc/easytut/easytut/

   This tutorial is a quick introduction, for those who want to dive
   right in.

   -  http://www.hetland.org/python/instant-hacking.php

   Here's a big list of tutorials at the main python website.

   -  http://www.python.org/doc/Newbies.html

   Some gaming websites you should check out include:

   -  http://gamedev.net/

   -  http://gamasutra.com/

   -  http://ludumdare.com/

   Of particular interest to new games programmers may be the `game
   dictionary <http://gamedev.net/dict/>`__. If you come accross any
   words you don't know there might be the best place to look first for
   an explanation.


Installing your python programming environment.
-----------------------------------------------

-  Time to get into the programming.

https://www.pygame.org/wiki/GettingStarted


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
      print dir(pygame)
      print dir()

   That should print a bunch of stuff. The import command tells python
   to load that module. The print command is used to print stuff. duh.
   The dir command is really cool. It shows you what stuff is inside the
   pygame module. Now type:

   ::

      help(pygame.Rect)

   That shows you documentation on a particular object/

   `function <http://www.honors.montana.edu/%7Ejjc/easytut/easytut/node9.html>`__/
   `variable <http://www.honors.montana.edu/%7Ejjc/easytut/easytut/node5.html#SECTION00510000000000000000>`__.
   Try out help on a few other things inside of the pygame module. eg
   help(pygame.sprite) Check out the documentation for python, and
   pygame at these places.

   -  Documentation for pygame: http://pygame.org/docs/index.html

   -  Documentation for python: http://python.org/docs/

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

