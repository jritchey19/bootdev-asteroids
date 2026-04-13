import pygame
import random

from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            r_angle = random.uniform(20.0, 50.0)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_asteroid = self.velocity.rotate(r_angle)
            second_asteroid = self.velocity.rotate(r_angle * -1)

            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

            asteroid_1.velocity = first_asteroid * 1.2
            asteroid_2.velocity = second_asteroid * 1.2


