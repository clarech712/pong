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

# Import Paddle and Ball classes
from paddle import Paddle
from ball import Ball

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

# Create and position Ball
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# Store all Sprites in Sprite list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

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
 
        # Move Paddle when key pressed 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: # User A presses "W" key
                paddleA.moveUp(5) # Move Paddle of User A up
        if keys[pygame.K_s]: # User A presses "S" key
                paddleA.moveDown(5) # Move Paddle of User A down
        if keys[pygame.K_UP]: # User B presses up arrow
                paddleB.moveUp(5) # Move Paddle of User B up
        if keys[pygame.K_DOWN]: # User B presses down arrow
                paddleB.moveDown(5) # Move Paddle of User B down
        
        # GAME LOGIC
        # Refresh screen and draw all Sprites
        all_sprites_list.update()
        
        # If Ball bouncing against any of four walls, change velocity
        if ball.rect.x >= 690:
                ball.velocity[0] = - ball.velocity[0]
        if ball.rect.x <= 0:
                ball.velocity[0] = - ball.velocity[0]
        if ball.rect.y > 490:
                ball.velocity[1] = - ball.velocity[1]
        if ball.rect.y < 0:
                ball.velocity[1] = - ball.velocity[1] 

        # If Ball colliding with Paddle, change velocity
        if (pygame.sprite.collide_mask(ball, paddleA) or
                pygame.sprite.collide_mask(ball, paddleB)):
                ball.bounce()
        
        # DRAWING
        # Clear screen to black
        screen.fill(BLACK)

        # Draw net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        
        # Draw all Sprites
        all_sprites_list.draw(screen) 

        # Update screen
        pygame.display.flip()
        
        # Limit to 60 frames per second
        clock.tick(60)
 
# Stop game engine
pygame.quit()