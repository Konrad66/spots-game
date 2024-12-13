import pygame
import sys

from pygame import Color
import random

pygame.init()
surface = pygame.display.set_mode((800, 600))

roll_dice = pygame.image.load("assets/images/rollDice.png")
roll_dice = pygame.transform.scale(roll_dice, (100, 100))

command1 = pygame.image.load("assets/images/command1.png")
command1 = pygame.transform.scale(command1, (250, 150))
command2 = pygame.image.load("assets/images/command2.png")
command2 = pygame.transform.scale(command2, (250, 150))

dice2 = pygame.image.load("assets/images/dice2.png")
dice2 = pygame.transform.scale(dice2, (80, 80))

def create_dice_list():
    dice_list = []
    for i in range(6):
        dice = pygame.image.load(f"assets/images/dice{i+1}.png")
        dice = pygame.transform.scale(dice, (80, 80))
        dice_list.append(dice)
    return dice_list

dice_list = create_dice_list()

print(dice_list)
x = 350
y = 300
roll_dice_rect = roll_dice.get_rect()
roll_dice_rect.topleft = (x, y)

pygame.display.set_caption("Spots Game")
random_number = 0

mod_1 = 0
mod_2 = 0
velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_dice_rect.collidepoint(event.pos):
                random_number = random.randint(0, 5)
                mod_1 = random.randint(-5, 5)
                mod_2 = random.randint(-5, 5)
                roll_dice_rect.topleft = (x + mod_1, y + mod_2)
        surface.fill(Color('antiquewhite2'))
        surface.blit(dice_list[random_number], (350 + mod_2, 150 + mod_1))
        surface.blit(roll_dice, roll_dice_rect)  # Rysowanie obrazka na ekranie
        surface.blit(command1, (100,50))
        surface.blit(command2, (370,50))


        pygame.display.flip()

pygame.quit()
sys.exit()