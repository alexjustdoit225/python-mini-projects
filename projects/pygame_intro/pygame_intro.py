from this import d
import pygame
from sys import exit
from random import randint

def score(): 
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {time}', False, (64,64,64))
    score_rect = score_surf.get_rect(midbottom= (370, 50))
    screen.blit(score_surf, score_rect)
    return time
    
def obstacle_movement(obstacle_list): 
    if obstacle_list: 
        for rectangles in obstacle_list: 
            rectangles.x -= 5
            
            screen.blit(snail_surface, rectangles)
        return obstacle_list
    else: 
        return []


pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('projects\\pygame_intro\\font\\Pixeltype.ttf', 50)
game_active = False
start_time = 0
display_score = 0

sky_surface = pygame.image.load('projects\pygame_intro\graphics\Sky.png').convert()
ground_surface = pygame.image.load('projects\pygame_intro\graphics\ground.png').convert()

# Obstacles
snail_surface = pygame.image.load('projects\pygame_intro\graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright= (700, 300))

obstacle_rect_list = []




player1_surf = pygame.image.load('projects\pygame_intro\graphics\Player\player_walk_1.png').convert_alpha()
player1_rect = player1_surf.get_rect(midbottom= (80, 300))
player1_grav = 0

#intro screen
player1_stand = pygame.image.load('projects\pygame_intro\graphics\Player\player_stand.png').convert_alpha()
player1_stand = pygame.transform.rotozoom(player1_stand, 0, 2)
player1_stand_rect = player1_stand.get_rect(center= (400, 200))
title_surf = test_font.render('Pixel Runner', False, (111,196,169))
title_rect = title_surf.get_rect(center= (400, 50))
start_surf = test_font.render("Press 'Space' to start", False, (111,196,169))
start_rect = start_surf.get_rect(midbottom= (400,350))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True: 
    #checks for any player input
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit() #most secure way to exit pygame
        if game_active: 
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
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                print('keydown')
                game_active = True
                player1_rect.right = 0
                snail_rect.left = WIDTH
                start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active: 
            print('test')
            obstacle_rect_list.append(snail_surface.get_rect(bottomright= (randint(900,1100), 300)))
                
    if game_active:             
        #draw all of our elements
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        display_score = score()
        
        # snail_rect.left -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # elif snail_rect.left >= 800: snail_rect.right = 0
        # screen.blit(snail_surface, snail_rect)
        
        #add gravity to player
        player1_grav += 1
        player1_rect.y += player1_grav
        if player1_rect.bottom >= 300: player1_rect.bottom = 300
        
        player1_rect.left += 2
        if player1_rect.right <= 0: player1_rect.left = 800
        elif player1_rect.left >= 800: player1_rect.right = 0
        screen.blit(player1_surf, player1_rect)
        
        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collision detection
        if player1_rect.colliderect(snail_rect): 
            print('collision detected')
            game_active = False
    else: #what you show when you lose the game
        screen.fill((94, 129, 169))
        screen.blit(player1_stand, player1_stand_rect)
        
        final_score = test_font.render(f'Score: {display_score}', False, 'black')
        final_score_rect = final_score.get_rect(center= (600, 200))
        
        if display_score == 0: 
            screen.blit(title_surf, title_rect)
            screen.blit(start_surf, start_rect)
        else: 
            screen.blit(final_score, final_score_rect)
        


    #updates everything
    pygame.display.update()
    clock.tick(60)