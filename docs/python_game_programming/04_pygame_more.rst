Python game programming part 4 - More pygame to make your brain hurt
====================================================================

From last weeks pygame we are now going to move on to a more featureful
demonstration. This lecture is based on the Chimp line by line tutorial
found at the pygame site. Thanks to Pete Shinners for letting us base
this lecture on his tutorial.

In the *pygame* examples there is a simple example named, "chimp". This
example simulates a punchable monkey moving around a small screen with
promises of riches and reward. The example itself is very simple, and a
bit thin on errorchecking code. This example program demonstrates many
of pygame's abilities, like creating a graphics window, loading images
and sound files, rendering TTF text, and basic event and mouse handling.

The program and images can be found inside the standard source
distribution of pygame. To find the examples use

::

  python -c "import pygame.examples;print(pygame.examples.__file__)"


Alternatively you can find the examples by typing this into the
interpreter REPL.

::

  >>> import pygame.examples
  >>> print(pygame.examples.__file__)


With your text editor open up chimp.py in that directory.

You should have been able to run chimp.py from the command line. If not,
go back to `Part 1 introduction <01_introduction>`__ and figure out how. As we go on
you'll be changing a few things in the chimp.py, so you may want to make
a backup copy.

This tutorial will go through the code block by block. Explaining how
the code works. There will also be mention of how the code could be
improved and what errorchecking could help out.

|chimpshot|


Import Modules
--------------

This is the code that imports all the needed modules into your program.
It also checks for the availability of some of the optional pygame
modules.
Modules <https://docs.python.org/3/tutorial/modules.html>`__
are a grouping of code, or a library.

::

   import os, sys
   import pygame
   from pygame.locals import *

   if not pygame.font: print('Warning, fonts disabled')
   if not pygame.mixer: print('Warning, sound disabled')

In the next line, we import the pygame package. When pygame is imported
it imports all the modules belonging to pygame. Some pygame modules are
optional, and if they aren't found, their value is set to "None". None
is like NULL in other programming languages.

There is a special *pygame* module named "locals". The members of this
module are commonly used constants and functions that have proven useful
to put into your program's global namespace. This locals module includes
functions like "Rect" to create a rectangle object, and many constants
like "QUIT, HWSURFACE" that are used to interact with the rest of
*pygame*. Importing the locals module into the global namespace like
this is entirely optional. If you choose not to import it, all the
members of locals are always available in the *pygame* module.

Lastly, we decide to print a nice warning message if the font or sound
modules in pygame are not available.


Loading Resources
-----------------

Now we are going to expand on what we did in the last lecture with
loading images. We are also going to be adding a sound loading function.

We're going to add some error checking, and set the color key for the
image. We put this code in a function so that we can reuse it to load
multiple images without having to type all the code in every time we
want to load an image.

This code is from chimp.py which should be open in your text editor.

::

   def load_image(name, colorkey=None):
       fullname = os.path.join('data', name)
       try:
           image = pygame.image.load(fullname)
       except pygame.error, message:
           print("Cannot load image:", name)
           raise SystemExit, message
       image = image.convert()
       if colorkey is not None:
           if colorkey is -1:
               colorkey = image.get_at((0,0))
           image.set_colorkey(colorkey, RLEACCEL)
       return image, image.get_rect()


Some new python concepts
~~~~~~~~~~~~~~~~~~~~~~~~

For those of you new to python, we are now going to describe some of the
concepts introduced here. Don't worry if you don't get them all, you'll
probably need to read this section a few times. I have made links to
websites that describe each of the concepts in more detail. You should
probably go and read those sections as well.

::

   def load_image(name, colorkey=None):
       fullname = os.path.join('data', name)

First two lines of the load_image
`function <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>`__/

def is used to tell python that you are starting a new function. A
function is a piece of code which does something. It means you don't
need to retype code all the time. Instead of typing all that stuff out
you can just call:

::

   im = load_image("chimp.bmp")

Further on in the code you see the try, and except being used. This is
for error handling. You try to load the image, and if there is an
unexpected error the code in the except block gets called. Read up more
about `errors and exceptions <https://docs.python.org/3/tutorial/errors.html>`__.


Loading images explained
~~~~~~~~~~~~~~~~~~~~~~~~

The load_image function takes the name of an image to load. It also
optionally takes an argument it can use to set a colorkey for the image.
A colorkey is used in graphics to represent a color of the image that is
transparent.

