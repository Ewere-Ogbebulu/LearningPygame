import pygame
from random import randint
from os.path import join

# Display Setup
pygame.init()
WINDOW_W, WINDOW_H = 1280, 720
pygame.display.set_caption("Space Shooter")
player_path = pygame.image.load(join('5games-main','space shooter','images', 'player.png'))
icon = player_path
pygame.display.set_icon(icon)

display_surface = pygame.display.set_mode((WINDOW_W, WINDOW_H))
running = True

SURF_W, SURF_H = 100, 200

# surface setup
surf = pygame.Surface((SURF_W, SURF_H))
surf.fill("green")
x =100

#Player /image
player = player_path.convert_alpha()

#Stars image

stars = pygame.image.load(join('5games-main','space shooter','images', 'star.png')).convert_alpha()

#meteor

meteor = pygame.image.load(join('5games-main','space shooter','images', 'meteor.png')).convert_alpha()





while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw game
    display_surface.fill("dark grey")

    
    x += 0.6
    display_surface.blit(player, (x, 100))


    #random stars
    for i in range(20):
        rand_x = randint(0, WINDOW_W)
        rand_y = randint(0, WINDOW_H)
        display_surface.blit(stars, (rand_x, rand_y))
   
    
        
    pygame.display.update()
            

pygame.quit()