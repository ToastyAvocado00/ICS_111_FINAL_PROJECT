import pygame
import sys
import random


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


MAZE_WIDTH = 50 
MAZE_HEIGHT = 50  
BLOCK_SIZE = 15  
SCREEN_WIDTH = BLOCK_SIZE * MAZE_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * MAZE_HEIGHT


TIMER_DURATION = 240000  
timer_start = 0


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")


background_image = pygame.image.load("Candy_Kingdom.jpg").convert()

exit_x = None
exit_y = None


def generate_maze():
    global exit_x, exit_y
    maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]

    def create_path(x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                maze[ny][nx] = 0
                create_path(nx, ny)

    create_path(1, 1)
  
    exit_x = random.randint(MAZE_WIDTH // 2, MAZE_WIDTH - 1)
    exit_y = random.randint(MAZE_HEIGHT // 2, MAZE_HEIGHT - 1)
    while maze[exit_y][exit_x] != 0:
        exit_x = random.randint(MAZE_WIDTH // 2, MAZE_WIDTH - 1)
        exit_y = random.randint(MAZE_HEIGHT // 2, MAZE_HEIGHT - 1)
    maze[exit_y][exit_x] = 0
