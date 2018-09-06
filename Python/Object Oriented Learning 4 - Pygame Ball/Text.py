# Ziwei Hou Lab 063 zh367
from Drawable import Drawable
import pygame

# Inherits from Drawable
class Text(Drawable):

    def __init__(self, x, y, color=(0, 0, 0), text=0):
        super().__init__(x, y, color)
        # Text to be displayed as score
        self.__text = text

    # Sets text
    def setText(self, t):
        self.__text = t

    # Returns text
    def getText(self):
        return self.__text

    # Draws the Text using pygame's methods
    def draw(self, surface):
        # Sets the font type and size
        font = pygame.font.SysFont("comicsans", 50)
        # Display the font on the top left corner as black
        surface.blit(font.render("Score:" + str(self.__text), False, (0, 0, 0)), (0, 0))

    # Text doesn't have 'hit box'
    def get_rect(self):
        pass