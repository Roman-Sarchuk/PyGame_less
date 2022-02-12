import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cube Game")

x = 100
y = 100
wight = 40
height = 60
speed = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (111, 118, 172), (x, y, wight, height))
    pygame.display.update()

pygame.quit()
