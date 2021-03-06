import pygame
from level import Level
from platform import Platform
from walls import Wall
from enemy import Enemy


''' Colors '''
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
''' Screen Dimensions'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600






class Level_01(Level):
    '''defines level 1'''
    def __init__(self, player):
        '''call parent constructor'''
        Level.__init__(self, player)
        self.level_limit = -10000

        '''array with with width, height, x, and y of platform'''
        level = [[210, 70, 500, 500],
                [210, 70, 800, 400],
                [210, 70, 1120, 280],
                [210, 70, 2000, 300],
                [210, 70, 1800, 500],
                [210, 70, 2900, 400],
                ]
        walls = [[70, 600, 0, 0],
                [70, 600, 3200, 0]]


        '''go through the array and add platforms'''
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        '''do the same for level walls'''
        for wall in walls:
            block = Wall(wall[0], wall[1])
            block.rect.x = wall[2]
            block.rect.y = wall[3]
            block.player = self.player
            self.walls_list.add(block)

        '''add enemies to level'''
        self.enemy_list.add(Enemy())
        self.enemy_list.add(Enemy())
