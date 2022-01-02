# Pong Tutorial using Pygame
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
#
# Name: paddle.py
# Modified by: clarech712
# Date: 1 January 2022
# Purpose: Implement Ball class

# Import pygame library, randint, and define colour
import pygame
from random import randint
BLACK = (0,0,0)
 
# Implement Ball class
class Ball(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
                # Call parent class constructor
                super().__init__()
                
                # Set Ball colour, width, and height
                # Set background colour
                self.image = pygame.Surface([width, height])
                self.image.fill(BLACK)
                self.image.set_colorkey(BLACK)
 
                # Draw rectangular Ball
                pygame.draw.rect(self.image, color, [0, 0, width, height])
                
                # Set velocity at random (to make game less predictable?)
                self.velocity = [randint(4,8), randint(-8,8)]
                
                # Fetch rectangle object with dimensions of image
                self.rect = self.image.get_rect()
                
        # To be called for each frame of main loop
        def update(self):
                self.rect.x += self.velocity[0]
                self.rect.y += self.velocity[1]
        
        # To be called on collision with Paddle
        def bounce(self):
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = randint(-8,8)
