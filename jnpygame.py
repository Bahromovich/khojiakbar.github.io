#pygame — bu Python dasturlash tilida 2D o‘yinlar yaratish uchun mo‘ljallangan mashhur kutubxona. 
#U boshlovchilar uchun juda qulay va oson o‘rganiladi, lekin shunga qaramay, murakkab o‘yinlar qilishga ham imkon beradi.
"""
pygame haqida asosiy ma’lumotlar:

✅ Nima uchun pygame? 
Oson o‘rnatiladi va foydalaniladi

Python asosida ishlaydi (yani sizga Pythonni bilish kifoya)

Ko‘p platformali (Windows, Linux, macOS)

Yengil grafik interfeys

2D o‘yinlar uchun yetarli tezlikda


"""
# pip install pygame --- pygame ni o'tqazish

#kichkina o'yin
import pygame
import sys
import random
#in the middle for the form of the legacy of theese words come with the most of the grade
# Dastlabki sozlamalar
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame FPC Shooter")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
telegram bot, pygame, tkinter
# Ranglar
black = (0,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# O'yinchi holati
player_pos = [400, 300]
player_speed = 5
#def crosshair in the background in the fucntion of the worlds most the advance for the IT elements of the course we will make of the under grade for the mobile version of this to the tools around this would be carefully thing

# Crosshair chizish
def draw_crosshair():
    cx, cy = 400, 300
    pygame.draw.line(screen, WHITE, (cx - 10, cy), (cx + 10, cy), 2)
    pygame.draw.line(screen, WHITE, (cx, cy - 10), (cx, cy + 10), 2)

# Dushmanlar
enemies = []
for _ in range(5):
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    enemies.append(pygame.Rect(x, y, 40, 40))

# O'yin sikli
while True:
    screen.fill(BLACK)

    # Hodisalar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # O‘q otish
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            crosshair = pygame.Rect(395, 295, 10, 10)
            for enemy in enemies[:]:
                if crosshair.colliderect(enemy):
                    enemies.remove(enemy)

    # Tugmalar holati
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]: player_pos[1] -= player_speed
    if keys[pygame.K_d]: player_pos[1] += player_speed
    if keys[pygame.K_s]: player_pos[0] -= player_speed
    if keys[pygame.K_f]: player_pos[0] += player_speed

    # Dushmanlarni chizish
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # HUD / crosshair
    draw_crosshair()

    # Foydalanuvchi holati
    pos_text = pygame.font.SysFont(None, 24).render(f"Pos: {player_pos}", True, WHITE)
    screen.blit(pos_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)