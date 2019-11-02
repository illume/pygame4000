Python game programming part 5 - Parts of a game
================================================

Forgetting the details: Wrapping away implementation details.
-------------------------------------------------------------

Whenever I approach a library I am usually less interesting in the
library than what I can do with it. Because of this, I don't really care
how the library works and what the details are. At a later date, it may
become important to do some special stuff, but initially I just need it
it work and most of the time this is sufficient.

When approaching game libraries, such as `PyGame <PyGame>`__, you
essentially only care about 4 things:


Interfacing with the OS
-----------------------

Interfacing with the OS usually consists of creating a window, setting
it's properties (is it fullscreen, resizable, have a special icon, have
a name) and sometimes things like getting the system time or disk access
for cross platform libraries. Because Python is already cross platform,
we will only need Pygame to handle creating our Window and setting it
up.

Let's look at `PygameWindow <PygameWindow>`__ for how to do this.


Loading & Drawing graphics
--------------------------

Loading and drawing graphics is the main purpose of any game library.
Some game libraries do not really do much else than this, since they
expect you can fall back on simple system libraries to handle other
aspects. Pygame is built on SDL which handles all aspects of interfacing
with your OS and handling input, sound and graphics.

When designing your graphics wrapper, you will want to think about what
features you need to be aware of. For a 2D game, as we will be
designing, you should know how you will want to organize your background
drawing (square tiled, isometric), how you want to layer your characters
(can they overlap? how?), and anything special such as a side-scrolling
game will have various layers of graphics.

For a simple but flexible wrapper, let's look at
`PygameGraphics <PygameGraphics>`__ to do this.

Drawing text with fonts is definitely considered in the realm of
graphics, but I believe it requires enough specialized code to handle
different conditions that it is worth creating a separate wrapper. Check
out `PygameFont <PygameFont>`__ for the wrapper.


Loading & Playing sound
-----------------------

Sound programming is usually a bit easier, as while doing complex things
can be very involved, you can have a good sounding game with some very
simple code.


Reading from Input devices
--------------------------

You can't have interactivity without reading input, and games are
defined by their interactivity. I believe processing input is a layered
task, and at the bottom layer you will need to poll the system devices
to find out what your player is telling you.

`PygameInput <PygameInput>`__ will handle thing functionality, and will
let you see an overview of what your player is currently communicating
to your game.



Next
~~~~

`Part Six <_06_abstraction>`__
