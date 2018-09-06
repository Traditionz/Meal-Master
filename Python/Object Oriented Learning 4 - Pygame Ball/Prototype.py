import pygame
import abc


class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__visible = True

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getColor(self):
        return self.__color

    def getVisible(self):
        return self.__visible

    def setVisible(self, v):
        self.__visible = v

    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]

    def getLoc(self):
        return (self.getX(), self.getY())

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass


class Block(Drawable):
    def __init__(self, x, y, color=(0, 0, 255), w=20):
        super().__init__(x, y, color)
        self.__w = w

    def draw(self, surface):
        pygame.draw.rect(surface, self.getColor(), [self.getX(), self.getY(), self.__w, self.__w])
        pygame.draw.rect(surface, (0, 0, 0), [self.getX(), self.getY(), self.__w, self.__w], 1)

    def get_rect(self):
        return pygame.Rect(self.getX(), self.getY(), self.__w, self.__w)


class Ball(Drawable):
    def __init__(self, x, y, color=(255, 0, 0), r=8):
        super().__init__(x, y, color)
        self.__r = r

    def getR(self):
        return self.__r

    def draw(self, surface):
        pygame.draw.circle(surface, self.getColor(), (int(self.getX()), int(self.getY())), self.__r)

    def get_rect(self):
        return pygame.Rect(self.getX() - self.getR(), self.getY() - self.getR(), 2 * self.getR(), 2 * self.getR())


class Text(Drawable):
    def __init__(self, x, y, color=(0, 0, 0), text=0):
        super().__init__(x, y, color)
        self.__text = text

    def getText(self):
        return self.__text

    def setText(self, t):
        self.__text = t

    def draw(self, surface):
        font = pygame.font.SysFont("comicsans", 24)
        surface.blit(font.render("Score:" + str(self.__text), False, (0, 0, 0)), (0, 0))

    def get_rect(self):
        pass


def intersect(rect1, rect2):
    if rect1.x < rect2.x + rect2.width and rect1.x + rect2.width > rect2.x and rect1.y < rect2.y + rect2.height and \
            rect1.height + rect1.y > rect2.y:
        return True
    return False


pygame.init()
surface = pygame.display.set_mode((500, 500))

ball = Ball(20, 400)

drawables = []
drawables.append(Block(380, 380))
drawables.append(Block(400, 380))
drawables.append(Block(420, 380))
drawables.append(Block(380, 360))
drawables.append(Block(400, 360))
drawables.append(Block(420, 360))
drawables.append(Block(380, 340))
drawables.append(Block(400, 340))
drawables.append(Block(420, 340))
drawables.append(ball)

score = Text(100, 50)

dt = 0.005
g = 9.8

x0, y0, x1, y1 = 0, 0, 0, 0
xv, yv = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            x1, y1 = pygame.mouse.get_pos()
            xv = x1 - x0
            yv = (y1 - y0)

    surface.fill((255, 255, 255))
    pygame.draw.line(surface, (0, 0, 0), (0, 400), (500, 400))

    yv += g * dt

    xv *= 0.999
    yv *= 0.999

    x = ball.getX() + xv * dt
    y = ball.getY() + yv * dt

    if y > 400:
        y = 400

    ball.setLoc((x, y))
    score.draw(surface)

    for block in drawables:
        if block.getColor() == (0, 0, 255):
            if intersect(block.get_rect(), ball.get_rect()) and block.getVisible():
                score.setText(score.getText() + 1)
                block.setVisible(False)

    for drawable in drawables:
        if drawable.getVisible():
            drawable.draw(surface)
    pygame.display.update()