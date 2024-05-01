import pygame

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
        "answer": "C"
    },
    {
        "question": "What has keys but can't open locks?",
        "options": ["A. Piano", "B. Map", "C. Secret"],
        "answer": "A"
    },
    {
        "question": "The more you take, the more you leave behind. What am I?",
        "options": ["A. Footsteps", "B. Memories", "C. Darkness"],
        "answer": "A"
    },
    {
        "question": "What belongs to you, but other people use it more than you?",
        "options": ["A. Your name", "B. Your time", "C. Your voice"],
        "answer": "B"
    },
    {
        "question": "I have keys but no locks. I have space but no room. You can enter, but can't go outside. What am "
                    "I?",
        "options": ["A. A keyboard", "B. A book", "C. A calendar"],
        "answer": "C"
    }
]
