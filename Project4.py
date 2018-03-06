"""
Project 4
Sample Stuff
"""


import pygame

screen_width = 480
screen_height = 480
red = (255, 0, 0)


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

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

    def update(self):
        #moves Player
        self.gravity()
        self.rect.x += self.change_x
        self.rect.y += self.change_y
    def gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else self.change_y += 0.35

        if self.rect.y >= screen_height - self.rect.height and self.change_y>=0:
            self.change_y = 0
            self.rect_y = screen_height -slef.rect.height
    def left(self):
        self.change_x = -5
    def right(self):
        self.change_x = 5
    def jump(self):
        self.change_y = -10

    def stop(self):
        #no keyboard input
        self.change_x = 0


def main():
    pygame.init()
    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    player = Player()

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left()
            if event.key == pygame.K_RIGHT:
                player.right()
            if event.key == pygame.K_UP:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
