import pygame
from tiles import Tile
from settings import tile_size, WIDTH
from player import Player

class Level(): 
    def __init__(self, level_map, surface):
        # Level setup 
        self.display_surface = surface
        self.level_setup(level_map)
        self.world_shift = 0
        
    def level_setup(self, map): 
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(map): 
            for col_index, cell in enumerate(row): 
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == 'X': 
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P': 
                    player_1 = Player((x, y))
                    self.player.add(player_1)
        
    def scroll_x(self): 
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < WIDTH / 4 and direction_x < 0: 
            self.world_shift = 8
            player.speed = 0  
        elif player_x > WIDTH - (WIDTH / 4) and direction_x > 0: 
            self.world_shift = -8
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 8  
        
    def run(self):
        
        # Level Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        # Player
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
        
        
                