import pygame

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

x, y = 300, 200
radius = 30
speed = 5

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 255), (x, y), radius)
    pygame.display.update()

pygame.quit()






