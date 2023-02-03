import pygame

# initialize pygame
pygame.init()

# set screen dimensions
screen_width = 600
screen_height = 340
screen = pygame.display.set_mode((screen_width, screen_height))

# load background image
background = pygame.image.load("pictures/background.png")

# set player starting position
player_x = 100
player_y = 500

# load player image
player_image = pygame.image.load("pictures/player.png")

# set game speed
speed = 5

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # move player to the right
    player_x += speed
    
    # blit background and player onto the screen
    screen.blit(background, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    
    # update screen
    pygame.display.update()

# quit pygame
pygame.quit()
