import pygame
from tiles import Tile
from settings import tile_size

class Level(): 
    def __init__(self, level_map, surface):
        # Level setup 
        self.display_surface = surface
        self.level_setup(level_map)
        self.world_shift = 0
        
    def level_setup(self, map): 
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(map): 
            for col_index, cell in enumerate(row): 
                print(f'({row_index}, {col_index}): {cell}')
                if cell == 'X': 
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
        
        
    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        
                