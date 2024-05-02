import pygame
import sys


def game2_function():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spot the Difference")

    image1 = pygame.image.load('forest_animals_different.png')
    image2 = pygame.image.load('forest_animals.jpg')

    image1 = pygame.transform.scale(image1, (WIDTH // 2, HEIGHT))
    image2 = pygame.transform.scale(image2, (WIDTH // 2, HEIGHT))

    clock = pygame.time.Clock()

    correct_positions = [
        (306, 533),
        (10, 463),
        (89, 160),
        (140, 212),
        (357, 341),
        (395, 410),
        (192, 165),
        (243, 208)
    ]

    CLICK_TOLERANCE = 30

    clicked_positions = []

    correct_differences = 0
    incorrect_clicks = 0

    game_over = False
    game_won = False

    def display_images():
        screen.blit(image1, (0, 0))
        screen.blit(image2, (WIDTH // 2, 0))

    def draw_circles():
        for pos in clicked_positions:
            pygame.draw.circle(screen, (255, 0, 0), pos, 10, 2)

    def check_difference(pos):
        nonlocal correct_differences, game_won, game_over, incorrect_clicks
        if pos[0] < WIDTH // 2:
            clicked_positions.append(pos)
            found_correct_difference = False
            for correct_pos in correct_positions:
                distance = pygame.math.Vector2(pos).distance_to(pygame.math.Vector2(correct_pos))
                print(f"Distance to correct position: {distance}")
                if distance < CLICK_TOLERANCE:
                    correct_differences += 1
                    found_correct_difference = True
                    break
            if not found_correct_difference:
                incorrect_clicks += 1
                if incorrect_clicks >= 5:
                    game_over = True
            if correct_differences >= 5:
                game_won = True

    def show_winning_screen():
        screen.fill((0, 255, 0))
        font = pygame.font.SysFont('forest_animals_different.png', 48)
        text = font.render("Congratulations! You found all differences!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

    def show_losing_screen():
        screen.fill((255, 0, 0))
        font = pygame.font.SysFont('forest_animals.jpg', 48)
        text = font.render("Sorry! You clicked too many incorrect areas.", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

    running = True
    while running:
        screen.fill((255, 255, 255))

        if game_won:
            show_winning_screen()
        elif game_over:
            show_losing_screen()
        else:
            display_images()
            draw_circles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_won and not game_over:
                mouse_pos = pygame.mouse.get_pos()
                check_difference(mouse_pos)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    game2_function()
