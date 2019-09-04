.. contents::
   :depth: 3
..

| Taking a byte of bits of Serial, along with Green screen with Sam,
  pygame, and an Arduino hooked up to a light sensor and a motor thing.
| Coffee too?  Naturally.
| Where do we begin?  At the end of course.  A video of the result...

.. container:: separator

| 

The arduino code
================

::

   #include <Servo.h>
   Servo myservo;
   int potpin = 0;
   int val;

   void setup() {
     Serial.begin(9600);
     myservo.attach(9);
   } 
    
   void loop() {
     val = analogRead(potpin);
     Serial.println(val);
     val = map(val, 62, 540, 0, 179);
     myservo.write(val);
     delay(15);
   }

python pygame code
==================

| Extended the "`green eggs and
  ham" <http://renesd.blogspot.de/2013/04/reducing-number-of-concepts-to-make.html>`__
  code I made recently to read serial data from the Arduino, and paint
  the screen different shades of green, whilst also making some silly
  sounds depending on the value read from the light sensor.

.. code:: code

   import os
   import pygame
   import serial

   # guessing serial ports names. Linux or macosx.
   #'/dev/tty.usbserial'
   ser = serial.Serial('/dev/tty.usbmodem1411',
                       9600,
                       timeout = 0)
   serial_buffer = ""

   # an event number for the SERIAL
   SERIAL = pygame.USEREVENT + 1


   from pygame.locals import *
   Event = pygame.Event
   split = os.path.split


   pygame.mixer.pre_init(44100, 8, 2, 1024)
   pygame.init()
   screen = pygame.display.set_mode((640, 480))
   message = "Press q to quit, b for blue, r for red."
   pygame.display.set_caption(message)

   import pygame.examples
   example_path = split(pygame.examples.__file__)[0]
   example_data = os.path.join(example_path, "data")
   sounds = [pygame.mixer.Sound("wiff.wav"),
             pygame.mixer.Sound("punch.wav"),
            ]

   going = True
   while going:
       serial_data = ser.read()
       #print (repr(serial_data))
       while serial_data:
           serial_buffer += serial_data
           # if there is a new line in it, then
           if "\r\n" in serial_buffer:
               #print (repr(serial_buffer))

               evt = Event(SERIAL,
                           {'line': serial_buffer})
               pygame.event.post(evt)
               serial_buffer = ""
           serial_data = ser.read()

       events = pygame.event.get()

       for event in events:
           print (event)
           if event.type == KEYDOWN and event.key == K_q:
               going = False
           if event.type == KEYDOWN and event.key == K_b:
               screen.fill(Color("blue"))
           if event.type == KEYDOWN and event.key == K_r:
               screen.fill(Color("red"))
           if event.type == SERIAL:
               # read the line from the serial event.
               print (repr(event.line))

               # clean up, and do sanity checking.
               # It could be corrupt or garbage.
               line = event.line.replace("\r\n", "")
               line = line.replace("\n", "")
               line = line.replace("\r", "")
               # it could be empty.
               if line:
                   val = int(line)
                   if val < 1024 and val > 0:
                       print (repr(val))
                       # map 0 and 1023 of analog read to
                       #  0-255 colour colour range.
                       green = int((val/float(1023))*255 )
                       screen.fill((0, green, 0))
                       if val < 100:
                           sounds[0].play()
                       if val > 300:
                           sounds[1].play()

       pygame.display.flip()

   ser.close()
