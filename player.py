
import pygame
''' Colors '''
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
''' Screen Dimensions'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    '''Represents the player controlled object'''

    def __init__(self):
        '''consutructor function'''
        #calls parent's instructor
        super().__init__()

        '''creates an image of the player and fills it with a color
            This could aslo be an image loaded off the disk'''
        width = 40
        height = 60
        img = pygame.image.load('doge.png')
        self.image = pygame.transform.scale(img, (width, height))
        #self.image = pygame.Surface([width, height])
        #self.image.fill(WHITE)

        '''set refernce to the image rect'''
        self.rect = self.image.get_rect()

        '''set speed vector of player'''
        self.change_x = 0
        self.change_y = 0

        '''list of sprites we can bump up against'''
        self.level = None

        self.health = 100 #start with 100 health


    def subtract_health(self, value):
        """
        creating health attribute
        call subtract_health(value) to subtract value from health
        """

        self.health = self.health - value

        if self.health <=0:
            self.health = 0
            self.kill()


    def update(self):
        '''move player'''

        '''gravity'''
        self.calc_grav()

        '''move left right'''
        self.rect.x += self.change_x


        '''check for collisions'''
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            '''reset position based on the left/right of the object'''
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        '''move up/down'''
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            '''stop vertical movement'''
            self.change_y = 0

        block_hit_list = pygame.sprite.spritecollide(self, self.level.walls_list, False)
        for block in block_hit_list:
            '''reset position based on the left/right of the object'''
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right


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
