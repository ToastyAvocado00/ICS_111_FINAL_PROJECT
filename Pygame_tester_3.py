import pygame
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
STAR_RADIUS = 3
STAR_SPEED = 8
ASTEROID_RADIUS = 20
EXIT_RADIUS = 3
NUM_STARS = 50
NUM_POWERUPS = 3
NUM_ASTEROIDS = 7
ASTEROID_SPEED = 4
ASTEROID_DELAY = 30

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guiding Shooting Star")

background_image = pygame.image.load('Starry sky.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_starry_background():
    for _ in range(NUM_STARS):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(screen, WHITE, (x, y), 1)


class Star:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed = STAR_SPEED


