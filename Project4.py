"""
Project 4
Sample Stuff
"""


import pygame

screen_width = 480
screen_height = 480
red = (255, 0, 0)
black = (0,0,0)


"""
define class for player
    add gravity
    add keyboard controls
"""



class Player(pygame.sprite.Sprite):
    """
    Makes a player object that:
        Responds to gravity
        Moves according to user input
    """
    def __init__(self):
        super().__init__()

        #defines filled block
        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(red)

        #makes the brick into a rectangle
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

    def update(self):
        #moves Player
        self.gravity()
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        print(self.rect.x, self.rect.y)

    def gravity(self):
        #defines gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
             self.change_y += 0.35

        if self.rect.y > = screen_height - self.rect.height and self.change_y > =0:
            self.change_y = 0
            self.rect_y = screen_height -self.rect.height

    def left(self):
        #move left
        self.change_x = -7
    def right(self):
        #move right
        self.change_x = 7
    def jump(self):
        #move up
        self.change_y = -10

    def stop(self):
        #no keyboard input
        self.change_x = 0


def main():
    pygame.init()

    #defines screen size
    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    #instantiates a player object and adds it to a group of sprites
    player = Player()
    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)

    #end condition  - ensures looping
    done = False

    #ensures framerate
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            #if event.type == pygame.QUIT():
            #    done = True
            if event.type == pygame.KEYDOWN:
                #if a key is pressed, call the approiate action
                if event.key == pygame.K_LEFT:
                    player.left()
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                #if the key is released, stop the player
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        screen.fill(black) #overwrite the screen
        active_sprite_list.update() #update the sprites
        active_sprite_list.draw(screen) #draw the sprites
        clock.tick(60) #max framerate = 60fps
        pygame.display.update() #update the display
        #pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
