import pygame
import random



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

class Enemy(pygame.sprite.Sprite):
    '''creates game enemies'''
    def __init__(self):

        super().__init__()

        width = 60
        height = 60

        img = pygame.image.load('bezos_head.jpg')
        self.image = pygame.transform.scale(img, (width, height))

        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(100, 3000)
        self.rect.y = random.randrange(0, 100)

        path = random.randrange(1, 2)
        if path == 1:
            self.change_x = random.randrange(1, 6)
        if path == 2:
            self.change_x = random.randrange(-6, 1)

        self.change_y = 0

        self.level = None

    def update(self):
        self.calc_grav()

        self.rect.x += self.change_x


#playtform collisions sides
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            '''reset position based on the left/right of the object'''
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.jump()
            elif self.change_x < 0:
                self.rect.left = block.rect.right
                self.jump()

        '''move up/down'''
        self.rect.y += self.change_y
#playtform collisions top/bottom
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            '''stop vertical movement'''
            self.change_y = 0
#wall collisions
        block_hit_list = pygame.sprite.spritecollide(self, self.level.walls_list, False)
        for block in block_hit_list:
            '''reset position based on the left/right of the object'''
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.change_x = -self.change_x
            elif self.change_x < 0:
                self.rect.left = block.rect.right
                self.change_x = -self.change_x

    def calc_grav(self):
        '''calculates the effect of gravity'''
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        '''check to see if on ground'''
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        '''called when user hits jump button'''
        '''move down a bit to see if platform below (move down 2 pixels)'''
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        '''if ok to jump, set speed upwards'''
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    '''player controlled movement'''
    def go_left(self):
        '''called when player hits left arrow'''
        self.change_x = -6

    def go_right(self):
        '''called when player hits right arrow'''
        self.change_x = 6

    def stop(self):
        '''called when player lets off keyboard'''
        self.change_x = 0
