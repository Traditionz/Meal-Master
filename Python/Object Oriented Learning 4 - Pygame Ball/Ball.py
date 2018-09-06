# Ziwei Hou Lab 063 zh367
from Drawable import Drawable
import pygame

# Inherits from Drawable
class Ball(Drawable):

    def __init__(self, x, y, color=(255, 0, 0), r=8):
        super().__init__(x, y, color)
        # r = radius
        self.__r = r

    # Draws the red ball
    def draw(self, surface):
        pygame.draw.circle(surface, self.getColor(), (int(self.getX()), int(self.getY())), self.__r)

    # Returns the 'hit box' for the red ball
    def get_rect(self):
        return pygame.Rect(self.getX() - self.__r, self.getY() - self.__r, 2 * self.__r, 2 * self.__r)