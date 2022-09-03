import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        player1_walk_1 =pygame.image.load('projects\pygame_intro\graphics\Player\player_walk_1.png').convert_alpha()
        player1_walk_2 = pygame.image.load('projects\pygame_intro\graphics\Player\player_walk_2.png').convert_alpha()
        self.player_walk = [player1_walk_1, player1_walk_2]
        self.player_jump = pygame.image.load('projects\pygame_intro\graphics\Player\jump.png').convert_alpha()
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom= (200,300))
        self.gravity = 0

        # self.jump_sound = pygame.mixer.Sound('projects\\pygame_intro\\audio\\jump.mp3')
    
    def player_input(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            # self.jump_sound.play() 
            self.gravity = -20
    
    def apply_gravity(self): 
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: self.rect.bottom = 300
        
    def animation(self): 
        if self.rect.bottom < 300: 
            self.image = self.player_jump
        else: 
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()
        
class Obstacle(pygame.sprite.Sprite): 
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly': 
            fly_frame1 = pygame.image.load('projects\pygame_intro\graphics\Fly\Fly1.png').convert_alpha()
            fly_frame2 =pygame.image.load('projects\pygame_intro\graphics\Fly\Fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else: 
            # Obstacles
            snail_frame1 = pygame.image.load('projects\pygame_intro\graphics\snail\snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('projects\pygame_intro\graphics\snail\snail1.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300
            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom= (randint(900,1100), y_pos))
    
    def animations(self): 
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        self.animations()
        self.rect.x -= 6
        self.destroy()
        
    def destroy(self): 
        if self.rect.x <= -100: 
            self.kill()


def score(): 
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {time}', False, (64,64,64))
    score_rect = score_surf.get_rect(midbottom= (370, 50))
    screen.blit(score_surf, score_rect)
    return time
       
def sprite_collisions(): 
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):  #returns a list if True empty list if not
        obstacle.empty() #delets all obstacles after collision is detected
        return False
    else: 
        return True

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('projects\\pygame_intro\\font\\Pixeltype.ttf', 50)
game_active = False
start_time = 0
display_score = 0
bg_sound = pygame.mixer.Sound('projects\\pygame_intro\\audio\\music.wav')
bg_sound.play(loops= -1) #-1 tells python to loop this sound forever


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle = pygame.sprite.Group()

sky_surface = pygame.image.load('projects\pygame_intro\graphics\Sky.png').convert()
ground_surface = pygame.image.load('projects\pygame_intro\graphics\ground.png').convert()


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
            if event.type == obstacle_timer: 
                obstacle.add(Obstacle(choice(['fly', 'fly','snail', 'snail', 'snail']))) 
                           

    if game_active:             
        #draw all of our elements
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        display_score = score()
  
        player.draw(screen)
        player.update()
        
        obstacle.draw(screen)
        obstacle.update()
        
        game_active = sprite_collisions()
  
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