The first thing this function does is create a full pathname to the
file. In this example all the resources are in a "data" subdirectory. By
using the
`os.path.join <https://docs.python.org/3/library/os.path.html#os.path.join>`__
function, a pathname will be created that works for whatever platform
the game is running on.

Remember that we can look at the documentation for functions in the
interactive interpreter. In the interactive interpreter type:

::

   import os.path
   help(os.path.join)

Next we load the image using the
`pygame.image.load <https://www.pygame.org/docs/ref/image.html#pygame.image.load>`__
function. We wrap this function in a try/except block, so if there is a
problem loading the image, we can exit gracefully. After the image is
loaded, we make an important call to the convert() function. This makes
a new copy of a Surface and converts its color format and depth to match
the display. This means blitting the image to the screen will happen as
quickly as possible.

Images can be in many different color formats. For example RGB with 8
bits for red, green and blue. Or 8 bit indexed color, or RGBA
(Red,Green,Blue,Alpha). The more bits used for each pixel on an image,
the more colors it can show. For an explanation of surfaces check out
https://www.pygame.org/docs/ref/surface.html

Last, we set the colorkey for the image. If the user supplied an
argument for the colorkey argument we use that value as the colorkey for
the image. This would usually just be a color RGB value, like (255, 255,
255) for white. You can also pass a value of -1 as the colorkey. In this
case the function will lookup the color at the topleft pixel of the
image, and use that color for the colorkey.


Loading sound explained
~~~~~~~~~~~~~~~~~~~~~~~

::

   def load_sound(name):
       class NoneSound:
           def play(self): pass
       if not pygame.mixer:
           return NoneSound()
       fullname = os.path.join('data', name)
       try:
           sound = pygame.mixer.Sound(fullname)
       except pygame.error, message:
           print("Cannot load sound:", fullname)
           raise SystemExit, message
       return sound

Next is the function to load a sound file. The first thing this function
does is check to see if the
`pygame.mixer <https://www.pygame.org/docs/ref/mixer.html>`__ module
was imported correctly. If not, it returns a small class instance that
has a dummy play method. This will act enough like a normal
`Sound <https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound>`__ object for this game
to run without any extra error checking.

If you're wondering what a class is read up on them at these places:

-  https://python.org/doc/current/tut/node11.html,

-  https://diveintopython.org/fileinfo_divein.html,

-  http://ibiblio.org/obp/thinkCS/python/english/chap12.htm.

You will need to know about classes for the sections below, where we
make and describe the Fist, and Chimp classes.

This function is similar to the image loading function, but handles some
different problems. First we create a full path to the sound image, and
load the sound file inside a try/except block. Then we simply return the
loaded Sound object.

Pygame can load a number of different sound files.

-  .ogg files. A free high quality lossy sound format.
   http://www.vorbis.com/

-  .mp3 files. A popular lossy format. If you haven't heard of these,
   pull up a random teenager and ask them about it.
-  .wav files. Of various types. These are usually uncompressed sound
   formats.

It can also open up mod files, and midi files for music.


Game Object Classes
-------------------

Here we create two classes to represent the objects in our game. Almost
all the logic for the game goes into these two classes. We will look
over them one at a time here.

::

   class Fist(pygame.sprite.Sprite):
       """moves a clenched fist on the screen, following the mouse"""
       def __init__(self):
           pygame.sprite.Sprite.__init__(self) #call Sprite initializer
           self.image, self.rect = load_image(fist.bmp, -1)
           self.punching = 0

       def update(self):
           "move the fist based on the mouse position"
           pos = pygame.mouse.get_pos()
           self.rect.midtop = pos
           if self.punching:
               self.rect.move_ip(5, 10)

       def punch(self, target):
           "returns true if the fist collides with the target"
           if not self.punching:
               self.punching = 1
               hitbox = self.rect.inflate(-5, -5)
               return hitbox.colliderect(target.rect)

       def unpunch(self):
           "called to pull the fist back"
           self.punching = 0

The players fist is represented by the class above.

It is derived from the Sprite class included in the
`pygame.sprite <https://www.pygame.org/docs/ref/sprite.html>`__
module. The init function is called when new instances of this class are
created. The first thing we do is be sure to call the init function for
our base class. This allows the Sprite's init function to prepare our
object for use as a sprite. This game uses one of the sprite drawing
Group classes. These classes can draw sprites that have an "image" and
"rect" attribute. By simply changing these two attributes, the renderer
will draw the current image at the current position.

