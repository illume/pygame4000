Sound generation and drawing
============================


Here's a few sound generation examples with pygame (and no numpy/scipy).

All the basics for making a music program (sampler/synth).

    - some sample rate conversion,
    - bit rate conversion
    - tone generation using generators (square wave)
    - python arrays used as buffers for pygame.Sound (zero copy).

code/sound_generation_and_drawing/sound_samples.py

    - a simple 'square wave' generated
    - resampling sample rates (eg, 8363 to 44100)
    - using built in python array for making pygame.Sound samples.
    - samples at different bit sizes
    - converting from signed 8 to signed 16bit
    - how initializing the mixer changes what samples Sound needs.
    - Using the python stdlib audioop.ratecv for sample rate conversion.
    - drawing sound sample arrays as a waveform scaled into a Surface.


Metronome.
----------

code/sound_generation_and_drawing/metronome.py

