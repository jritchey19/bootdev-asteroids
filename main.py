import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event
from player import Player
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)
    score = 0
    score_rollover = 0
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if score >= 5000:
            player.lives += 1
            score_rollover += 5000
            score = 0

        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            for s in shots:
                if obj.collides_with(s):
                    log_event("asteroid_shot")

                    score += obj.radius

                    s.kill()
                    obj.split()

        for obj in asteroids:
            
            if obj.collides_with(player):
                if player.lives == 0:
                    final_score = score + score_rollover

                    log_event("player_hit")
                    log_event(f"player_final_score-{score}")

                    print("Game over!")
                    print(f"Final Score: {final_score}")
                    sys.exit()
                else:
                    player.lives -= 1
                    player.position = pygame.Vector2(x, y)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
