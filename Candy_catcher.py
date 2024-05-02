def game1_function(screen, clock):
    import pygame
    import random

    WIDTH, HEIGHT = 1000, 800
    background = pygame.image.load("Candy_Kingdom.jpg")
    basket_image = pygame.transform.scale(pygame.image.load("Empty-straw-basket-Decorative-rural-car-Graphics"
                                                            "-40617431-1"
                                                            "-1-580x387.png"), (60, 60))
    candy_image = pygame.transform.scale(pygame.image.load("CANDY.jpg"), (40, 40))
    evil_candy_image = pygame.transform.scale(pygame.image.load("evil candy.png"), (40, 40))

    basket_size = 70
    basket_x = WIDTH // 3 - basket_size // 3
    basket_y = HEIGHT - basket_size
    basket_speed = 10
    candy_size = 40
    candy_speed = 5
    evil_candy_speed = 5
    obstacle_speed = 3

    candies = []
    evil_candies = []
    obstacles = []
    score = 0

    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        basket_x = max(0, min(WIDTH - basket_size, basket_x))

        if random.randint(0, 100) < 1:
            candies.append(pygame.Rect(random.randint(0, WIDTH - candy_size), -candy_size, candy_size, candy_size))

        if random.randint(0, 200) < 1:
            evil_candies.append(pygame.Rect(random.randint(0, WIDTH - candy_size), -candy_size, candy_size, candy_size))

        for candy in candies[:]:
            candy.y += candy_speed
            screen.blit(candy_image, candy)
            if candy.colliderect(pygame.Rect(basket_x, basket_y, basket_size, basket_size)):
                candies.remove(candy)
                score += 1

        for evil_candy in evil_candies[:]:
            evil_candy.y += evil_candy_speed
            screen.blit(evil_candy_image, evil_candy)
            if evil_candy.colliderect(pygame.Rect(basket_x, basket_y, basket_size, basket_size)):
                evil_candies.remove(evil_candy)
                running = False
                break

        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            screen.blit(evil_candy_image, obstacle)

        screen.blit(basket_image, (basket_x, basket_y))

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if score >= 20:
            win_text = font.render("You Win!", True, (255, 255, 255))
            screen.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2))
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