Unlike in the previous lecture where we *blit* the image directly to the
screen, here we put the images in sprite classes. This gives us some
advantages. Mainly the sprite classes are used for organising drawing of
images. We want to draw as little as possible, which the sprite classes
can do for us by keeping track of where the images we draw go. If you
want to know more about sprites read
https://www.pygame.org/docs/tut/SpriteIntro.html.

All sprites have an update() method. This function is typically called
once per frame. It is where you should put code that moves and updates
the variables for the sprite. The update() method for the fist moves the
fist to the location of the mouse pointer. It also offsets the fist
position slightly if the fist is in the "punching" state.

The punch() and unpunch() methods change the punching state for the
fist. The punch() method also returns a true value if the fist is
colliding with the given target sprite.


Don't be a square; detour into the world of Rect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ok a short detour from the Sprite classes to describe Rects.
`Rect <https://www.pygame.org/docs/ref/rect.html>`__ objects are simply
classes which represent a rectangle. However they are very featureful.

They are used throughout pygame to help you organise and optimize
drawing images. They can be used for collision detection and moving
images accross the screen. You can check to see if a point is within a
rectangle. There are many things you can do with them. Just check out
the documentation.

::

   my_rect = pygame.Rect(20, 25, 40, 50)

That makes a Rect object with its top corner at x= 20 y = 25. It has a
width of 40 pixels and a height of 50 pixels.

You can see that in the Fist.punch() method it uses a colliderect() call
to see if the target(usually the rect for our unfortunate chimp) has
collided with the fists rect attribute. It uses a slightly smaller rect
than the fists rect, so that it is slightly harder to punch the chimp.
It uses the
`Rect.inflate <https://www.pygame.org/docs/ref/rect.html#pygame.Rect.inflate>`__ method
to make a smaller rect.


Python note on docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~

In this class we see docstrings being used. Docstrings are documentation
or comments used to describe what functions do. Docstrings are not like
normal comments, in that they are used to generate online documentation.
When you do a:

::

   >>> def x():
   ...     """prints the letter x"""
   ...     print("x")
   ...
   >>> help(x)

   Help on function x in module __main__:

   x()
       prints the letter x
   >>> print(x.__doc__)
   prints the letter x
   >>>

In this function the """prints the letter x""" is a doc string. A doc
string is the line immediately after the start of a class or function
declaration.

You can also access the docstring through the doc attribute.


Back on to the Chimp sprite
---------------------------

Ok, now we are going to explain the Chimp class.

::

   class Chimp(pygame.sprite.Sprite):
       """moves a monkey critter across the screen. it can spin the
          monkey when it is punched."""
       def __init__(self):
           pygame.sprite.Sprite.__init__(self) #call Sprite intializer
           self.image, self.rect = load_image('chimp.bmp', -1)
           screen = pygame.display.get_surface()
           self.area = screen.get_rect()
           self.rect.topleft = 10, 10
           self.move = 9
           self.dizzy = 0

       def update(self):
           "walk or spin, depending on the monkeys state"
           if self.dizzy:
               self._spin()
           else:
               self._walk()

       def _walk(self):
           "move the monkey across the screen, and turn at the ends"
           newpos = self.rect.move((self.move, 0))
           if self.rect.left < self.area.left or \
               self.rect.right > self.area.right:
               self.move = -self.move
               newpos = self.rect.move((self.move, 0))
               self.image = pygame.transform.flip(self.image, 1, 0)
           self.rect = newpos

       def _spin(self):
           "spin the monkey image"
           center = self.rect.center
           self.dizzy = self.dizzy + 12
           if self.dizzy >= 360:
               self.dizzy = 0
               self.image = self.original
           else:
               rotate = pygame.transform.rotate
               self.image = rotate(self.original, self.dizzy)
           self.rect = self.image.get_rect()
           self.rect.center = center

       def punched(self):
           "this will cause the monkey to start spinning"
           if not self.dizzy:
               self.dizzy = 1
               self.original = self.image

The chimp class is doing a little more work than the fist, but nothing
more complex. This class will move the chimp back and forth across the
screen. When the monkey is punched, he will spin around to exciting
effect. This class is also derived from the base Sprite class, and is
initialized the same as the fist. While initializing, the class also
sets the attribute "area" to be the size of the display screen.

