# Simple Animation with PyGame, Donte Gardner, 1/13/22, 2:27PM, v0.9

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setup coloe values
WHITE = (255, 255, 255)
RED = (255,0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup the box data.
b1 = {'rect':pygame.Rect(300, 80, 50, 100),'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20),'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60),'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop.
while True:
    # Check for QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)

    for b in boxes:
        # Move the box data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['rect'].top < 0:
            # The box has moved past the top.
            if b['dir'] == UPLEFT: 
                b['dir'] = DOWNLEFT 
            if b['dir'] ==  UPRIGHT: # Align vertically with 62. 
                b['dir'] = DOWNRIGHT # Align vertically with 63. 
        if b['rect'].bottom > WINDOWHEIGHT: 
                # The box has moved past the bottom 
            if b['dir'] == DOWNLEFT: # Align vertically with 62. 
                b['dir'] = UPLEFT # UPLEFT
            if b['dir'] == UPRIGHT: # Align vertically with 62. 
                b['dir'] = UPRIGHT # UPRIGHT 
        if b['rect'].left < 0: # Align vertically with 60. 
                # The box has moved past the left 
            if b['dir'] == DOWNLEFT: # Align vertically with 62. 
                b['dir'] = DOWNRIGHT # Align vertically with 63. 
            if b['dir'] == UPLEFT: # Align vertically with 62. 
                b['dir'] = UPRIGHT # Align vertically with 63. 
        if b['rect'].right > WINDOWWIDTH: # Align vertically with 60. 
                # THe box has moved past the right
            if b['dir'] == DOWNRIGHT: # Align vertically with 62. 
                b['dir'] = DOWNLEFT # Align vertically with 63. 
            if b['dir'] == UPRIGHT: # Align vertically with 62. 
                b['dir'] = UPLEFT # Align vertically with 63. 

        # Draw rhe box onto the game surface.                       
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

   # Draw the window to the screen.
    pygame.display.update()
    time.sleep(0.02)
