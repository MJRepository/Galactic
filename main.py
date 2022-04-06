import pygame
import math
pygame.init()

# Ustawienia okna wyświetlania
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)

def main():

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)                  # Ilość klatek na sekundę
        WIN.fill(WHITE)                 # Co pętla czyszczenie ekranu
        pygame.display.update()         # Co pętla aktualizacja ekranu

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Jeżeli event wyjście to wyłącz
                run = False

    pygame.quit()   # Jeżeli kończą się eventy to kończy się program

main()