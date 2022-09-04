import pygame
import sys

# Initialize pygame, set screen, set window title, set clock to control frame rate
pygame.init()
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platform Game')
clock = pygame.time.Clock()


# GAME SCREEN START
while True: 
    # EVENT LOOP
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    
    
    
    
    
    
    # Update Screen
    pygame.display.update()
    # Control FPS
    clock.tick(60)