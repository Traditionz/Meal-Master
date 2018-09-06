# Ziwei Hou Lab 063 zh367
from Drawable import Drawable
import pygame

# Inherits from Drawable
class Block(Drawable):

    def __init__(self, x, y, color=(0, 0, 255), w=20):
        super().__init__(x, y, color)
        # w = width
        self.__w = w

    def draw(self, surface):
        # Draws the block
        pygame.draw.rect(surface, self.getColor(), [self.getX(), self.getY(), self.__w, self.__w])
        # Draws the black outline for the block
        pygame.draw.rect(surface, (0, 0, 0), [self.getX(), self.getY(), self.__w, self.__w], 1)

    def get_rect(self):
        # Returns the 'hit box' of the blocks
        return pygame.Rect(self.getX(), self.getY(), self.__w, self.__w)
