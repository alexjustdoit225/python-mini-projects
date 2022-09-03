import pygame
from sys import exit

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('projects\\pygame_intro\\font\\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('projects\pygame_intro\graphics\Sky.png').convert()
ground_surface = pygame.image.load('projects\pygame_intro\graphics\ground.png').convert()
text_surface = test_font.render("First Game", False, 'black')

snail_surface = pygame.image.load('projects\pygame_intro\graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright= (700, 300))

player1_surf = pygame.image.load('projects\pygame_intro\graphics\Player\player_walk_1.png').convert_alpha()
player1_rect = player1_surf.get_rect(midbottom= (80, 300))
player1_grav = 0

score_surf = test_font.render('Score: ', False, 'black')
score_rect = score_surf.get_rect(midbottom= (WIDTH//2 - 40, 150))

while True: 
    #checks for any player input
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #most secure way to exit pygame
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if (player1_rect.collidepoint(event.pos)): 
                print('collision')
                if player1_rect.bottom == 300: 
                    player1_grav = -20
        #detects if a key is pressed down
        if event.type == pygame.KEYDOWN: 
            print('keydown')
            if event.key == pygame.K_SPACE and player1_rect.bottom == 300:
                player1_grav = -20
                
                
    #draw all of our elements
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    #draw the rectangle you used to position score
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 0, 5)
    screen.blit(score_surf, score_rect)
    
    snail_rect.left += 4
    if snail_rect.right <= 0: snail_rect.left = 800
    elif snail_rect.left >= 800: snail_rect.right = 0
    screen.blit(snail_surface, snail_rect)
    
    #add gravity to player
    player1_grav += 1
    player1_rect.y += player1_grav
    if player1_rect.bottom >= 300: player1_rect.bottom = 300
    
    player1_rect.left += 2
    if player1_rect.right <= 0: player1_rect.left = 800
    elif player1_rect.left >= 800: player1_rect.right = 0
    screen.blit(player1_surf, player1_rect)
    
    if player1_rect.colliderect(snail_rect): 
        print('collision detected')
        
    #updates everything
    pygame.display.update()
    clock.tick(60)