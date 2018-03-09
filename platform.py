import pygame
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


class Platform(pygame.sprite.Sprite):
    '''platform the player can jump on'''

    def __init__(self, width, height):
        '''platform constructor. Assumes constructed with user passing in an array of
        five numbers like what is defined at the top of this code'''
        super().__init__()
        img = pygame.image.load('cloud.png')
        self.image = pygame.transform.scale(img, (width, height))
        #self.image = pygame.Surface([width, height])
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
