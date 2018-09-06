# Ziwei Hou Lab 063 zh367
import pygame
from Ball import Ball
from Block import Block
from Text import Text

# Intersect definition provided in the HW4 pdf
def intersect(rect1, rect2):

    if rect1.x < rect2.x + rect2.width and rect1.x + rect2.width > rect2.x and rect1.y < rect2.y + rect2.height and \
            rect1.height + rect1.y > rect2.y:
        return True
    return False

# Starts the pygame and display
pygame.init()
surface = pygame.display.set_mode((500, 500))

# Sets the ball's location
ball = Ball(20, 400)

# List of interactive objects: blocks and a ball
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

# Sets the score position
score = Text(0, 0)

# Change in time, gravity, Rebound, and friction constants
dt = 0.01
g = 6.67
R = 0.7
eta = 0.5

# Current x and y positions
x0, y0, x1, y1 = 0, 0, 0, 0
# x and y velocities
xv, yv = 0, 0

while True:

    # If a button is clicked, something happens
    for event in pygame.event.get():
        # If exit, game exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Press Q to quit
        elif event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q:
            pygame.quit()
            exit()
        # Get position of mouse onclick
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = pygame.mouse.get_pos()
        # Get position of mouse after the click is released
        elif event.type == pygame.MOUSEBUTTONUP:
            x1, y1 = pygame.mouse.get_pos()
            xv = x1 - x0
            yv = (y1 - y0)

    # White background
    surface.fill((255, 255, 255))
    # Draws the line/floor
    pygame.draw.line(surface, (0, 0, 0), (0, 400), (500, 400))

    # Updates the velocity with gravity for each change in time
    yv = yv + g * dt

    # Updates the ball's position
    x = ball.getX() + xv * dt
    y = ball.getY() + yv * dt

    # If the y value is under the floor, it rebounds with friction
    if y > 400:
        y = 400
        yv = -R * yv
        xv = eta * xv
    # Otherwise, it continues with velocity and gravity for each change in time
    else:
        yv = yv + g * dt

    # Sets the ball's location for the change in x and y
    ball.setLoc((x, y))
    # Displays score
    score.draw(surface)

    # For each object in drawables list
    for block in drawables:
        # If it's a block (Search by color)
        if block.getColor() == (0, 0, 255):
            # If it intersects and visibility is on, block's visibility is turned off and score adds for each block hit
            if intersect(block.get_rect(), ball.get_rect()) and block.getVisible():
                score.setText(score.getText() + 1)
                block.setVisible(False)

    # For each object in the list, draw the object
    for drawable in drawables:
        # If visibility is True, draw the object
        if drawable.getVisible():
            drawable.draw(surface)
    # Updates the display
    pygame.display.update()