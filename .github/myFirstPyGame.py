# My First PyGame, Donte Gardner, 11/29/21 1:59, v0,5 

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup our window. 1
windowSurface = pygame.display.set_mode((500, 400),0, 32)
pygame.display.set_caption('Hello, world!')

# Setuo Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup text
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect= text.get_rect()
textRect.centerx = windowsurface.get_rect().centerx
textRect,centery + windowSurface.get_rect().centery

# Fill background color.
windowSurface.fill(WHITE)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, GREEN,((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))