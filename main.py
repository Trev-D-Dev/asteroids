# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# imports all the constant values
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # sets screen to black using tuple of rgb
        pygame.display.flip()

if __name__ == "__main__":
    main()
