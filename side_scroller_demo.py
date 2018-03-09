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
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)

        '''set refernce to the image rect'''
        self.rect = self.image.get_rect()

        '''set speed vector of player'''
        self.change_x = 0
        self.change_y = 0

        '''list of sprites we can bump up against'''
        self.level = None

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

class Platform(pygame.sprite.Sprite):
    '''platform the player can jump on'''

    def __init__(self, width, height):
        '''platform constructor. Assumes constructed with user passing in an array of
        five numbers like what is defined at the top of this code'''
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

class Level():
    '''generic super-class used to define a level.
    Creates a child class for each level with level specific info.'''

    def __init__(self, player):
        '''constructor. pass in a handle to player. needed for when moving
        platforms collide with player'''
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        '''how far this world has been scrolled left/right'''
        self.world_shift = 0

    '''update everyhting on this level'''
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        '''draw everyhting on this level'''

        '''draw background'''
        screen.fill(BLACK)

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

class Level_01(Level):
    '''defines level 1'''
    def __init__(self, player):
        '''call parent constructor'''
        Level.__init__(self, player)
        self.level_limit = -1000

        '''array with with width, height, x, and y of platform'''
        level = [[210, 70, 500, 500],
                [210, 70, 800, 400],
                [210, 70, 1000, 500],
                [210, 70, 1120, 280],
                ]

        '''go through the array and add platforms'''
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

def main():
    '''main program'''
    pygame.init()

    #set height and width of the screen'''
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Side-Scrollin Platformer')
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

    #loop until the user clicks close button'''
    done = False
    #used to manage how fast the screen updates'''
    clock = pygame.time.Clock()

    #MAIN GAME LOOP'''
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

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
