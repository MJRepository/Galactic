import pygame
import math
pygame.init()   #Inicjalizacja biblioteki

#Ustawienia okna wyświetlania
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #Jeżeli event wyjście to wyłącz
                run = False

    pygame.quit()   #Jeżeli kończą się eventy to kończy się progrM

main()