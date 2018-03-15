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

class Wall(pygame.sprite.Sprite):
    '''walls to keep player in world'''

    def __init__(self, width, height):
        super().__init__()
        #img = pygame.image.load('cloud.png')
        #self.image = pygame.transform.scale(img, (width, height))
        self.image = pygame.Surface([width, height])
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
