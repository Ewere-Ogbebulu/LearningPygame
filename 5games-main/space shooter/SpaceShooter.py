import pygame

pygame.init()
WINDOW_W, WINDOW_H = 1280, 720
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("5games-main\space shooter\images\player.png")
pygame.display.set_icon(icon)
display_surface = pygame.display.set_mode((WINDOW_W, WINDOW_H))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("orange")

   

    pygame.display.update()
            

pygame.quit()