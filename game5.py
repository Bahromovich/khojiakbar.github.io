import pygame
import random

pygame.init()

# Oynaning o'lchami
WIDTH, HEIGHT = 400, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moshina O'yini")

# Ranglar
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (50, 50, 50)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

# O'yinchi moshinasi
player_width, player_height = 50, 100
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Moshinalar
car_width, car_height = 50, 100

# 7 qator uchun y koordinatalari (yo'l qismi)
lanes = [i * (HEIGHT // 7) for i in range(7)]

# Font
font = pygame.font.SysFont(None, 36)

def draw_player(x, y):
    pygame.draw.rect(win, GREEN, (x, y, player_width, player_height))

def draw_car(car):
    pygame.draw.rect(win, RED, (car['x'], car['y'], car_width, car_height))

def collision(rect1, rect2):
    return rect1.colliderect(rect2)

def add_cars(cars):
    # Har bir qatorda faqat bitta moshina paydo bo'lishi uchun
    for lane_y in lanes:
        lane_has_car = any(car['lane'] == lane_y for car in cars)
        if not lane_has_car:
            if random.random() < 0.4:
                car_x = random.randint(0, WIDTH - car_width)
                car = {'x': car_x, 'y': -car_height, 'lane': lane_y}
                cars.append(car)

def move_cars(cars, speed):
    score = 0
    for car in cars[:]:
        car['y'] += speed
        if car['y'] > HEIGHT:
            cars.remove(car)
            score += 1
    return score

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))

def draw_restart_button():
    button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 40, 120, 50)
    pygame.draw.rect(win, BLUE, button_rect)
    text = font.render("Restart", True, WHITE)
    win.blit(text, (button_rect.x + 20, button_rect.y + 10))
    return button_rect

def game_over_screen(score):
    win.fill(BLACK)
    over_text = font.render("O'YIN TUGADI!", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 50))
    win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    restart_button = draw_restart_button()
    pygame.display.update()
    return restart_button

def main():
    car_speed = 3
    speed_increase_time = 5000
    last_speed_increase = pygame.time.get_ticks()

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    cars = []
    score = 0
    run = True
    game_over = False

    while run:
        clock.tick(60)
        win.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if restart_button.collidepoint(mouse_pos):
                        # Restart qilinganida o'yinni qayta boshlaymiz
                        car_speed = 3
                        last_speed_increase = pygame.time.get_ticks()
                        cars = []
                        score = 0
                        player_rect.x = player_x
                        game_over = False

        if not game_over:
            current_time = pygame.time.get_ticks()
            if current_time - last_speed_increase > speed_increase_time:
                car_speed += 1
                last_speed_increase = current_time

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_rect.left > 0:
                player_rect.x -= player_speed
            if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
                player_rect.x += player_speed

            if len(cars) < 20 and random.randint(1, 60) == 1:
                add_cars(cars)

            score += move_cars(cars, car_speed)

            for lane_y in lanes:
                pygame.draw.line(win, WHITE, (0, lane_y), (WIDTH, lane_y), 2)

            draw_player(player_rect.x, player_rect.y)

            for car in cars:
                draw_car(car)
                car_rect = pygame.Rect(car['x'], car['y'], car_width, car_height)
                if collision(player_rect, car_rect):
                    game_over = True
                    break

            draw_score(score)

        else:
            restart_button = game_over_screen(score)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
