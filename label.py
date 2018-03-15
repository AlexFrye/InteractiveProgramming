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


pygame.init()
class Label(pygame.sprite.Sprite):
    def __init__(self, color, size, x, y, message):
        self.x = x
        self.y = y
        self.message = message

        self.font = pygame.font.Font(None, size)

        self.textSurf = self.font.render(str(message), True, color)
        self.image = pygame.Surface((x, y))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.x/2 - W/2, self.y/2 - H/2])

    def update(self, message):
        self.textSurf = self.font.render(message, 1, color)

        self.image.bilt(self.textSurf, [self.x/s2 - W/2, self.y/2 - heigh/2])

        
######################################################
"""
        #trying to add health label
        health_label = Label(RED,100,200,200,player.health)
        message_list.add(health_label)
        active_sprite_list.add(health_label)

"""
#####################################################
