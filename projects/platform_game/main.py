import pygame, sys
from settings import *
from tiles import Tile
from level import Level

# Initialize pygame, set screen, set window title, set clock to control frame rate
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platform Game')
clock = pygame.time.Clock()
level = Level(level_map, screen)


# GAME SCREEN START
while True: 
    # EVENT LOOP
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    
    screen.fill('black')
    level.run()
    
    # Update Screen
    pygame.display.update()
    print()
    # Control FPS
    clock.tick(60)