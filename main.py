import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

player_image = pygame.image.load('../pythonProject2/sprite.png').convert_alpha()
player_rect = player_image.get_rect(center =(WIDTH // 2, HEIGHT // 2))
speed = 6

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Jump')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed


    screen.fill((128, 128, 128))
    screen.blit(player_image, player_rect)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()