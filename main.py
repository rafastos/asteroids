import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for a in asteroids:
            if a.is_colliding(player):
                print("Game over!")
                exit(0)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds.


if __name__ == "__main__":
    main()
