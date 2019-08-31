""" Some examples for generating and converting sounds for pygame.

Python 2.7, 3.6

Shows:
    - a simple 'square wave' generated
    - resampling sample rates (eg, 8363 to 44100)
    - using built in python array for making pygame.Sound samples.
    - samples at different bit sizes
    - converting from signed 8 to signed 16bit
    - how initializing the mixer changes what samples Sound needs.
    - Using the python stdlib audioop.ratecv for sample rate conversion.
    - drawing sound sample arrays as a waveform scaled into a Surface.

Square Wave
  https://en.wikipedia.org/wiki/Square_wave
MOD (file format)
  https://en.wikipedia.org/wiki/MOD_(file_format)

pygame.mixer.get_init
    https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.get_init
pygame.Sound
    https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound

array (python stdlib)
    https://docs.python.org/3/library/array.html
wave (python stdlib)
    https://docs.python.org/3/library/wave.html
audioop.ratecv (python stdlib)
    https://docs.python.org/3/library/audioop.html?highlight=audio#audioop.ratecv

"""

from array import array
import pygame as pg

class Tone(pg.mixer.Sound):
    """This generates a 'Square wave' with a generator.

    Then creates an array of samples, and passes that into pygame.Sound.
    """

    def __init__(self, frequency, array_type, volume=.1):
        self.frequency = frequency
        if array_type == 'b':
            # we have to convert the 1 byte 'b' samples to 2 byte 'h'.
            samples = self.signed_char_to_signed_short(
                self.make_samples_b()
            )
        elif array_type == 'h':
            samples = self.make_samples_h()
        else:
            raise ValueError('array_type not supported')

        self.samples = samples
        pg.mixer.Sound.__init__(self, buffer=samples)
        self.set_volume(volume)

    def make_samples_b(self):
        """ Builds samples array between -127 and 127.
            Array type 'h'.
        """
        mixer_frequency = pg.mixer.get_init()[0]
        mixer_format = pg.mixer.get_init()[1]
        period = int(round(mixer_frequency / self.frequency))
        max_amplitude = 2 ** (abs(mixer_format) - 1) - 1
        max_amplitude = int(max_amplitude / 256)
        # print(f'mixer_frequency:{mixer_frequency}, mixer_format:{mixer_format}')
        # print(f'period:{period}, max_amplitude:{max_amplitude}')

        # 'b' array is signed char, 1 byte
        # https://docs.python.org/3/library/array.html
        samples = array('b',
            (max_amplitude if time < period / 2 else -max_amplitude
                for time in range(period))
        )
        return samples

    def signed_char_to_signed_short(self, b_samples):
        """ Converts 1 byte signed char samples to 2 byte signed short.

            127 -> 32767
        """
        # just a simple linear conversion.
        factor = int(32767 / 127)
        return array('h', (sample * factor for sample in b_samples))

    def make_samples_h(self):
        """ Builds samples array between -32767 snd 32767.
            Array type 'h'.
        """
        mixer_frequency = pg.mixer.get_init()[0]
        mixer_format = pg.mixer.get_init()[1]
        period = int(round(mixer_frequency / self.frequency))
        max_amplitude = 2 ** (abs(mixer_format) - 1) - 1
        # print(f'mixer_frequency:{mixer_frequency}, mixer_format:{mixer_format}')
        # print(f'period:{period}, max_amplitude:{max_amplitude}')

        # 'h' array is signed short, 2 bytes
        # https://docs.python.org/3/library/array.html
        samples = array('h',
            (max_amplitude if time < period / 2 else -max_amplitude
                for time in range(period))
        )
        return samples


class Sample(pg.mixer.Sound):
    """ For playing a sample.

    Takes a file, and reads it in as 8bit signed data.

    Then converts it to the 16bit signed size the pygame.mixer needs.
    """
    def __init__(self, fname, volume=.1):
        with open(fname, 'rb') as f:
            samples = self.signed_char_to_signed_short (
                array('b', f.read())
            )
            pg.mixer.Sound.__init__(self, buffer=samples)
        self.set_volume(volume)

    def signed_char_to_signed_short(self, b_samples):
        """ Converts 1 byte signed char samples to 2 byte signed short.
            127 -> 32767
        """
        # just a simple linear conversion.
        import time
        t0=time.time()
        factor = int(32767 / 127)
        samples = array('h', (
            max(sample, -127) * factor if sample < 0 else
            min(sample, 127) * factor
            for sample in b_samples))
        t1=time.time()
        print(t1-t0)
        return samples


