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
            
            if rectangles.bottom == 300: screen.blit(snail_surface, rectangles)
            else: screen.blit(fly_surf, rectangles)
            #check if obstacles are off screen and copy obstacle if not otherwise do not copy it
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: 
        return []

def collisions(player, enemies): 
    if enemies: 
        for enemy_rect in enemies: 
            if player.colliderect(enemy_rect): return False
    return True
            
def player_animation(): 
    global player1_surf, player_index
    if player1_rect.bottom < 300: 
        #display jump surface when not on floor
        player1_surf = player_jump
    else: 
        #play walking animation on floor
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player1_surf = player_walk[int(player_index)]
    

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
snail_frame1 = pygame.image.load('projects\pygame_intro\graphics\snail\snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('projects\pygame_intro\graphics\snail\snail1.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snails_index = 0

fly_frame1 = pygame.image.load('projects\pygame_intro\graphics\Fly\Fly1.png').convert_alpha()
fly_frame2 =pygame.image.load('projects\pygame_intro\graphics\Fly\Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
flies_index = 0

snail_surface = snail_frames[snails_index]
fly_surf = fly_frames[flies_index]

obstacle_rect_list = []

player1_walk_1 =pygame.image.load('projects\pygame_intro\graphics\Player\player_walk_1.png').convert_alpha()
player1_walk_2 = pygame.image.load('projects\pygame_intro\graphics\Player\player_walk_2.png').convert_alpha()
player_walk = [player1_walk_1, player1_walk_2]
player_jump = pygame.image.load('projects\pygame_intro\graphics\Player\jump.png').convert_alpha()
player_index = 0


player1_surf = player_walk[player_index]
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

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_anime_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_anime_timer, 500)

fly_anime_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_anime_timer, 200)

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
                start_time = int(pygame.time.get_ticks() / 1000)
                
    if game_active:             
        if event.type == obstacle_timer and game_active: 
            print('test')
            if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright= (randint(900,1100), 300)))
            else: 
                obstacle_rect_list.append(fly_surf.get_rect(bottomright= (randint(900,1100), 200)))
        #creates animation for snails and flies
        if event.type == snail_anime_timer: 
            if snails_index == 0: snails_index = 1
            else: snails_index = 0
            snail_surface = snail_frames[snails_index]
            
        if event.type == fly_anime_timer: 
            if flies_index == 0: flies_index = 1
            else: flies_index = 0
            fly_surf = fly_frames[flies_index]

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
        player_animation()
        screen.blit(player1_surf, player1_rect)
        
        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collision detection
        game_active = collisions(player1_rect, obstacle_rect_list)
        
        
    else: #what you show when you lose the game
        screen.fill((94, 129, 169))
        screen.blit(player1_stand, player1_stand_rect)
        obstacle_rect_list.clear()
        player1_rect.midbottom = (80, 300)
        player1_grav = 0
        
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