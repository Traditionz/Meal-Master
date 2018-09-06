# Ziwei Hou Lab 063 zh367
import abc

# This is the abstract base class the other objects will inherit from.
class Drawable(metaclass=abc.ABCMeta):
    # Constructor for x position, y position, and color.
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color
        # Visibility is default to True so we can see the game.
        self.__visible = True

    # Return x position
    def getX(self):
        return self.__x

    # Return y position
    def getY(self):
        return self.__y

    # Return color
    def getColor(self):
        return self.__color

    # Returns the visibility of the object
    def getVisible(self):
        return self.__visible

    # Sets Visibility as v
    def setVisible(self, v):
        self.__visible = v

    # Sets the location of the object
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]

    # Returns the X and Y Location of the object
    def getLoc(self):
        return (self.getX(), self.getY())

    # Abstract base method to draw the shapes
    @abc.abstractmethod
    def draw(self, surface):
        pass

    # Abstract base method to return the 'hit box'.
    @abc.abstractmethod
    def get_rect(self):
        pass
