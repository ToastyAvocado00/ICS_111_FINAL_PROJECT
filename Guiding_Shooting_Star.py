import pygame
import sys
import random


def game4_function():
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

    class Asteroid:
        def __init__(self):
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = random.randint(0, SCREEN_HEIGHT)
            self.speed_x = 0
            self.speed_y = 0

        def update(self, star_x, star_y):
            dx = star_x - self.x
            dy = star_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance != 0:
                self.speed_x = dx / distance * ASTEROID_SPEED
                self.speed_y = dy / distance * ASTEROID_SPEED

            self.x += self.speed_x
            self.y += self.speed_y

        def draw(self):
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), ASTEROID_RADIUS)

    class Exit:
        def __init__(self, star_x, star_y):
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = random.randint(0, SCREEN_HEIGHT)
            self.speed_x = random.uniform(-3, 3)  # Random speed for horizontal movement
            self.speed_y = random.uniform(-3, 3)  # Random speed for vertical movement

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

            if self.x < 0 or self.x > SCREEN_WIDTH:
                self.speed_x *= -1
            if self.y < 0 or self.y > SCREEN_HEIGHT:
                self.speed_y *= -1

        def draw(self):
            pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), EXIT_RADIUS)

    star = Star()
    exit_point = Exit(star.x, star.y)
    asteroids = []
    running = True
    clock = pygame.time.Clock()
    level = 1
    won = False
    game_over = False
    asteroid_delay_counter = ASTEROID_DELAY

    while running:
        screen.fill(BLACK)

        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        if not won and not game_over:
            star.update(keys_pressed)

        if asteroid_delay_counter > 0:
            asteroid_delay_counter -= 1

        if asteroid_delay_counter > 0:
            asteroid_delay_counter -= 1

        if asteroid_delay_counter == 0:
            if len(asteroids) == 0:
                asteroids = [Asteroid() for _ in range(NUM_ASTEROIDS)]
            else:
                for asteroid in asteroids:
                    asteroid.update(star.x, star.y)
                    asteroid.draw()

                    distance_to_star = ((asteroid.x - star.x) ** 2 + (asteroid.y - star.y) ** 2) ** 0.5
                    if distance_to_star < ASTEROID_RADIUS + STAR_RADIUS:
                        print("Game over!")
                        game_over = True

        exit_point.update()
        exit_point.draw()

        distance_to_exit = ((exit_point.x - star.x) ** 2 + (exit_point.y - star.y) ** 2) ** 0.5
        if distance_to_exit < EXIT_RADIUS + STAR_RADIUS:
            print("You win!")
            won = True
            running = False

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
        clock.tick(30)

    pygame.quit()
    sys.exit()


game4_function()
