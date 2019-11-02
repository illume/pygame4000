How to port and market games using #python and #pygame.
=======================================================

You've spent two years making a game, but now want other people to see
it?

How do you port it to different platforms, and make it available to
others? How do you let people know it is even a thing? Is your game Free
Libre software, or shareware?

All python related applications are welcome on
`www.pygame.org <https://www.pygame.org/>`__. You'll need a screenshot,
a description of your game, and some sort of URL to link people to (a
github/gitlab/bitbucket perhaps).  But how and where else can you share
it?

a few platforms to port to
--------------------------

-  itch.io and windows
-  windows store?
-  mac (for itch.io)
-  mac store
-  steam
-  linux 'flatpack' (latest fedora/ubuntu etc use this like an app
   store).
-  pypi (python packages can actually be installed by lots of people)
-  android store
-  web
-  debian
-  redhat/fedora

Make it a python package
------------------------

| Some of the tools work more easily with your package as a python
  package. Working with all the different tools is sort of hard, and
  having a convention for packaging would make things easier.
| Python packaging guide - http://packaging.python.org/
| So, why don't we do things as a simple python package with one example
  app to do this? pygame has an example app already, solarwolf -
  https://github.com/pygame/solarwolf. With work, it could be a good
  example app to use. We can also link in this guide to other pygame
  apps that have been distributed on various places.
| There are other example apps linked below for different distribution
  technology.
|  


Where to put your files?
~~~~~~~~~~~~~~~~~~~~~~~~

The `stuntcat community game <https://github.com/pygame/stuntcat/>`_ is setup as
an example of how you can package your game.

It's not the only way to structure your files,
but there are some advantages to doing it this way.

- Follows the python packaging guidelines. It's just a python package.
- Uses free Appveyor and TravisCI accounts to make Windows, Mac, and Linux binaries.
- Is set up to run tests when you push to github.
- Makes a windows, mac, linux, and python package.
- Uses different python packages like pymunk, thorpy, pyscroll.
- It will be kept working, and ported to more and more platforms as time goes on.

So if you're looking for inspiration on how to structure your files, it's a good place to look.


pyinstaller
~~~~~~~~~~~

| https://www.pyinstaller.org/
| This can make ones for linux, windows, and mac.

   ::

      pyinstaller --onefile --windowed --icon=icon.ico .py

Windows
-------

| pynsist and pyinstaller can be used.
| https://github.com/takluyver/pynsist
| The benefit of pynsist is that it can create installers. Whereas
  pyinstaller is for making standalone executables (which is good if you
  are putting your app on the Steam store for example).

Windows code signing
~~~~~~~~~~~~~~~~~~~~

-  https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Win-Code-Signing
-  https://docs.microsoft.com/en-us/windows/uwp/packaging/create-certificate-package-signing

Flatpak
-------

| apps on linux - https://flatpak.org/
| Here's an example of making a pygame one.
  https://github.com/flathub/flathub/pull/478
| Developer guide for more detail here -
  http://docs.flatpak.org/en/latest/

pypi
----

| The python package system can mean your app can be available for
  everyone who can use pip. Which is an audience in the millions.

Mac
---

| pyinstaller is probably the best option at the moment. If your game is
  open source, then you could use TravisCI for free to make builds with
  pyinstaller.
| Unfortunately you probably need a Mac to make a mac build, test it,
  and release on the mac/ios stores. Getting a cheap apple machine off
  ebay might be the way to go. Or a cloud account perhaps from
  'macincloud'. Also the mac developer program costs $100.
| Another option might be to borrow a friends machine to make the builds
  when it's time.
| See:

-  https://github.com/pyinstaller/pyinstaller/wiki/Recipe-OSX-Code-Signing
-  https://developer.apple.com/macos/distribution/
-  https://developer.apple.com/support/code-signing/

iOS
---

| It's not easy, but possible.
| With pygame 2 this should be possible since it uses the new SDL2.
| If you use LGPL code on iOS you still have to let your users benefit
  from the protections the LGPL gives them.
| Tom from renpy says... "I've been distributing Ren'Py under LGPL
  section 6c, which says that you can distribute it along with a written
  offer to provide the source code required to create the executables.
  Since Ren'Py has a reasonably strong distinction between the engine
  and game scripts, the user can then combine the game data from an iOS
  backup with the newly-linked Ren'Py to get a package they can install
  through xcode."
  https://github.com/renpy/pygame_sdl2/issues/109#issuecomment-412156973
| An apple developer account costs $100, and selling things costs 30% of
  the cost of your app. https://developer.apple.com/

Steam
-----

| There's a few games released using pygame on steam. Here are two
  threads of games released:

-  https://www.reddit.com/r/pygame/comments/87q9fr/i_just_published_my_game_the_four_colour_theorem/
-  https://www.reddit.com/r/pygame/comments/4ck5zv/released_a_pygame_game_on_steam_after_3_years_of/
-  https://www.reddit.com/r/pygame/comments/3j6zvr/with_help_from_you_guys_my_first_game_launched_on/

