import pygame
from sys import exit

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()

while True: 
    #checks for any player input
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #most secure way to exit pygame
    #draw all of our elements
    #updates everything
    pygame.display.update()
    clock.tick(60)