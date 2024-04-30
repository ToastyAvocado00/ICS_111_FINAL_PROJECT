import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fear-Themed Riddle Game")

RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

lives = 3
correct_answers_count = 0

riddles = [
    {
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What "
                    "am I?",
        "options": ["A. Ghost", "B. Tree", "C. Echo"],
        "answer": "C"},
    {"question": "What has keys but can't open locks?",
     "options": ["A. Piano", "B. Map", "C. Secret"],
     "answer": "A"},
    {"question": "The more you take, the more you leave behind. What am I?",
     "options": ["A. Footsteps", "B. Memories", "C. Darkness"],
     "answer": "A"},
    {"question": "What belongs to you, but other people use it more than you?",
     "options": ["A. Your name", "B. Your time", "C. Your voice"],
     "answer": "B"},
    {"question": "I have keys but no locks. I have space but no room. You can enter, but can't go outside. What am I?",
     "options": ["A. A keyboard", "B. A book", "C. A calendar"],
     "answer": "C"}
]

background_image = pygame.image.load('Nightmare_World.jpg')
background_rect = background_image.get_rect()


def display_riddle(riddle):
    screen.blit(background_image, background_rect)
    riddle_text = font.render(riddle["question"], True, RED)
    screen.blit(riddle_text, (50, 50))
    options_y = 150
    for option in riddle["options"]:
        option_text = font.render(option, True, RED)
        screen.blit(option_text, (50, options_y))
        options_y += 50


def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False


running = True
current_riddle_index = 0
while running:
    screen.fill(BLACK)
    display_riddle(riddles[current_riddle_index])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 50 <= mouse_pos[0] <= 250:
                option_clicked = (mouse_pos[1] - 150) // 50
                selected_option = riddles[current_riddle_index]["options"][option_clicked]
                if check_answer(selected_option[0], riddles[current_riddle_index]["answer"]):
                    print("Correct!")
                    correct_answers_count += 1
                    current_riddle_index += 1
                    if correct_answers_count == len(riddles):  # Check if all riddles are answered correctly
                        print("Congratulations! You've answered all riddles correctly. You win!")
                        running = False
                else:
                    print("Wrong!")
                    lives -= 1
                    if lives == 0:
                        print("Game Over!")
                        running = False
                    else:
                        print("Lives left:", lives)

    pygame.display.flip()

pygame.quit()
