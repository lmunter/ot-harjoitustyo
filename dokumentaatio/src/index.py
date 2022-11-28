import pygame
import os
import random

dirname = os.path.dirname(__file__)

class Pelaaja(pygame.sprite.Sprite):
    def __init__(self):
        super(Pelaaja, self).__init__()
        self.surf = pygame.image.load(os.path.join(dirname, "assets", "pelaaja.jpg"))
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()

class Alusta(pygame.sprite.Sprite):
    def __init__(self):
        super(Alusta, self).__init__()
        self.leveys = random.randint(300, 700)
        self.surf = pygame.Surface((self.leveys, 50))
        self.surf.fill((10, 10, 10))
        self.rect = self.surf.get_rect()

class Peli:
    def __init__(self):
        pygame.init()
        pelaaja = Pelaaja()
        alusta = Alusta()

        screen = pygame.display.set_mode([500, 500])

        running = True
        while running:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    running = False
                elif tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_ESCAPE:
                        running = False
            
    
            screen.fill((235, 235, 235))
            screen.blit(pelaaja.surf, pelaaja.rect)
            screen.blit(alusta.surf, alusta.rect)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Peli()