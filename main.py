import pygame
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from logger import *
import sys
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, drawable, updatable)
    Shot.containers = (shots, drawable, updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")


        updatable.update(dt)
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        log_state()

  
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
