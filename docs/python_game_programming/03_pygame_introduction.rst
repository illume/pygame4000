Python game programming part 3 - Introduction to pygame
=======================================================


Now onto the flashy graphics!

We're going to show you pygame now. Going line by line through a simple
example which puts a monkey head onto a window.

If you want to see the full code listing skip to the bottom of the
lecture. For now we'll start exploring the first few lines.


Import Modules
--------------

Below is the code that imports all the needed modules into your program.
`Modules <https://docs.python.org/3/tutorial/modules.html>`__
are a grouping of code, or a library.

Open a command prompt and go into the pygame examples directory. Then
run python.

::

   >>> import pygame, sys,os
   >>> from pygame.locals import *

Try typing that into your interpreter like this: |import_stuff|

You can look up the documentation for these modules:
`pygame <https://pygame.org/docs/ref/pygame.html>`__,
`os <https://docs.python.org/3/library/os.html>`__,
`sys <https://docs.python.org/3/library/sys.html>`__.

You may also want to try using dir() and help() functions on those
modules :)

::

   >>> dir(pygame)


Initializing pygame
-------------------

Now we initialize all imported pygame modules. This is done with the
`pygame.init() <https://www.pygame.org/docs/ref/pygame.html#pygame.init>`__
function.

::

   >>> pygame.init()
   (6,0)

We've now initialized the video, the sound, and a number of other pygame
modules. If you type it into the interpreter you'll see that 6 modules
have initialized correctly, and none have failed.


Setting up the screen
---------------------

First we are making a window 468 pixels wide, and 60 pixels high. A
wide, short window.

::

   window = pygame.display.set_mode((468, 60))

Check out the documentation for
`pygame.display.set_mode <https://pygame.org/docs/ref/display.html#pygame.display.set_mode>`__,

Now we set a caption on the window. The caption is the text in the
middle of the window bar. Set the text to what ever you like! Change
'Monkey Fever' to 'I am the best python coder in the room!'.

::

   pygame.display.set_caption('Monkey Fever')

Check out the documentation for
`pygame.display.set_caption <https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption>`__,

Finally we get the display surface representing a screen.

::

   screen = pygame.display.get_surface()

A surface represents either the screen or an area in memory where images
are held.

Check out the documentation for
`pygame.Surface <https://pygame.org/docs/ref/surface.html>`__,


Constructing the monkey filename
--------------------------------

::

   >>> monkey_head_file_name = os.path.join("data","chimp.bmp")
   >>> print(monkey_head_file_name)
   data\chimp.bmp

This creates a relative pathname to the file. In this example all the
resources are in a "data" subdirectory of the pygame examples directory.
By using the
`os.path.join <http://python.org/doc/current/lib/module-os.path.html>`__
function, a pathname will be created that works for whatever platform
the game is running on.


To open the pygame documentation you can run this command.

::

   python -m pygame.docs


To find the folder where the examples are type this command into the
interpreter.

::

  >>> import pygame.examples
  >>> print(pygame.examples.__file__)


The relative path "data\chimp.bmp" is relative to the examples
directory. The full path name would be

::

   "C:\\Program Files\Pygame-Docs\examples\data\chimp.bmp"

On debian linux the pygame examples directory is in
/usr/share/doc/python3.7-pygame/examples/ The relative path
"data/chimp.bmp" is relative to that examples directory. The full path
name would be

::

   "/usr/share/doc/python3.7-pygame/examples/data/chimp.bmp"

Hopefully you can see that *os.path.join()* is one of the python
functions which helps you write code which will run on multiple
platforms. The same code should run on windows, linux boxes, macs, and
other types of machines.




Loading the monkey head image
-----------------------------

Now we get to load the monkey head image.

::

   >>> monkey_surface = pygame.image.load(monkey_head_file_name)

simple eh?

Have a look at the documentation for the
`pygame.image.load <https://pygame.org/docs/ref/image.html#pygame.image.load>`__
function.


Drawing the monkey onto the screen.
-----------------------------------

::

   screen.blit(monkey_surface, (0,0))

Here we come accross the blit function. *blit* is just another word for
draw.

What we are doing on this line is drawing the image of the monkey, which
is contained in the monkey_surface variable, onto the screen.

The second argument to the function is telling *blit* to draw the monkey
at coordinates (0,0). The top left of the screen.

