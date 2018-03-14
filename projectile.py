
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

import random

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, v_foward, v_down):
        """
        x,y are initial sprite position
        v_foward is x velocity
        """
        super().__init__()
        self.image = pygame.Surface([ 10, 10])
        self.image.fill(RED)


        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.v_foward = v_foward
        self.v_down = v_down


    def update(self):
        """dropping bullet
        Randomly generates it across the top of the screen"""

        self.rect.x += self.v_foward
        self.rect.y += self.v_down

        #kill if goes off screen
        if self.rect.bottom < 0:
            self.kill()

    def gravity(self):
        '''calculates the effect of gravity'''
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

'''

projectile_list = pygame.sprite.Group()

Add to keypressed event for creating and shooting bullet:

if event.key == pygame.K_SPACE:
    bullet = Projectile(player.rect.x, player.rect.y, 12, 0)
    active_sprite_list.add(bullet)
    projectile_list.add(bullet)


OR

import random

projectile = Projectile(random.randrange(SCREEN_WIDTH - self.rect.width), self.rect.y = random.randrange(1,5), 0, random.randrange(1,8))
active_sprite_list.add(projectile)
projectile_list.add(projectile)



CHECK TO SEE IF PROJECTILE HIT PLAYER:

hits = pygame.sprite.spritecollide(player,projectile_list, False)
if hits:
    player.subtract_health(10)


if player.subtract_health(0) = 0:  # not necessary since self.kill() is already in the player.subtract_health, might want to use this for some sort of "you lost" message
    done = True
'''
