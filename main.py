# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# imports all the constant values
from constants import *

from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # sets screen to black using tuple of rgb

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000 # converts milliseconds to seconds

if __name__ == "__main__":
    main()
