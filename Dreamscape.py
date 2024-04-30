import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dreamscape")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

current_state = "Transition"
transition_duration = 3000
transition_timer = 0
transition_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


def display_intro(image_path, text):
    intro_img = pygame.image.load(image_path)
    intro_img = pygame.transform.scale(intro_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.blit(intro_img, (0, 0))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    pygame.time.delay(5000)


def display_transition(text, image_path):
    transition_img = pygame.image.load(image_path)
    transition_img = pygame.transform.scale(transition_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(transition_img, (0, 0))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    pygame.time.delay(transition_duration)


def enchanted_forest():
    screen.fill(WHITE)
    pygame.display.flip()
    # Add logic for enchanted forest gameplay here


def nightmare_world():
    screen.fill(BLACK)
    pygame.display.flip()
    # Add logic for nightmare world gameplay here


def celestial_sky():
    screen.fill(WHITE)
    pygame.display.flip()
    # Add logic for celestial sky gameplay here


class JigsawPuzzle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((self.screen_width, self.screen_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, RED, (100, 100, 200, 200))
        pygame.draw.rect(self.image, BLUE, (350, 100, 200, 200))

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class MazeGame:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((self.screen_width, self.screen_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, BLACK, (50, 50, 300, 200))
        pygame.draw.rect(self.image, BLACK, (400, 50, 300, 200))
        pygame.draw.rect(self.image, BLACK, (50, 300, 300, 200))
        pygame.draw.rect(self.image, BLACK, (400, 300, 300, 200))

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class FearRiddle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((self.screen_width, self.screen_height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        font = pygame.font.Font(None, 36)
        text = font.render("What has keys but can't open locks?", True, WHITE)
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.image.blit(text, text_rect)

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class ConstellationGame:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((self.screen_width, self.screen_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        pygame.draw.circle(self.image, WHITE, (self.screen_width // 2, self.screen_height // 2), 100)
        pygame.draw.circle(self.image, BLACK, (self.screen_width // 2 - 50, self.screen_height // 2 - 50), 10)
        pygame.draw.circle(self.image, BLACK, (self.screen_width // 2 + 50, self.screen_height // 2 - 50), 10)

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    intro_image_path = "Dreamscape_intro.jpg"
    intro_text = "Welcome to Dreamscape! Press any key to begin..."
    display_intro(intro_image_path, intro_text)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_state == "Transition":
            if transition_timer >= transition_duration:
                if current_state == "Enchanted Forest":
                    display_transition("Entering Enchanted Forest...", "Enchanted_Forest.jpg")
                    current_state = "Enchanted Forest"
                elif current_state == "Nightmare World":
                    display_transition("Entering Nightmare World...", "Nightmare_World.jpg")
                    current_state = "Nightmare World"
                elif current_state == "Celestial Sky":
                    display_transition("Entering Celestial Sky...", "Celestial_Sky.jpg")
                    current_state = "Celestial Sky"
                transition_timer = 0
            else:
                screen.fill(BLACK)
                pygame.display.flip()
                transition_timer += clock.get_rawtime()

        elif current_state == "Enchanted Forest":
            enchanted_forest()
        elif current_state == "Nightmare World":
            nightmare_world()
        elif current_state == "Celestial Sky":
            celestial_sky()

        pygame.display.flip()

pygame.quit()
