Python game programming part 6 - Abstraction
============================================


Wrapping up the libraries and forgetting the details
----------------------------------------------------

Your problem: you want to play a sound, but don't know where to start
with this library you are trying out.

Often libraries are much more complex than what you want to deal with.

The solution is to wrap it up in something that you are more comfortable
using.

Another good reason to wrap up a library is if you want to maybe use two
different libraries. For playing sounds, maybe later you want to use
openal, or fmod sound libraries instead of pygames sound system. However
you have allready got lots of sound code in your programs. It is
probably going to be much easier to make an implementation of your
wrapper than to use try and replace all of your pygame specific sound
code.

Why are libraries complex? Often libraries do lots of different
wonderful things, for lots of different people. The libraries have lots
of features, and are often quite flexible. The price for lots of
features, and flexibility is often complexity.

Below we are going to make a wrapper for the pygame sound library as an
example of wrapping up a library and forgetting the details. The pygame
sound system is pretty simple to use allready, but we're going to try
making something simpler still!


Goals for our sounds module
~~~~~~~~~~~~~~~~~~~~~~~~~~~

One goal for making this sound wrapper will be to make it as simple as
possible to load and play sounds. One line to play a sound would be
acceptable(without extra lines to load the sounds).

A secondary goal for our sound module can be stated like this "Make the
simple things easy, and the difficult things possible". What this means
is that by default the most common things should be \*really\* easy to
do. However we also want to make difficult things possible to do. In our
case changing volume for the sounds should be possible. So should
queueing sounds. Also loading files from a different directory should be
possible.


Disadvantages to wrapping up a library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your simplifications may make it hard to fully take advantage of certain
features. This can be an easy mistake to make if you do not really know
the library you are dealing with.

Wrapping is extra work you have to do. It is extra code you have to
write, test, and maintain. So, are the benefits of wrapping a library
enough to make it worth doing? This is up to you to decide.


Our sounds module
-----------------

Here is how we will use our new, simple to use sounds module.

::

   import sounds
   sound_manager = sounds.SoundManager()

   sound_manager.play("bump")

Ok so we kind of failed at our goal of making it be done in one line.
However counting import lines is not fair :)

We have to have a "sounds" directory with .ogg files(compressed sound
files) in it. The sound manager looks in this directory for you, and
loads up all of the files.

To play the "bump" sound there would need to be a sounds/bump.ogg file.

When you call the play() method the `SoundManager <SoundManager>`__
looks to see if it has allready loaded the sound. If it is not loaded,
it loads the sound for you.


Extra features for our sound module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a couple of extra features that are in this sound module.
Which maybe you don't need. They are hidden by using default arguments.

One feature is to allow you to say the volume of each speaker that the
sound should play at.

::

   # play it loud out of left, and silent in right.
   sound_manager.play("bump", volume = [1., 0.])

::

   # play it at half volume out of both speakers.
   sound_manager.play("bump", volume = [0.5, 0.5])

The other feature is basic sound queueing.

I'll describe the sound queueing feature after we go through the
implementation of our sounds module.


Implementing our sound module
-----------------------------

As you may know by now a python module can simply be the code inside a
.py file.

Below is our code for the sounds module in full. It should be put inside
a file called sounds.py

