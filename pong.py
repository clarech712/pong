# Pong Tutorial using Pygame
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
#
# Modified by: clarech712
# Date: 1 January 2022

# Prevent pygame from printing message to command line
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import pygame library and initialise game engine
import pygame
pygame.init()

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Carry on until user exits game (e.g. clicks close button)
carryOn = True
 
# Control how fast screen updates
clock = pygame.time.Clock()
 
# Main programme loop
while carryOn:
        # Main event loop
        for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # User clicked close
                          carryOn = False # Exit loop
 
        # --- Game logic should go here
 
 
 
        # --- Drawing code should go here
        # Clear screen to black
        screen.fill(BLACK)
        
        # Draw net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
        # Update screen
        pygame.display.flip()
         
        # Limit to 60 frames per second
        clock.tick(60)
 
# Stop game engine
pygame.quit()