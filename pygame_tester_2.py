import pygame
import sys

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


correct_positions = [(114, 345), (211, 140), (447, 386), (582, 241), (688, 189)]

clicked_positions = []

correct_differences = 0


game_won = False



def display_images():
    screen.blit(image1, (0, 0))
    screen.blit(image2, (WIDTH // 2, 0))


# Function to draw circles around differences
def draw_circles():
    for pos in clicked_positions:
        pygame.draw.circle(screen, (255, 0, 0), pos, 10, 2)


