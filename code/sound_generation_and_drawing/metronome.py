"""
Show a light for every beat.
Show the BPM as text.
Use 4/4 timing. Four beats to a bar.

Press space until the BPM gets to what you want.
"""
import time
import os
import pygame as pg


def average_bpm(times):
    """ For the list of times(seconds since epoch) return
        the average beats per minute.
    """
    spaces = []
    previous = times[0]
    for t in times[1:]:
        spaces.append(t - previous)
        previous = t
    avg_space = sum(spaces) / len(spaces)
    return 60.0 / avg_space


class Bpm:
    """ Beats Per Minute.

    By press()ing this, the bpm counter will change.
    """

    def __init__(self):

        self.space_between_beats = 0.5
        self.last_press = time.time()
        """ The time since epoch of the last press.
        """
        self.bpm = 120
        self.bpm_average = 120
        """ The average bpm from the last 4 presses.
        """

        self.times = []


        self._last_update = time.time()
        self._elapsed_time = 0.0
        self._last_closeness = 1.0

        self.on_beat = 0
        """ The time since the epoch when the last beat happened.
        """

        self.beat_num = 0
        """ accumlative counter of beats.
        """

        self.finished_beat = 0
        """ True for one tick, when 0.1 seconds has passed since the beat.
        """

        self.first_beat = 0
        """ True if we are the first beat on a bar (out of 4).
        """

        self.started_beat = 0
        """ This is true only on the tick
        """


    def press(self):
        """ For when someone is trying to update the timer.
        """
        press_time = time.time()
        self.space_between_beats = press_time - self.last_press
        self.last_press = press_time
        self.times.append(press_time)
        self.bpm = 60.0 / self.space_between_beats

        if len(self.times) > 4:
            self.bpm_average = average_bpm(self.times[-4:])
            self.times = self.times[-4:]
        else:
            self.bpm_average = self.bpm


    def update(self):
        the_time = time.time()
        self._elapsed_time += the_time - self._last_update
        self._last_update = the_time

        # if _elapsed_time 'close' to bpm show light.
        space_between_beats = 60.0 / self.bpm_average
        since_last_beat = the_time - self.on_beat

        self.finished_beat = self.on_beat and (since_last_beat > 0.1)
        if self.finished_beat:
            self.on_beat = 0

        closeness = self._elapsed_time % space_between_beats
        if closeness < self._last_closeness:
            self.on_beat = the_time
            self.finished_beat = 0
            self.dirty = 1
            self.beat_num += 1
            self.started_beat = 1
            self.first_beat = not (self.beat_num % 4)
        else:
            self.started_beat = 0

        self._last_closeness = closeness


class BpmCounter(pg.sprite.DirtySprite):
    """ For showing a text representing what the Beats Per Minute is.
    """
    def __init__(self, bpm):
        pg.sprite.DirtySprite.__init__(self)
        self.bpm = bpm

        self.font = pg.font.SysFont("Arial", 24)
        self.image = self.font.render(
            "%s" % int(self.bpm.bpm_average), True, (255, 255, 255)
        )
        self.rect = self.image.get_rect()

    def press(self):
        self.bpm.press()
        self.image = self.font.render(
            "%s" % int(self.bpm.bpm_average), True, (255, 255, 255)
        )
        self.rect = self.image.get_rect()
        self.dirty = 1

    def events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.press()


class BpmLight(pg.sprite.DirtySprite):
    """ Shows a red 'light' representing each beat.
    """
    def __init__(self, bpm):
        pg.sprite.DirtySprite.__init__(self)
        self.bpm = bpm

        self.image = pg.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 5

    def press(self):
        self.image.fill((255, 0, 0))
        self.elapsed_time = 0.0

    def update(self):

        if self.bpm.finished_beat:
            self.image.fill((0, 0, 0))
            self.dirty = 1
        if self.bpm.started_beat:
            self.image.fill((255, 0, 0))
            self.dirty = 1

def main():

    if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 512)
    pg.init()
    screen = pg.display.set_mode((640, 480))
    going = True

    bpm = Bpm()
    bpm_counter = BpmCounter(bpm)
    bpm_light = BpmLight(bpm)
    clock = pg.time.Clock()

    pygame_dir = os.path.split(os.path.abspath(pg.__file__))[0]
    data_dir = os.path.join(pygame_dir, "examples", "data")
    sound = pg.mixer.Sound(os.path.join(data_dir, "punch.wav"))

    pg.display.set_caption('press space 4 times to adjust BPM timing')

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    allsprites = pg.sprite.LayeredDirty([bpm_counter, bpm_light])
    allsprites.clear(screen, background)

    while going:
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key in [pg.K_ESCAPE, pg.K_q]:
                going = False

        bpm.update()
        # if bpm.started_beat and bpm.first_beat:
        #     sound.play()
        if bpm.started_beat:
            sound.play()

        bpm_counter.events(events)
        allsprites.update()

        rects = allsprites.draw(screen)

        # note, we don't update the display every 240 seconds.
        if rects:
            pg.display.update(rects)
        # We loop quickly so timing can be more accurate with the sounds.
        clock.tick(240)
        # print(rects)
        # print(clock.get_fps())

if __name__ == '__main__':
    main()
