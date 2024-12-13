import pygame
import sys


def main():
    pygame.init()
    surface = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Spots Game")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