The update function for the chimp simply looks at the current "dizzy"
state, which is true when the monkey is spinning from a punch. It calls
either the \_spin or \_walk method. These functions are prefixed with an
underscore. This is just a standard python idiom which suggests these
methods should only be used by the Chimp class. We could go so far as to
give them a double underscore, which would tell python to really try to
make them private methods, but we don't need such protection. :)

The \_walk method creates a new position for the monkey by moving the
current rect by a given offset. If this new position crosses outside the
display area of the screen, it reverses the movement offset. It also
mirrors the image using the
`pygame.transform.flip <https://www.pygame.org/docs/ref/transform.html#pygame.transform.flip>`__
function. This is a crude effect that makes the monkey look like he's
turning the direction he is moving.

The \_spin method is called when the monkey is currently "dizzy". The
dizzy attribute is used to store the current amount of rotation. When
the monkey has rotated all the way around (360 degrees) it resets the
monkey image back to the original unrotated version. Before calling the
`transform.rotate <https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate>`__
function, you'll see the code makes a local reference to the function
simply named "rotate". There is no need to do that for this example, it
is just done here to keep the following line's length a little shorter.

Note that when calling the rotate function, we are always rotating from
the original monkey image. When rotating, there is a slight loss of
quality. Repeatedly rotating the same image and the quality would get
worse each time.

Also, when rotating an image, the size of the image will actually
change. This is because the corners of the image will be rotated out,
making the image bigger. We make sure the center of the new image
matches the center of the old image, so it rotates without moving.

The last method is punched() which tells the sprite to enter its dizzy
state. This will cause the image to start spinning. It also makes a copy
of the current image named "original".


Initialize Everything
---------------------

Before we can do much with pygame, we need to make sure its modules are
initialized. In this case we will also open a simple graphics window.
Now we are in the main() function of the program, which actually runs
everything.

::

   pygame.init()
   screen = pygame.display.set_mode((468, 60))
   pygame.display.set_caption(Monkey Fever)
   pygame.mouse.set_visible(0)

The first line to initialize *pygame* takes care of a bit of work for
us. It checks through the imported *pygame* modules and attempts to
initialize each one of them. It is possible to go back and check if
modules failed to initialize, but we won't bother here. It is also
possible to take a lot more control and initialize each specific module
by hand. That type of control is generally not needed, but is available
if you desire.

Next we set up the display graphics mode. Note that the pygame.display
module is used to control all the display settings. In this case we are
asking for a simple skinny window. There is an entire separate tutorial
on setting up the graphics mode, but if we really don't care, *pygame*
will do a good job of getting us something that works. Pygame will pick
the best color depth, since we haven't provided one.

Last we set the window title and turn off the mouse cursor for our
window. Very basic to do, and now we have a small black window ready to
do our bidding. Usually the cursor defaults to visible, so there is no
need to really set the state unless we want to hide it.


Create The Background
---------------------

Our program is going to have text message in the background. It would be
nice for us to create a single surface to represent the background and
repeatedly use that. The first step is to create the surface.

::

   background = pygame.Surface(screen.get_size())
   background = background.convert()
   background.fill((250, 250, 250))

This creates a new surface for us that is the same size as the display
window. Note the extra call to convert() after creating the Surface. The
convert with no arguments will make sure our background is the same
format as the display window, which will give us the fastest results.

We also fill the entire background with a solid white-ish color. Fill
takes an RGB triplet as the color argument.


Put Text On The Background, Centered
------------------------------------

Now that we have a background surface, lets get the text rendered to it.
We only do this if we see the pygame.font module has imported properly.
If not, we just skip this section.

::

   if pygame.font:
       font = pygame.font.Font(None, 36)
       text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
       textpos = text.get_rect()
       textpos.centerx = background.get_rect().centerx
       background.blit(text, textpos)

As you see, there are a couple steps to getting this done. First we must
create the font object and render it into a new surface. We then find
the center of that new surface and blit (paste) it onto the background.

The font is created with the font module's Font() constructor. Usually
you will pass the name of a truetype font file to this function, but we
can also pass None, which will use a default font. The Font constructor
also needs to know the size of font we want to create.

We then render that font into a new surface. The render function creates
a new surface that is the appropriate size for our text. In this case we
are also telling render to create antialiased text (for a nice smooth
look) and to use a dark grey color.

Next we need to find the centered position of the text on our display.
We create a "Rect" object from the text dimensions, which allows us to
easily assign it to the screen center.

Finally we blit (blit is like a copy or paste) the text onto the
background image.


