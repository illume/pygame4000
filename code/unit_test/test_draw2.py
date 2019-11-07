""" where we test if the ellipse draws red.
"""
import unittest


class TestEllipse(unittest.TestCase):

    def test_ellipse(self):
        import pygame.draw
        black = pygame.Color('black')
        red = pygame.Color('red')

        surf = pygame.Surface((320, 200))
        surf.fill(black)

        # The area the ellipse is contained in, is held by rect.
        #
        # 10 pixels from the left,
        # 11 pixels from the top.
        # 225 pixels wide.
        # 95 pixels high.
        rect = (10, 11, 225, 95)
        pygame.draw.ellipse(surf, red, rect)

        # To see what is drawn you can save the image.
        # pygame.image.save(surf, "test_draw2_image.png")

        # The ellipse should not draw over the black in the top left spot.
        self.assertEqual(surf.get_at((0, 0)), black)

        # It should be red in the middle of the ellipse.
        middle_of_ellipse = (125, 55)
        self.assertEqual(surf.get_at(middle_of_ellipse), red)


if __name__ == '__main__':
    unittest.main()
