import pygame
import random
from player import Player
from background import Background
from platform import Platform
from level import Level
from level_01 import Level_01
from level_02 import Level_02
from projectile import Projectile
from walls import Wall
from enemy import Enemy



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




#pygame.init()

"""

def text_object(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.SysFont(None, 120)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    main()
"""

def text(text):
    font = pygame.font.Font(None, 120)
    text = font.render(text, 1, (0,0,0))
    text_box = text.get_rect(centerx = DISPLAYSURF.get_width()/2)
    background.bilt(text, text_box)

def main():
    '''main program'''
    pygame.init()

    #setting up font

    #set height and width of the screen'''
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Side-Scrollin Platformer')
    BackGround = Background('shinning-stars-space-background.jpg', [0, 0])
    #create the player'''
    player = Player()
    #crate levels'''
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    #set current level'''
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)


    #bad guys
    enemyList = pygame.sprite.Group()
    for level in level_list:
        level.enemy_list.add(Enemy())
        level.enemy_list.add(Enemy())
        level.enemy_list.add(Enemy())
        level.enemy_list.add(Enemy())
        level.enemy_list.add(Enemy())
        for enemy in level.enemy_list:
            active_sprite_list.add(enemy)
            enemyList.add(enemy)
            enemy.level = current_level







    #loop until the user clicks close button'''
    done = False
    #used to manage how fast the screen updates'''
    clock = pygame.time.Clock()

    projectile_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()




    #MAIN GAME LOOP'''
    while not done:
        screen.fill(WHITE)
        screen.blit(BackGround.image, BackGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                    player.jump()
                    #player.subtract_health(3)
                    #message_display(player.health)
                    #text(player.health)
                    #print (player.health)

                if event.key == pygame.K_SPACE:
                    bullet = Projectile(player.rect.x, player.rect.y, 12, 0)
                    active_sprite_list.add(bullet)
                    bullet_list.add(bullet)



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()


        #hit test between bullets and enemies
        pygame.sprite.groupcollide(bullet_list, enemyList, True, True)



        #dropping projectiles

        odds_of_drop = random.randint(1,100)
        if odds_of_drop <5:
            projectile = Projectile(random.randrange(SCREEN_WIDTH), random.randrange(1,5), 0, random.randrange(5,8))
            active_sprite_list.add(projectile)
            projectile_list.add(projectile)

        hits = pygame.sprite.spritecollide(player,projectile_list, True)
        if hits:
            player.subtract_health(1)
            #projectile_list.remove(projectile)
            print("hit")
            print(player.health)
            #projectile.kill()


    #update player'''
        active_sprite_list.update()
    #update items in the level'''
        current_level.update()
    #if player gets near the right side, shift the world left (-x)'''
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
    #if player gets near the left side, shift the world right(+x)'''
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
    #if the player gets to the end of the level, go to next level'''
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

    #all code to draw should go below this comment'''
        current_level.draw(screen)
        active_sprite_list.draw(screen)
    #all code to draw should go above this comment'''

    #limt to 6o fps'''
        clock.tick(60)

    #go ahead and update the screen with what weve drawn'''
        pygame.display.flip()

#be IDLE friendly. if you foget this line program will hang on exit'''
    pygame.quit()
if __name__ == '__main__':
    main()
