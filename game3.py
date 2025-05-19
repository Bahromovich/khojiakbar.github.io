import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bouncing Ball - Gravity Falls Lofi")

# To'p parametrlar
x, y = 300, 300
radius = 20
max_radius = 100
dx, dy = 5, 4

# Audio yuklash
pygame.mixer.init()
sounds = [
    pygame.mixer.Sound("sounds/sound1.wav"),
    pygame.mixer.Sound("sounds/sound2.wav"),
    pygame.mixer.Sound("sounds/sound3.wav"),
    pygame.mixer.Sound("sounds/sound4.wav")
]
sound_index = 0  # qaysi musiqa navbatda

def play_sound():
    global sound_index
    sounds[sound_index].play()
    sound_index = (sound_index + 1) % len(sounds)

run = True
while run:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Chegaralarga tekshirish
    if x + radius >= 600:
        dx = -dx
        if radius < max_radius:
            radius += 2
            x -= 2
        play_sound()

    elif x - radius <= 0:
        dx = -dx
        if radius < max_radius:
            radius += 2
            x += 2
        play_sound()

    if y + radius >= 600:
        dy = -dy
        if radius < max_radius:
            radius += 2
            y -= 2
        play_sound()

    elif y - radius <= 0:
        dy = -dy
        if radius < max_radius:
            radius += 2
            y += 2
        play_sound()

    # Harakat
    x += dx
    y += dy

    # Ekranni chizish
    win.fill((15, 15, 25))
    pygame.draw.circle(win, (255, 100, 0), (x, y), radius)
    pygame.display.update()

pygame.quit()
