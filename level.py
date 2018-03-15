import pygame
from platform import Platform
#global constants
''' Colors '''
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
''' Screen Dimensions'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Level():
    '''generic super-class used to define a level.
    Creates a child class for each level with level specific info.'''

    def __init__(self, player):
        '''constructor. pass in a handle to player. needed for when moving
        platforms collide with player'''
        self.walls_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        '''how far this world has been scrolled left/right'''
        self.world_shift = 0

    '''update everyhting on this level'''
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.walls_list.update()

    def draw(self, screen):
        '''draw everyhting on this level'''

        '''draw background'''
        #screen.fill(BLACK)

        '''draw all the sprite lists that we have'''
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        '''when user moves left/right and we need to scroll everything'''

        '''keep track of shift amount'''
        self.world_shift += shift_x

        '''go through all the sprite lists and shift everything'''
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        '''do the same for walls and enemies'''
        for wall in self.walls_list:
            wall.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
