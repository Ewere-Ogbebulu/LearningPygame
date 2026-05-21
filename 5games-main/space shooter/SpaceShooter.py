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
player_rect = player.get_frect(center = (WINDOW_W /2, WINDOW_H/2))
player_direction = 1

stars = pygame.image.load(join('5games-main','space shooter','images', 'star.png')).convert_alpha()
stars_pos = [(randint(0, WINDOW_W), randint(0, WINDOW_H)) for i in range(20)]



meteor = pygame.image.load(join('5games-main','space shooter','images', 'meteor.png')).convert_alpha()
meteor_rect = meteor.get_frect(center = (WINDOW_W /2, WINDOW_H/2))

laser = pygame.image.load(join('5games-main','space shooter','images', 'laser.png')).convert_alpha()
laser_rect = laser.get_frect(bottomleft = (20,WINDOW_H -20))




while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw game
    display_surface.fill("dark grey")

    #random stars
    for pos in stars_pos:
       display_surface.blit(stars, pos)

    display_surface.blit(meteor, meteor_rect)

    display_surface.blit(laser, laser_rect)
    
    player_rect.x += player_direction *0.4
    if player_rect.right >= WINDOW_W or player_rect.left < 0:
         player_direction *= -1
    display_surface.blit(player, player_rect)
    
    


    pygame.display.update()
            

pygame.quit()