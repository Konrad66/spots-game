import pygame
import sys

# Inicjalizacja pygame
pygame.init()

# Ustawienia ekranu
screen = pygame.display.set_mode((800, 600))  # Rozmiar okna
pygame.display.set_caption("Moja pierwsza gra")  # Tytuł okna

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Zamknięcie okna
            running = False

    # Rysowanie na ekranie
    screen.fill(WHITE)  # Wypełnienie tła kolorem
    pygame.draw.rect(screen, RED, (200, 150, 100, 50))  # Rysowanie prostokąta

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie programu
pygame.quit()
sys.exit()
