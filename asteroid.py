import pygame
import random

from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        random_angle = random.uniform(20, 50)

        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(-random_angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_rad)
        a1.velocity = vec1 * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_rad)
        a2.velocity = vec2 * 1.2
