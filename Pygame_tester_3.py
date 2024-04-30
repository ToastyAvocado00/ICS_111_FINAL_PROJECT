import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)  # Yellow color for the star
RED = (255, 0, 0)  # New color for the exit
STAR_RADIUS = 3
STAR_SPEED = 8  # Faster star speed
ASTEROID_RADIUS = 20
EXIT_RADIUS = 3  # Smaller exit size
NUM_STARS = 50  # Adjust the number of stars for slower background
NUM_POWERUPS = 3  # Number of power-ups in each level
NUM_ASTEROIDS = 7  # Increased number of asteroids
ASTEROID_SPEED = 4  # Faster asteroid speed
ASTEROID_DELAY = 30  # Delay before asteroids start moving (in frames)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guiding Shooting Star")


# Function to draw a starry background
def draw_starry_background():
    for _ in range(NUM_STARS):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(screen, WHITE, (x, y), 1)


# Define a Star class
class Star:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed = STAR_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), STAR_RADIUS)


# Define an Asteroid class
class Asteroid:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed_x = 0
        self.speed_y = 0

    def update(self, star_x, star_y):
        # Calculate direction towards the star
        dx = star_x - self.x
        dy = star_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Set speed based on direction
        if distance != 0:
            self.speed_x = dx / distance * ASTEROID_SPEED
            self.speed_y = dy / distance * ASTEROID_SPEED

        # Move asteroid
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), ASTEROID_RADIUS)


# Define the Exit class
class Exit:
    def __init__(self, star_x, star_y):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed_x = random.uniform(-3, 3)  # Random speed for horizontal movement
        self.speed_y = random.uniform(-3, 3)  # Random speed for vertical movement

        # Move exit far away from star
        dx = self.x - star_x
        dy = self.y - star_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        while distance < SCREEN_WIDTH / 4:  # Keep moving until exit is far enough
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = random.randint(0, SCREEN_HEIGHT)
            dx = self.x - star_x
            dy = self.y - star_y
            distance = (dx ** 2 + dy ** 2) ** 0.5

    def update(self):
        # Move exit
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off screen edges
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), EXIT_RADIUS)


# Define the Powerup class
class Powerup:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), STAR_RADIUS)


# Main game loop
star = Star()

# Initialize exit point with star's coordinates
exit_point = Exit(star.x, star.y)

powerups = [Powerup(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_POWERUPS)]
asteroids = []  # Asteroids start empty

running = True
clock = pygame.time.Clock()
level = 1
won = False  # Flag to track if the game is won
game_over = False  # Flag to track if the game is over
asteroid_delay_counter = ASTEROID_DELAY  # Counter for asteroid delay

while running:
    screen.fill(BLACK)

    draw_starry_background()  # Draw starry background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if not won and not game_over:  # Only allow movement if the game is not won and not over
        star.update(keys_pressed)

    # Update asteroid delay counter
    if asteroid_delay_counter > 0:
        asteroid_delay_counter -= 1

    if asteroid_delay_counter > 0:
        asteroid_delay_counter -= 1

    if asteroid_delay_counter == 0:
        # Once delay is over, create asteroids
        if len(asteroids) == 0:  # Check if there are no asteroids
            asteroids = [Asteroid() for _ in range(NUM_ASTEROIDS)]
        else:
            for asteroid in asteroids:
                asteroid.update(star.x, star.y)
                asteroid.draw()

                # Check for collision with star
                distance_to_star = ((asteroid.x - star.x) ** 2 + (asteroid.y - star.y) ** 2) ** 0.5
                if distance_to_star < ASTEROID_RADIUS + STAR_RADIUS:
                    print("Game over!")
                    game_over = True

    for powerup in powerups:
        powerup.draw()

    exit_point.update()
    exit_point.draw()

    # Check for collisions with power-ups
    for powerup in powerups:
        distance = ((powerup.x - star.x) ** 2 + (powerup.y - star.y) ** 2) ** 0.5
        if distance < STAR_RADIUS + STAR_RADIUS:
            print("You collected a power-up!")

    # Check if the star reached the exit
    distance_to_exit = ((exit_point.x - star.x) ** 2 + (exit_point.y - star.y) ** 2) ** 0.5
    if distance_to_exit < EXIT_RADIUS + STAR_RADIUS:
        print("You win!")
        won = True
        running = False  # Stop the game loop

    # Generate new power-ups if all are collected
    if all(distance < STAR_RADIUS + STAR_RADIUS for distance in
           [(powerup.x - star.x) ** 2 + (powerup.y - star.y) ** 2 for powerup in powerups]):
        powerups = [Powerup(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in
                    range(NUM_POWERUPS)]

    # Draw star
    star.draw()

    if won:
        font = pygame.font.Font(None, 36)
        text = font.render("You Win!", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, RED)  # Display game-over message in red
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 FPS for slower background

pygame.quit()
sys.exit()
