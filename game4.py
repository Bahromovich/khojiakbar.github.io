import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Avoid the Enemies")

# Raqamli ranglar
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

# O'yinchi
player_radius = 20
player_x = 250
player_y = 500
player_speed = 5

# Dushmanlar
enemies = []
enemy_speed = 4
enemy_width = 40
enemy_height = 40
spawn_timer = 0
score = 0
font = pygame.font.SysFont("comicsans", 30)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    win.fill(BLACK)

    # Hodisalar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # O'yinchi harakati
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_radius > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_radius < 500:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_radius > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_radius < 600:
        player_y += player_speed

    # Dushmanlarni yaratish
    spawn_timer += 1
    if spawn_timer >= 30:
        ex = random.randint(0, 460)
        ey = -enemy_height
        enemies.append(pygame.Rect(ex, ey, enemy_width, enemy_height))
        spawn_timer = 0
        score += 1  # Har yangi dushmanda 1 ochko

    # Dushmanlarni harakatlantirish
    for enemy in enemies:
        enemy.y += enemy_speed
        pygame.draw.rect(win, RED, enemy)

        # To'qnashuv tekshirish
        dist_x = abs(enemy.centerx - player_x)
        dist_y = abs(enemy.centery - player_y)
        if dist_x < enemy_width//2 + player_radius and dist_y < enemy_height//2 + player_radius:
            text = font.render("Game Over! Score: " + str(score), True, WHITE)
            win.blit(text, (100, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

    # O'yinchini chizish
    pygame.draw.circle(win, BLUE, (player_x, player_y), player_radius)

    # Score yozuv
    score_text = font.render("Score: " + str(score), True, WHITE)
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
