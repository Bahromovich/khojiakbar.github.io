import pygame
import random
import math
import time

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Click the Circles - Level Mode")

font = pygame.font.SysFont("comicsans", 30)
big_font = pygame.font.SysFont("comicsans", 50)

# Dastlabki sozlamalar
level = 1
score = 0
radius = 30
max_level = 6
circles = []
level_start_time = time.time()
level_time = 15  # 1-uroven
clicked_circles = 0

def generate_circles(n):
    circles.clear()
    for _ in range(n):
        x = random.randint(radius, 600 - radius)
        y = random.randint(radius, 600 - radius)
        circles.append({'x': x, 'y': y, 'clicked': False})

generate_circles(5)

run = True
while run:
    pygame.time.delay(30)
    current_time = time.time()
    remaining_time = int(level_time - (current_time - level_start_time))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for c in circles:
                if not c['clicked']:
                    dist = math.hypot(mx - c['x'], my - c['y'])
                    if dist <= radius:
                        c['clicked'] = True
                        score += 1
                        clicked_circles += 1

    # Ekranni tozalash
    win.fill((10, 10, 20))

    # Doiralarni chizish
    for c in circles:
        if not c['clicked']:
            pygame.draw.circle(win, (0, 200, 255), (c['x'], c['y']), radius)

    # HUD (yuqoridagi matnlar)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    time_text = font.render(f"Time Left: {max(remaining_time, 0)}s", True, (255, 255, 255))

    win.blit(score_text, (10, 10))
    win.blit(level_text, (250, 10))
    win.blit(time_text, (420, 10))

    # Vaqt tugasa yoki hamma doira bosilsa:
    if remaining_time <= 0 or clicked_circles == len(circles):
        if level < max_level:
            level += 1
            level_time = 15 + (level - 1) * 5
            generate_circles(5 + (level - 1) * 2)
            clicked_circles = 0
            level_start_time = time.time()
        else:
            # G‘alaba holati
            win.fill((0, 0, 0))
            win.blit(big_font.render("WINNER!", True, (0, 255, 0)), (200, 250))
            win.blit(font.render(f"Final Score: {score}", True, (255, 255, 255)), (220, 320))
            pygame.display.update()
            pygame.time.delay(5000)
            break

    pygame.display.update()

pygame.quit()
