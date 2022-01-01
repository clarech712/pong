# Pong Tutorial using Pygame
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
#
# Name: pong.py
# Modified by: clarech712
# Date: 1 January 2022
# Purpose: Implement two-player Pong

# Prevent pygame from printing message to command line
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import pygame library
import pygame

# Import Paddle class
from paddle import Paddle

# Initialise game engine
pygame.init()

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Create and position two Paddles
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Store Paddles in Sprite list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# Carry on until user exits game (e.g. clicks close button)
carryOn = True
 
# Control how fast screen updates
clock = pygame.time.Clock()
 
# Main programme loop
while carryOn:
        # Main event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # User clicks close
                        carryOn = False # Exit loop
                elif event.type == pygame.KEYDOWN: # User presses key
                        if event.key == pygame.K_x: # User presses "X" key
                                carryOn = False # Exit loop
 
        # Refresh screen and draw all Sprites
        all_sprites_list.update()

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