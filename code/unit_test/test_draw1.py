""" here is a very simple test.

An easy test to write, but it provides really good value.

- Shows an example of using the code.
- Makes sure the arguments are correct.
- Makes sure the code runs on 20+ different platforms and python versions.
- No "regressions" (Code that starts failing because of a change).


It doesn't actually test if an ellipse is drawn...
but that can come later.

If there is no test at all for a function this is a great test!
"""
import unittest


class TestEllipse(unittest.TestCase):

    def test_ellipse(self):
        import pygame.draw
        surf = pygame.Surface((320, 200))
        pygame.draw.ellipse(surf, (255, 0, 0), (10, 10, 25, 20))


if __name__ == '__main__':
    unittest.main()
