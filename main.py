
"""
Main entry point for the Asteroids game.
"""

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # Initialize pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create game objects and groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up containers for sprites
    Shot.containers = (shots, updatable, drawable)
    updatable.add(player)
    drawable.add(player)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)

        # Collision detection
        for a in asteroids:
            for s in shots:
                if a.is_colliding(s):
                    a.split()
                    s.kill()
            if a.is_colliding(player):
                print("Game over!")
                exit(0)

        # Draw all drawable objects
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds.



if __name__ == "__main__":
    main()
