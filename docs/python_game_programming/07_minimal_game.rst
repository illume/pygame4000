Python game programming part 7 - Make a game
============================================

This lecture we are going to run through making a game. Or what some
people would call a prototype of a game.

It will be kind of like that old table top game starving starving
rhinoceros(or something like that). Where lots of balls roll around, and
you have to get your rhinoceros to eat them up.

The person who eats the most balls wins.

It is a simple game, but one with a smaller enough scope that we can
finish it fairly quickly. Which are my favourite types of games to
finish.

It could also be expanded later with more features if we want to.


A slightly detailed game design.
--------------------------------

First thing we do is think about what features will be in the first
version of our game. To finish the game quickly we want to make the
design as simple as possible.

Why do we want to finish the game quickly? Evaluating the game quicker.
If the game play isn't fun, then we want to know about it as soon as
possible to fix it. Or we may even decide that the game is not possible
to fix, and stop making it all together, and try out some other ideas.

So we want to limit the features to the minimal ones which are required
to make the game work.


Limited game play features
~~~~~~~~~~~~~~~~~~~~~~~~~~

There will be two rhinos which eat up the balls. We may want to add more
rhinos later, but two will be the minimum number.

The rhinos will be facing in one direction. Maybe in a later version we
will allow the rhinos to move. But for now each of them will be in the
middle of the game play area, and facing opposite from each other.

Two player game to start with. As coding a fun AI can be a lot of work,
we will save that for another version. Two player games are much easier
to do than single player games most of the time. By two player we mean
two players playing on the same computer, not network play. So one
player will use the mouse, and another the keyboard. Or maybe both will
use the keyboard.

Balls will bounce off the walls. So we will need to figure out how to
see if a ball hits the wall, and how to make it bounce back.

Balls will also need to move around. To start with we will not take into
account acceleration. All balls will move at the same speed.

Show the score for each of the rhinos. In the top left corner, and top
right corner the score will be shown. The top left will be for the rhino
on the left, the top right will be for the rhino on the right.

Opening and closing the rhinos mouth. When the balls come towards the
players rhino, and the mouth is closed the balls will bounce off. If the
mouth is open the balls will go inside the mouth. But the rhino will
have to close the mouth to swallow the balls.


Game play uncertainty.
~~~~~~~~~~~~~~~~~~~~~~

At this stage we have a small design of our game. But a few things are
uncertain. The main one is, will this be fun?

The part which I am uncertain about is how the mouth closing, and
opening to eat the balls is going to be fun. Maybe we will need to make
the balls hit the back of its mouth, and bounce back? How hard should it
be to eat the balls?

Another uncertainy I have is about how the balls will bounce around. I
can possibly imagine that the balls could bounce around in such a way
that they never go near the players rhinos mouths. Perhaps we will have
to add a game play element that makes the balls go towards the players
mouth.

These are just two uncertainties I have. You may have different ones, or
see how these problems could easily be solved by changing the design.
However both of these uncertainties will become clear as we start to
develop the game, and when we finish what we have set out to do. Once
the game is done, we may find that neither are problems, and that the
game is fun! Yah! However we may find that they need fixing. Another
more likely possibility is that there will be other problems.

So we make a minimal design, begin implementing that, and then improve
the design as we go.


Graphical design
~~~~~~~~~~~~~~~~

When we consider graphical design for a game, it is often best to start
with place holder graphics. This allows us to quickly test out the game
play ideas.

It is also a good idea to draw basically what your game will look like.
Stick figures, and boxes are usually enough.

Here are some other factors you may want to take into account when
making your graphics.

-  The graphical routines you have at your disposal. Do we have a 2d
   engine, a 3d engine?
-  The skills you have. 2d graphics, drawing, 3d modeling, animation.
-  What the game play requires.
-  Time you have. 2d graphics are generally quicker to do than 3d
   graphics.
-  Your audience. What type of computer do they have?

For our game I don't want to do really advanced graphics to start with.
I want to get it done quickly, so I'll choose to use 2d graphics. I also
don't want to use any external images to start with, so I will use the
pygame.draw graphics routines. These allow you to draw lines, circles,
rectangles, and flat polygons.

Not using any external files will mean that I will be able to make the
game work with one python script.

Once the game is complete, if I wish to continue with it, I could
improve the graphics.


