import pygame, sys
from settings import *
from tiles import Tile

# Initialize pygame, set screen, set window title, set clock to control frame rate
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platform Game')
clock = pygame.time.Clock()


tile = pygame.sprite.Group(Tile((600, 200), 200))

# GAME SCREEN START
while True: 
    # EVENT LOOP
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    
    tile.draw(screen)
    
    
    
    # Update Screen
    pygame.display.update()
    # Control FPS
    clock.tick(60)