Pygame uses a coordinate system for the screen where x= 0, y=0 is the
top left of the screen. (0,20) is twenty pixels below the top of the
screen.


Fliping the display
-------------------

::

   pygame.display.flip()

Here is where we flip the display surface. This updates the whole
screen.

There are more complicated things which you can do with updating the
display, which we will explain in the upcomming lectures. If you want to
learn more about updating the display you can find out here -
https://www.pygame.org/docs/ref/display.html#pygame.display.flip

Why do you have to flip the display? To see your graphics drawn.
Flipping the display is your way of telling pygame that you have
finished making changes for that frame, now please show the changes.

For now just be content that you should flip the display after having
drawn to it.


Adding a way to quit.
---------------------

::

   def input(events):
      for event in events:
         if event.type == QUIT:
            sys.exit(0)
         else:
            print(event)

We are defining a function with this code. This function does two
things:

-  looks for a quit event.
-  prints other events.

An event is:

-  Something that takes place; an occurrence.
-  A significant occurrence or happening.
-  A social gathering or activity.

Our game isn't likely to get an invitation down to the pub, or the park,
but it may be told that the mouse has moved, that certain keys have been
pressed or the joystick has been moved.

These are the types of events that happen within our program.

The input() function above loops over the input sequence *events*, and
does a test on each event.

Once a quit event happens the program exits. A quit event can happen by
clicking on the close window, or pressing ALT+F4.

If it is not a quit event it prints the event to the console(command
line window).


The main loop
-------------

::

   while True:
      input(pygame.event.get())

Here we have an infinite loop. While True is true it will keep looping.
As true is going to stay true for a long time, it will keep going
on(probably until the program exits).

`pygame.event.get <https://www.pygame.org/docs/ref/event.html#pygame.event.get>`__
is used to see what is happening in the program. It returns a list of
events. We pass this list to the input function we defined above.


All the code together.
----------------------

Below we have all the code together. Copy this into your text editor and
save it in the Pygame-Docs\examples directory as monkey_fever.py

Then run it, and see all the events fly by on the console!

::

   import pygame, sys,os
   from pygame.locals import *

   pygame.init()

   window = pygame.display.set_mode((468, 60))
   pygame.display.set_caption('Monkey Fever')
   screen = pygame.display.get_surface()

   monkey_head_file_name = os.path.join("data","chimp.bmp")

   monkey_surface = pygame.image.load(monkey_head_file_name)

   screen.blit(monkey_surface, (0,0))
   pygame.display.flip()

   def input(events):
      for event in events:
         if event.type == QUIT:
            sys.exit(0)
         else:
            print(event)

   while True:
      input(pygame.event.get())

|monkey_fever|

As you can see the monkey looks a bit strange. It's got red in the
background. The red color is what is called a color key. That is a color
in the image which represents transparency. So instead of showing red it
should show nothing, and let the black background be seen.

Now try pressing a few keys. You will notice the events being printed
out to the console. If you press a mouse button you will get events for
that. If you move the mouse you will get events.

Read the pygame docs for events, they are quite good -
https://www.pygame.org/docs/ref/event.html


Also try out this example

::

    python -m pygame.examples.eventlist


Exercises
---------


Move the head
~~~~~~~~~~~~~

-  Make the monkeys head be drawn 35 pixels to the right. Then make it
   drawn 40 pixels from the top of the window.


Quit on any key pressed
~~~~~~~~~~~~~~~~~~~~~~~

-  Find out how to make the program quit when you press any key. Once
   you find out, make your program quit when any key is pressed.


Find the size of the monkey surface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



-  Print to the console the size of the monkey surface.


Move the head when pressing a key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  When pressing the 's' key make the monkey move to x = 0 and y =0.
   Make it move to x = 35 y = 40 when the 'd' key is pressed.


Read pygame examples
~~~~~~~~~~~~~~~~~~~~

-  Read through some of the pygame examples. Run them see what they do.
   You probably won't understand them all, but you will likely get a
   feel for some other pygame code. For those new to python you should
   also have a read through some of the python tutorials:

   -  https://docs.python.org/3/tutorial/

   -  https://python.org/doc/Intros.html


Next
~~~~

In the next article I will be showing you:

-  how to load and play sounds,
-  some more advanced stuff with updating the display,
-  how to load color keys in images properly.
-  an introduction to the pygame sprite class.

Until next time. Have fun!

`Part Four <_04_pygame_more>`__
