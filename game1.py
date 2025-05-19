import pygame
import random

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Collector Game")

# O'yinchi
x, y = 50, 50
player_size = 40
vel = 5

# Narsa (item)
item_size = 20
item_x = random.randint(0, 600 - item_size)
item_y = random.randint(0, 600 - item_size)

# To‘siqlar
obstacles = [
    pygame.Rect(200, 200, 100, 20),
    pygame.Rect(400, 100, 20, 100),
    pygame.Rect(100, 400, 150, 20),
]

font = pygame.font.SysFont("comicsans", 30)
score = 0

run = True
while run:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Harakat
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= vel
    if keys[pygame.K_RIGHT]: x += vel
    if keys[pygame.K_UP]: y -= vel
    if keys[pygame.K_DOWN]: y += vel

    player_rect = pygame.Rect(x, y, player_size, player_size)
    item_rect = pygame.Rect(item_x, item_y, item_size, item_size)

    # To‘siqqa tegsa — o‘yin tugaydi

    for obs in obstacles:
        if player_rect.colliderect(obs):
            print("Game Over! Tegib ketding.")
            run = False

    # Narsani yutsa:
    if player_rect.colliderect(item_rect):
        score += 1
        player_size += 2  # kvadrat kattalashadi
        item_x = random.randint(0, 600 - item_size)
        item_y = random.randint(0, 600 - item_size)

    # O‘yin tugash sharti
    if score >= 30:
        print("You Win!")
        run = False

    # Ekranni chizish
    win.fill((30, 30, 30))

    pygame.draw.rect(win, (255, 0, 0), player_rect)
    pygame.draw.rect(win, (0, 255, 0), item_rect)

    for obs in obstacles:
        pygame.draw.rect(win, (100, 100, 255), obs)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
