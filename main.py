# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# imports all the constant values
from constants import *

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    a_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # sets screen to black using tuple of rgb

        for item in updatable:
            item.update(dt)

        for item in asteroids:
            if(item.check_collision(player)):
                print("Game Over!")
                raise SystemExit()

        for a in asteroids:
            for s in shots:
                if(a.check_collision(s)):
                    s.kill()
                    a.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000 # converts milliseconds to seconds

if __name__ == "__main__":
    main()
