import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spot the Difference")

# Load images
image1 = pygame.image.load('forest_animals_different.png')
image2 = pygame.image.load('forest_animals.jpg')

# Resize images to fit half the screen
image1 = pygame.transform.scale(image1, (WIDTH // 2, HEIGHT))
image2 = pygame.transform.scale(image2, (WIDTH // 2, HEIGHT))

# Set up clock
clock = pygame.time.Clock()

# List to store correct difference positions
correct_positions = [(114, 345), (211, 140), (447, 386), (582, 241), (688, 189)]

# List to store clicked positions
clicked_positions = []

# Number of correct differences found
correct_differences = 0

# Boolean to track winning state
game_won = False


# Function to display images
def display_images():
    screen.blit(image1, (0, 0))
    screen.blit(image2, (WIDTH // 2, 0))


# Function to draw circles around differences
def draw_circles():
    for pos in clicked_positions:
        pygame.draw.circle(screen, (255, 0, 0), pos, 10, 2)


# Function to check for differences
# Function to check for differences
def check_difference(pos):
    global correct_differences, game_won
    if pos[0] < WIDTH // 2:  # Check if the click is on the left image
        clicked_positions.append(pos)
        # Check if clicked position corresponds to a correct difference
        for correct_pos in correct_positions:
            if pygame.math.Vector2(pos).distance_to(pygame.math.Vector2(correct_pos)) < 20:
                correct_differences += 1
                break
        if correct_differences >= 5:
            game_won = True
            show_winning_screen()  # Display winning screen


# Function to display winning screen
def show_winning_screen():
    screen.fill((0, 255, 0))  # Fill screen with green color
    font = pygame.font.SysFont(None, 48)
    text = font.render("Congratulations! You found all differences!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()


# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill screen with white

    if game_won:
        show_winning_screen()
    else:
        display_images()  # Display images
        draw_circles()  # Draw circles around differences

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_won:
            mouse_pos = pygame.mouse.get_pos()
            check_difference(mouse_pos)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS
