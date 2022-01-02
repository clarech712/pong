# Pong Tutorial using Pygame
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
#
# Name: paddle.py
# Modified by: clarech712
# Date: 1 January 2022
# Purpose: Implement Paddle class

# Import pygame library and define colour
import pygame
BLACK = (0, 0, 0)

# Implement paddle class
class Paddle(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
                # Call parent class constructor
                super().__init__()
                
                # Set paddle colour, width, and height
                # Set background colour
                self.image = pygame.Surface([width, height])
                self.image.fill(BLACK)
                self.image.set_colorkey(BLACK)
 
                # Draw rectangular paddle
                pygame.draw.rect(self.image, color, [0, 0, width, height])
                
                # Fetch rectangle object with dimensions of image
                self.rect = self.image.get_rect()
                
        # Vertical motion
        def moveUp(self, pixels):
                self.rect.y -= pixels
		        # Prevent from going off screen
                if self.rect.y < 0:
                        self.rect.y = 0
          
        def moveDown(self, pixels):
                self.rect.y += pixels
                # Prevent from going off screen
                if self.rect.y > 400:
                        self.rect.y = 400
        
        