Drawing the game design
'''''''''''''''''''''''

|starving_rhino_game_concept|

As you can see I spent maybe two minutes on this drawing.

You can draw it on paper, or on the computer. Just a rough draft is
neccessary for the game design. You may want to spend more time on it
drawing up different rhinos at different sizes, and different frames of
their animation.

As we are not going to do much graphics to start with, just concentrate
on getting the shapes and sizes of things correct.


Sound design
------------

No sounds to start with. Later I may want all manner of sounds. But as
the game design so far does not concerntrate on sounds as game play, I
will not use any sounds.

If I were to do sounds, some could be:

-  ball rolling. Get a marble and roll it along a desk.
-  ball hitting the wall. Roll a marble into something.
-  Rhino noises. Hrmmm, these would be harder to make. Be creative!


User input design
-----------------

Some people say the user interface to your game is the most important
part. There are a few reasons they say this. One is that if the player
can't figure out the controls, they will not play. Also it is what the
player will be doing.

For our game it will only require one input. That is all the player can
do is to say open mouth, or close mouth. That's it! Simple eh? Maybe too
simple. But it will do for now.

There are lots of things we could add later, but opening, and closing
the mouth of the rhino is the main interaction the player will have. So
we want this main interaction to also be the easiest to find out how to
do.

Clicking the mouse button, and pressing any key will be the way to
control our game. Player one will control the first rhino(one on left)
with the mouse click. Player two will control its rhino with pressing a
key on the keyboard.

The user input to the game may also change as we make the game. So as
you make a game, occasionally evaluate how your controls will work.
Especially after adding lots more user interaction.


Other input devices
~~~~~~~~~~~~~~~~~~~

We will not put into our game support for any more types of input. But
many of them could be added later quite easily. However then we would
need to detect or allow the player to chose which input they are using.

We could make our game see if the player is pressing on a joystick and
make the joystick controll player two. Or perhaps make it control player
one. In that way we could avoid making the player manually choose which
input they want to use. It will just use which ever input they bash on
:)


timing and user input.
~~~~~~~~~~~~~~~~~~~~~~

We may want to limit how fast a person can do things. In our game we
will probably want to limit how quickly the player can open and close
the mouth of the rhino.

The game could be quite different if we make it so that you can only
open and close the mouth every two seconds. Compared to if you could
open and close the mouth as quickly as you could click.


Other things player can do.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two other things most games have are:

-  exiting/quiting the game.
-  pausing the game.


User input for quiting
~~~~~~~~~~~~~~~~~~~~~~

There are some conventions in games for quiting. One is the 'q' key.
Another is the ESC key. Often the esc or q keys take the player to the
main menu. As we will not have a main menu those keys will just quit the
game. Another convention is to use ALT+F4. But that is not

Quiting with the mouse is another thing we may want to add. Maybe a big
quit button somewhere on the screen. In the first version we won't
implement it, as it is too much work to test out the game play. Later
though it may be important. One problem with that is that the player may
accidentally press it. If we make our game go in windowed mode, the
player can quit with the mouse by using the quit button on the window.


User input for pausing.
~~~~~~~~~~~~~~~~~~~~~~~

It is generally a good idea to build pausing into the game as early as
possible. As it can be a pain to add in later.

The convention for pausing a game is usually the 'p' key. Also some
games pause the game when you press ESC, whilst they show a menu.


Code design
-----------

First we need to decide what our audience is. From that we decide which
programming language, methods, and libraries to use.

In this case the audience is those people reading a python for
programming set of lectures/articles. So our language, and library
choice is python, and pygame.

As we want the game to be easy to run for you, I've decided to make the
game in one file. So all our graphics will be done with code, and there
will be no sound files with the game.

Because we want to finish the game quickly we choose to do a 2d game.

Our game design will probably not require any super speed code.

The only performance problems I could see us having is with lots of
balls moving around the screen. If we use the pygame.sprite classes this
shouldn't be a problem. Also the sprite classes will help us organise
the different visual elements of our game.

Different visual elements in the game:

-  Score. In the corners of the screen. Will change the number when the
   rhino scores.
-  Rhinos. Two of them in the middle of the screen. These will be
   animated.
-  Balls. There will be many of them. They are allways moving, except
   when eaten.

A slightly hard bit of code identified earlier in game play uncertainty,
is the ball bouncing code. Luckily there have been lots of games done
about balls bouncing around so the techniques to do so are described in
lots of websites. If we have a problem coding it, with a little research
we should find the answer.

If the game starts to run a little slowly when we have lots of balls, we
could just reduce the number of balls moving around.

Also for a bit of variation, we may want to give the players the option
of changing the amount of balls in play. Allthough we won't give them
the option in the first version of the game.


Coding the game
---------------

Now we dive into the coding of the game. I like to do it in small steps.
First get the screen up. Then draw the basic elements to the screen.
Then maybe add in some keyboard handling, and some mouse handling. Below
I describe the process I take making the game.


Getting something on screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~

I'll make some basic code to get a few things on screen first.

So I initialize things, make a main loop, and put in the event handling
for quiting.

::

   import pygame
   from pygame.locals import *


   pygame.init()

   display_flags = DOUBLEBUF
   width, height = 640, 480

   if pygame.display.mode_ok((width, height), display_flags ):
       screen = pygame.display.set_mode((width, height), display_flags)


   run = 1

   clock = pygame.time.Clock()

   while run:

       events = pygame.event.get()

       for event in events:

           if event.type == QUIT or (event.type == KEYDOWN and
                                     event.key in [K_ESCAPE, K_q]):
               # set run to 0 makes the game quit.
               run = 0

       # add the game play in here later.

       pygame.display.flip()

       # limit the game to about 40fps, or 40 ticks per second.
       clock.tick(40)

Ok. So now I have a black screen showing in a window, which I can quit
from. I limited the frame rate to 40 frames per second so when I do
animation, it is smoother. For smooth animation you need as constant a
frame rate as possible. Which is one of the reasons why tv, and film run
at 24 or 30 frames per second. There is more to it than this. If you
want to know more there is a good discussion on the topic at
http://ludumdare.com/forums/viewtopic.php?topic=141&forum=2&22


Drawing the balls
~~~~~~~~~~~~~~~~~

For the balls I am simply going to use the pygame.draw.circle function.
To draw a filled in circle.

We need two different colored circles, so this little function will draw
them to two surfaces for us.

::

   import pygame
   from pygame.locals import *


   def render_ball_simple(radius, color):
       """ Returns (surf,rect) containing a picture of
            a circle of the radius, and color given.
       """
       size = radius * 2
       surf = pygame.Surface((size, size))
       pygame.draw.circle(surf, color, (radius, radius), radius)
       return surf, surf.get_rect()

   def max(x, y):
       """ returns x, unless x > y.  if it is it returns y.
       """
       if x > y:
           return y
       else:
           return x


   def render_ball_funky(radius, color):
       """ Returns (surf,rect) containing a picture of
            a slightly shaded ball of the radius, and color given.
       """

       size = radius * 2
       surf = pygame.Surface((size, size))

       # we progressively draw smaller circles of different colors.
       increment = int(radius / 4)
       for x in range(4):
           iradius = radius - (x * increment)
           print(iradius)
           isize = iradius * 2
           icolor = [0, 0, 0]

           # we increment the color.  if it is bigger than 255 we make it 255.
           icolor[0] = max(color[0] + (x * 15), 255)
           icolor[1] = max(color[1] + (x * 15), 255)
           icolor[2] = max(color[2] + (x * 15), 255)

           pygame.draw.circle(surf, icolor, (radius, radius), iradius)



       return surf, surf.get_rect()

   def render_ball(radius, color):
       """ Returns (surf,rect) containing a picture of
            a ball of the radius, and color given.
       """
       # we use the kind of funk one...
       return render_ball_funky(radius, color)



   def main():


       pygame.init()

       display_flags = DOUBLEBUF
       width, height = 640, 480

       if pygame.display.mode_ok((width, height), display_flags ):
           screen = pygame.display.set_mode((width, height), display_flags)


       run = 1

       clock = pygame.time.Clock()

       # draw some graphics to surfaces.
       ball1,ball1_rect = render_ball_funky(10, (50, 200, 200))
       ball2,ball2_rect = render_ball_simple(6, (50, 200, 200))

       # move the simple one towards the center top of the screen.
       ball2_rect.x = 200


       while run:

           events = pygame.event.get()

           for event in events:

               if event.type == QUIT or (event.type == KEYDOWN and
                                         event.key in [K_ESCAPE, K_q]):
                   # set run to 0 makes the game quit.
                   run = 0

           # add the game play in here later.
           screen.blit(ball1, ball1_rect)
           screen.blit(ball2, ball2_rect)


           pygame.display.flip()

           # limit the game to about 40fps, or 40 ticks per second.
           clock.tick(40)


   # this runs the main function if this script is called to run.
   #  If it is imported as a module, we don't run the main function.
   if __name__ == "__main__":
       main()

In this code you can see that I have drawn two ball looking things to
the screen. Circles really. I got carried away with the draw ball
function, and made a render_ball_funky(). It draws four circles
progressively lighter to give a really simple shading effect. This is
what we call feature creep. I just did it for fun.

Feature creep gets in the way of you finishing the game. So avoid it! ;)

I have also moved the mainloop and the initialisation code inside a main
function. This is just to make it a bit neater.

Inside the main loop(the while loop), I do two blits. One for each of
the balls. The one in the center top of the screen is the simple circle,
the one on the left top is the so called funky ball. If you recall a
blit means to draw, or to copy an image. In this case we are blitting
directly to the screen.

The max function we define makes sure that the color values don't get
above 255. It is what some people call a helper function. That is a
small function made to make your code a bit nicer looking.

You should try and run this code as it gets developed. Add in some print
functions, and play around with it, so you can get the flow of how it is
working.

.. |starving_rhino_game_concept| image:: http://py3d.org/collab/images/starving_rhino_game_concept.png