::

   import pygame
   import os
   import glob
   import time

   from pygame.locals import *


   # path where all our sounds are.
   SOUND_PATH = os.path.join("sounds")



   def get_sound_list(path = SOUND_PATH):
       """ gets a list of sound names without thier path, or extension.
       """
       # load a list of sounds without path at the beginning and .ogg at the end.
       sound_list = map(lambda x:x[len(SOUND_PATH):-4],
                        glob.glob(os.path.join(SOUND_PATH,"*.ogg"))
                       )


       return sound_list


   SOUND_LIST = get_sound_list()




   class SoundManager:
       """ Controls loading, mixing, and playing the sounds.
           Having seperate classes allows different groups of sounds to be
            loaded, and unloaded from memory easily.

           Useage:
               sm = SoundManager()
               sm.play("bump")
       """


       def __init__(self):
           """
           """
           # keyed by the sound name, value is a sound object.
           self.sounds = {}

           # keyed by sound name, value is the channel.
           self.chans = {}

           self._debug_level = 0

           # sounds which are queued to play.
           self.queued_sounds = []

       def _debug(self, x, debug_level = 0):
           """ Used for optionally printing debug messages.
           """
           if self._debug_level > debug_level:
               print(x)



       def load(self, names = SOUND_LIST, path = SOUND_PATH):
           """Loads sounds."""
           sounds = self.sounds

           if not pygame.mixer:
               for name in names:
                   sounds[name] = None
               return
           for name in names:
               if not sounds.has_key(name):
                   fullname = os.path.join(path, name+'.ogg')
                   try:
                       sound = pygame.mixer.Sound(fullname)
                   except:
                       sound = None
                       self._debug("Error loading sound", fullname)
                   sounds[name] = sound


       def _getSound(self, name):
           """ Returns a Sound object for the given name.
           """
           if not self.sounds.has_key(name):
               self.load([name])

           return self.sounds[name]



       def play(self, name, volume=[1.0, 1.0], wait = 0):
           """ Plays the sound with the given name.
               name - of the sound.
               volume - left and right.  Ranges 0.0 - 1.0
               wait - used to control what happens if sound is allready playing:
                   0 - will not wait if sound playing.  play anyway.
                   1 - if there is a sound of this type playing wait for it.
                   2 - if there is a sound of this type playing do not play again.
           """

           vol_l, vol_r = volume

           sound = self._getSound(name)

           if sound:
               # check to see if we want to do any sound queueing, and handle it.
               if wait in [1,2]:
                   # check if the sound is allready playing, and is busy...
                   if self.chans.has_key(name) and self.chans[name].get_busy():
                       if wait == 1:
                           # sound is allready playing we wait for it to finish.
                           self.queued_sounds.append((name, volume, wait))
                           return
                       elif wait == 2:
                           # not going to play sound if playing.  We do nothing.
                           return

               # play the sound, and store its channel in a
               #   dictionary, keyed by the sound name.
               self.chans[name] = sound.play()

               # if the sound did not play, start fading out a channel, and
               #   use pygames queueing to queue up a sound on that channel.
               if not self.chans[name]:
                   # forces a channel to return. we fade that out,
                   #  and enqueue our one.
                   self.chans[name] = pygame.mixer.find_channel(1)
                   self.chans[name].fadeout(100)
                   self.chans[name].queue(sound)

               # if we have a channel, set its volume.
               if self.chans[name]:
                   self.chans[name].set_volume(vol_l, vol_r)



       def update(self, elapsed_time):
           """ This should be called frequently.  At least once every game tic/frame.
           """
           # if the sound for the channel is not busy we
           for name in self.chans.keys():
               if not self.chans[name].get_busy():
                   del self.chans[name]
           # copy the current queue, to the old queue.
           old_queued = self.queued_sounds

           # start a new queue.
           self.queued_sounds = []

           # Try and play any sounds from the old queue.
           #   This may queue the sounds again, if they still shouldn't be played.
           for snd_info in old_queued:
               name, volume, wait = snd_info
               self.play(name, volume, wait)

Here is a little test program for our new sounds module.

::

   import pygame, time
   import sounds

   pygame.init()
   sound_manager = sounds.SoundManager()
   sound_manager.play("bump")

   # we sleep for one second so that pygame has time to play the sound before quiting.
   time.sleep(1)

You can get a `bump.ogg <http://py3d.org/files/bump.ogg>`__ sound to
play with it. Of course it's fun making your own sounds in the
microphone :)


Next
~~~~

`Part Seven <_07_minimal_game>`__