def fetch_example_mod_file(mod_fname):
    """ Grab a file that has a sound samples in it from the net.

    'MOD is a computer file format used primarily to represent music,
    and was the first module file format. MOD files use the ".MOD"
    file extension, except on the Amiga which doesn't rely on
    filename extensions, instead it reads a file's header to
    determine filetype. A MOD file contains a set of instruments in
    the form of samples, a number of patterns indicating how and when
    the samples are to be played, and a list of what
    patterns to play in what order.'

    https://en.wikipedia.org/wiki/MOD_(file_format)
    """
    import os
    url = 'https://api.modarchive.org/downloads.php?moduleid=101996'

    if not os.path.exists(mod_fname):
        import urllib2
        print ('Fetching %s .mod into file: %s' % (url, mod_fname))
        data = urllib2.urlopen(url).read()
        with open(mod_fname, 'w') as modf:
            modf.write(data)


def resample(mod_fname):
    """ An example of resampling audio to a different framerate.

    eg, from 8363 one byte samples per second to
        44100 two byte samples per second.
    """
    import audioop
    import wave
    from io import BytesIO

    in_framerate = 8363
    in_sampwidth = 1
    in_nchannels = 1

    out_framerate = 44100

    num_seconds = 5
    with open(mod_fname, 'rb') as f:
        # Throw away the start data of this mod file.
        #   Better samples later on.
        f.read(8363*2)
        in_frame_data = f.read(in_framerate * num_seconds)

    # https://docs.python.org/3/library/audioop.html?highlight=audio#audioop.ratecv
    newfragment, newstate = audioop.ratecv(
        in_frame_data,
        in_sampwidth,
        in_nchannels,
        in_framerate,
        out_framerate,
        None)

    # print(f'len(newfragment):{len(newfragment)}')
    # A perfect conversion is not possible, because the sample
    #   rates do not divide equally. However, the number
    #   of samples should be close.
    assert (out_framerate * num_seconds) - len(newfragment) < 10
    pg.mixer.Sound(buffer=newfragment).play(-1)



# TODO:
# Converting between modo and stereo?
#   audioop.tomono and audioop.tostereo
#   https://docs.python.org/3/library/audioop.html?highlight=audio#audioop.tomono
# Show it running in a separate process using mmap to share data efficiently.
# Using OSC messages to control it with other controllers (ipad, etc).
# More generator types
# Filters, envelopes and classic effects



def scale_samples_to_surf(width, height, samples):
    """ Returns a generator containing (x, y) to draw a waveform.

    :param width: width of surface to scale points to.
    :param height: height of surface to scale points to.
    :param samples: an array of signed 1 byte or signed 2 byte.
    """
    assert samples.typecode in ['h', 'b']
    # precalculate a bunch of variables, so not done in the loop.
    len_samples = len(samples)
    width_per_sample = width / len_samples
    height_1 = height - 1

    if samples.typecode == 'h':
        # for array typecode 'h', -32768 to 32768
        factor = 1.0 / 65532
        normalize_modifier = int(65532 / 2)
    elif samples.typecode == 'b':
        # for array typecode 'b', -127 to 127
        factor = 1.0 / 256
        normalize_modifier = int(256 / 2)

    return ((
        int((sample_number + 1) * width_per_sample),
        int(
            (1.0 -
                (factor *
                    (samples[sample_number] + normalize_modifier)))
            * (height_1)
        ))
    for sample_number in range(len_samples))

def draw_wave(surf,
              samples,
              wave_color = (0, 0, 0),
              background_color = pg.Color('white')):
    """Draw array of sound samples as waveform into the 'surf'.

    :param surf: Surface we want to draw the wave form onto.
    :param samples: an array of signed 1 byte or signed 2 byte.
    :param wave_color: color to draw the wave form.
    :param background_color: to fill the 'surf' with.
    """
    assert samples.typecode in ['h', 'b']
    if background_color is not None:
        surf.fill(background_color)
    width, height = surf.get_size()
    points = tuple(scale_samples_to_surf(width, height, samples))
    pg.draw.lines(surf, wave_color, False, points)



if __name__ == "__main__":
    # Set the mixer to have less buffer size, so it
    # https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.init
    pg.mixer.pre_init(44100, -16, 1, 1024)
    pg.init()

    pg.display.set_caption('Playing square wave, 808 frequency')
    screen = pg.display.set_mode((640, 480))

    mod_fname = 'outrun_3.mod'

    fetch_example_mod_file(mod_fname)

    # play on repeat, -1 means loop indefinitely.
    # https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play
    if 1:
        tone = Tone(frequency=808, array_type='b')
        tone.play(-1)

        print(tone.samples)
        waveform = pg.Surface((320, 200)).convert_alpha()
        draw_wave(waveform, tone.samples)
        screen.fill((255, 255, 255))
        screen.blit(waveform, (160, 100))

    if 0:
        try:
            Sample(mod_fname).play(-1)
        except IOError:
            print ('no %s' % mod_fname)
    if 0:
        pg.mixer.music.load(mod_fname)
        pg.mixer.music.play()

    if 0:
        resample(mod_fname)

    going = True
    while going:
        for e in pg.event.get():
            if e.type in [pg.QUIT]:
                going = False
            if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                going = False

        pg.display.flip()