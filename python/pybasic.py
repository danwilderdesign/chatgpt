''' 
Basic Python game

The initial setup for this code was built using ChatGPT. The 
    - The prompt: 
I used the 
'''

import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 340
screen = pygame.display.set_mode((screen_width, screen_height))

# load background image
background = pygame.image.load("pictures/background.png")

# Load player image
player_image = pygame.image.load("pictures/player.png")

# Set player starting position
player_x = 100
player_y = 100

# Set player speed
speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('crouch')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('crouch stop')
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Blit background onto the screen
    # screen.blit(background, (0, 0))

    # Blit player onto the screen
    screen.blit(player_image, (player_x, player_y))
    
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
