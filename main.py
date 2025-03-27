from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('image\icon.png')
pygame.display.set_icon(icon)

target_image = pygame.image.load('image\Мишень.png')
target_width = 80
target_heidth = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_heidth)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_heidth:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_heidth)


    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()