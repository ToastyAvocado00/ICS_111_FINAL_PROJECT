import pygame
import sys
import random

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Define maze parameters
MAZE_WIDTH = 50  # Increased maze width
MAZE_HEIGHT = 50  # Increased maze height
BLOCK_SIZE = 15  # Decreased block size
SCREEN_WIDTH = BLOCK_SIZE * MAZE_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * MAZE_HEIGHT

# Timer variables
TIMER_DURATION = 240000  # 30 seconds in milliseconds
timer_start = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Load background image
background_image = pygame.image.load("Candy_Kingdom.jpg").convert()

# Initialize exit position
exit_x = None
exit_y = None


# Generate maze using recursive backtracking algorithm
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
    # Set exit area far away from the start
    exit_x = random.randint(MAZE_WIDTH // 2, MAZE_WIDTH - 1)
    exit_y = random.randint(MAZE_HEIGHT // 2, MAZE_HEIGHT - 1)
    while maze[exit_y][exit_x] != 0:
        exit_x = random.randint(MAZE_WIDTH // 2, MAZE_WIDTH - 1)
        exit_y = random.randint(MAZE_HEIGHT // 2, MAZE_HEIGHT - 1)
    maze[exit_y][exit_x] = 0  # Set exit area

    return maze


# Function to draw the maze
def draw_maze(maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))  #
                # Draw thinner black lines
            elif maze[y][x] == 0 and x == exit_x and y == exit_y:  # Draw exit position
                pygame.draw.rect(screen, GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


# Function to draw the player character
def draw_player(player_pos):
    pygame.draw.circle(screen, RED,
                       (player_pos[0] * BLOCK_SIZE + BLOCK_SIZE // 2, player_pos[1] * BLOCK_SIZE + BLOCK_SIZE // 2),
                       BLOCK_SIZE // 4)


# Function to check if the game timer has expired
def is_game_over():
    return pygame.time.get_ticks() - timer_start >= TIMER_DURATION


# Main game loop
def main():
    global timer_start
    maze = generate_maze()
    player_pos = [1, 1]
    timer_start = pygame.time.get_ticks()  # Start the timer

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player_pos[1] > 0 and maze[player_pos[1] - 1][player_pos[0]] == 0:
                        player_pos[1] -= 1
                elif event.key == pygame.K_DOWN:
                    if player_pos[1] < MAZE_HEIGHT - 1 and maze[player_pos[1] + 1][player_pos[0]] == 0:
                        player_pos[1] += 1
                elif event.key == pygame.K_LEFT:
                    if player_pos[0] > 0 and maze[player_pos[1]][player_pos[0] - 1] == 0:
                        player_pos[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    if player_pos[0] < MAZE_WIDTH - 1 and maze[player_pos[1]][player_pos[0] + 1] == 0:
                        player_pos[0] += 1

        # Draw background image
        screen.blit(background_image, (0, 0))

        # Draw maze and player
        draw_maze(maze)
        draw_player(player_pos)

        # Check if the game is over
        if is_game_over():
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over!", True, RED)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Pause for 2 seconds before quitting
            pygame.quit()
            sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