Display The Background While Setup Finishes
-------------------------------------------

We still have a black window on the screen. Lets show our background
while we wait for the other resources to load.

::

   screen.blit(background, (0, 0))
   pygame.display.flip()

This will blit our entire background onto the display window. The blit
is self explanatory, but what about this flip routine?

In pygame, changes to the display surface are not immediately visible.
Normally, a display must be updated in areas that have changed for them
to be visible to the user. With double buffered displays the display
must be swapped (or flipped) for the changes to become visible. In this
case the flip() function works nicely because it simply handles the
entire window area and handles both singlebuffered and doublebufferes
surfaces.


Prepare Game Object
-------------------

Here we create all the objects that the game is going to need.

::

   whiff_sound = load_sound('whiff.wav')
   punch_sound = load_sound('punch.wav')
   chimp = Chimp()
   fist = Fist()
   allsprites = pygame.sprite.RenderPlain((fist, chimp))
   clock = pygame.time.Clock()

First we load two sound effects using the load_sound function we defined
above. Then we create an instance of each of our sprite classes. And
lastly we create a sprite Group which will contain all our sprites.

We actually use a special sprite group named
`RenderPlain <RenderPlain>`__. This sprite group can draw all the
sprites it contains to the screen. It is called
`RenderPlain <RenderPlain>`__ because there are actually more advanced
Render groups. But for our game, we just need simple drawing. We create
the group named "allsprites" by passing a list with all the sprites that
should belong in the group. We could later on add or remove sprites from
this group, but in this game we won't need to.

The clock object we create will be used to help control our game's
framerate. We will use it in the main loop of our game to make sure it
doesn't run too fast.


Main Loop
---------

Nothing much here, just an infinite loop.

::

   while 1:
       clock.tick(60)

All games run in some sort of loop. The usual order of things is to
check on the state of the computer and user input, move and update the
state of all the objects, and then draw them to the screen. You'll see
that this example is no different.

We also make a call to our clock object, which will make sure our game
doesn't run faster than 60 frames per second.


Handle All Input Events
-----------------------

This is an extremely simple case of working the event queue.

::

   for event in pygame.event.get():
       if event.type == QUIT:
           return
       elif event.type == KEYDOWN and event.key == K_ESCAPE:
           return
       elif event.type == MOUSEBUTTONDOWN:
           if fist.punch(chimp):
               punch_sound.play() #punch
               chimp.punched()
           else:
               whiff_sound.play() #miss
       elif event.type == MOUSEBUTTONUP:
           fist.unpunch()

First we get all the available Events from pygame and loop through each
of them. The first two tests see if the user has quit our game, or
pressed the escape key. In these cases we just return from the main()
function and the program cleanly ends.

Next we just check to see if the mouse button was pressed or released.
If the button was pressed, we ask the fist object if it has collided
with the chimp. We play the appropriate sound effect, and if the monkey
was hit, we tell him to start spinning (by calling his punched()
method).


Update the Sprites
------------------

::

   allsprites.update()

Sprite groups have an update() method, which simply calls the update
method for all the sprites it contains. Each of the objects will move
around, depending on which state they are in. This is where the chimp
will move one step side to side, or spin a little farther if he was
recently punched.


Draw The Entire Scene
---------------------

Now that all the objects are in the right place, time to draw them.

::

   screen.blit(background, (0, 0))
   allsprites.draw(screen)
   pygame.display.flip()

The first blit call will draw the background onto the entire screen.
This erases everything we saw from the previous frame (slightly
inefficient, but good enough for this game). Next we call the draw()
method of the sprite container. Since this sprite container is really an
instance of the "`DrawPlain <DrawPlain>`__" sprite group, it knows how
to draw our sprites. Lastly, we flip() the contents of pygame's software
double buffer to the screen. This makes everything we've drawn visible
all at once.


Game Over
---------

User has quit, time to clean up.

Cleaning up the running game in *pygame* is extremely simple. In fact
since all variables are automatically destructed, we really don't have
to do anything.


Assignment:
-----------

-  Using the scale command to make the monkey smaller. Getting too good
   at spanking the monkey? We want to give that monkey a chance. So
   after every five times the monkey is hit, we want to make the monkey
   a bit smaller.


Next
~~~~


`Part Five <_05_parts_of_a_game>`__


.. |chimpshot| image:: https://www.pygame.org/docs/_images/chimpshot.gif