| Costs $100 to join up and sell a game on this store.
  https://partner.steamgames.com/
| Recently someone used pyinstaller to package thier game.

   ::

      pyinstaller --onefile --windowed --icon=icon.ico .py

SteamworksPy
~~~~~~~~~~~~

| A python module for the C++ steam sdk.
  https://github.com/Gramps/SteamworksPy
| Made by someone who has released their game (using pygame) on steam.


Itch.io
-------

| "itch.io is an open marketplace for independent digital creators with
  a focus on independent video games."

-  creators FAQ - https://itch.io/docs/creators/faq

| Quite a few people have released their pygame games on itch.io.

Android
-------

| This isn't really possible to do well at the moment without a bit of
  work.
| python-for-android seems the best option, but doesn't work well with
  pygame. https://github.com/kivy/python-for-android There is an old and
  unmaintained pygame recipe included (for an old pygame 1.9.1). With
  some work it should be possible to update the recipe to use the SDL2
  support in pygame.
| There was an older 'pygame subset for android' which is now
  unmaintained, and does not work with more recent Android devices.

Web
---

| There's not really an 'export for web' option at the moment. It is
  possible with both CPython and SDL as well as SDL2 working on
  emscripten (the compiler for WASM and stuff that goes on the web).
| Here is the latest 'cpython on web' project.
  https://github.com/iodide-project/pyodide

Building if you do not have a windows/mac/linux machine
-------------------------------------------------------

CI tools
~~~~~~~~

| If your game is open source, you can use these systems to build your
  game remotely for free.

-  Appveyor (for windows) https://www.appveyor.com/
-  Travis (for linux and mac) https://travis-ci.org/

| How to do that? Well, that's an exercise left up to the reader.
  Probably getting it to use pyinstaller, and having them upload the
  result somewhere.
| One python app that uses Travis and Appveyor is the Mu editor. You can
  see how in their .travis.yml and appveyor.yml files. See
  https://github.com/mu-editor/mu

Virtualbox
~~~~~~~~~~

| With virtualbox (and other emulators) you can run some systems on your
  local machine. Which means you do not need to buy a new development
  machine yourself for those platforms.
| Both windows and linux images are available that you could use
  legally.
| https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/
| Note, that it is good to do your testing on a free install, rather
  than testing on the same machine that you made your executables with.
  This is because perhaps you forgot to include some dependency, and
  that dependency is on the development machine, but not everyone else's
  machines.

Writing portable python code
----------------------------

| Some old (but still valid) basic advice on making your game portable:
  https://www.pygame.org/wiki/distributing
| Things like naming your files case sensitively.

Announcing your game.
---------------------

| Generic Indie game marketing guides all apply here.
| Some python/pygame specific avenues for marketing and announcing...

-  post a 'release' on the pygame website
-  mention it on the pygame reddit (and python reddit perhaps)
-  announce on the python announce mailing list
   (https://mail.python.org/mailman/listinfo/python-announce-list)
-  get your blog listed on planet with your 'python' tag. (open an issue
   https://github.com/python/planet/issues)
-  mention @pygame_org or #pygame for retweets

| Of course the python world is a tiny place compared to the entire
  world.

-  https://www.reddit.com/r/gamedevexpo/

|

Icons
-----

| Each platform has slightly different requirements for icons. This
  might be a nice place to link to all the requirements (TODO).

Making a game trailer (for youtube)
-----------------------------------

| You may not need to make the best trailer, or even a good trailer.
  Just a screen capture of your game might be 'good enough' and is
  better than nothing.
| How about making a trailer with pygame itself? You could call it 'demo
  mode', or 'intro mode'.
| There's a free iMovie on Mac, the Microsoft video editor on windows,
  and blender for all platforms. An alternative is to use the python
  module `moviepy <https://zulko.github.io/moviepy/>`__ and script your
  game trailer.
| OBS is pretty good multi platform free screen capture software.
  https://obsproject.com/download

-  `the top 10 best indie game trailers
   2018 <https://www.youtube.com/watch?v=NOx3uvUyHGs>`__
-  `How to Make an Indie Game Trailer With No
   Budget <https://gamedevelopment.tutsplus.com/tutorials/how-to-make-an-indie-game-trailer-with-no-budget--cms-20825>`__

Animated gif
------------

| These are useful for sharing on twitter and other such places, so
  people can see game play.
| You can save the .png files with pygame, and convert them to a gif
  with the 'convert' tool from imagemagik.

   ::

      # brew install imagemagick
      # sudo apt-get install imagemagick

      # call this in your main loop.
      pygame.image.save(surf, 'bla_%05d.png' % frame_idx)

|
| Now you can convert the png files to

   ::

      convert -delay 20 -loop 0 bla_*png animated.gif

|
| Some solutions on stack overflow.

-  https://stackoverflow.com/questions/10922285/is-there-a-simple-way-to-make-and-save-an-animation-with-pygame
-  https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
