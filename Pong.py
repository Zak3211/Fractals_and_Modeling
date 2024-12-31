#Pong Game Made by ChatGPT

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
paddle_speed = 10
score_left = 0
score_right = 0

font = pygame.font.SysFont("Arial", 30)


left_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2


ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2


clock = pygame.time.Clock()

def draw_window():
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (20, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 20 - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Draw mid line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw scores
    score_text = font.render(f"{score_left} - {score_right}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.update()

def handle_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, score_left, score_right

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball out of bounds (scoring)
    if ball_x <= 0:
        score_right += 1
        reset_ball()
    if ball_x + BALL_SIZE >= WIDTH:
        score_left += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = WIDTH // 2 - BALL_SIZE // 2
    ball_y = HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))

def handle_paddles():
    global left_paddle_y, right_paddle_y

    # Left paddle movement (up and down)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y + PADDLE_HEIGHT < HEIGHT:
        left_paddle_y += paddle_speed

    # Right paddle movement (up and down)
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y + PADDLE_HEIGHT < HEIGHT:
        right_paddle_y += paddle_speed

def handle_collisions():
    global ball_speed_x, ball_speed_y

    # Left paddle collision
    if ball_x <= 20 + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        ball_speed_x = -ball_speed_x

    # Right paddle collision
    if ball_x + BALL_SIZE >= WIDTH - 20 - PADDLE_WIDTH and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
        ball_speed_x = -ball_speed_x

def main():
    global score_left, score_right

    # Game loop
    running = True
    while running:
        clock.tick(60)  # Set FPS to 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_ball()
        handle_paddles()
        handle_collisions()
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
