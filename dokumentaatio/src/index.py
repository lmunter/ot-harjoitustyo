import pygame
import os
import random

dirname = os.path.dirname(__file__)

class Pelaaja(pygame.sprite.Sprite):
    def __init__(self):
        super(Pelaaja, self).__init__()
        self.image = os.path.join(dirname, "assets", "pelaaja.jpg")
        self.surf = pygame.image.load(self.image)
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 50
        self.rect.y = 980
    
    def hyppy(self):
        hyppy = True
        while hyppy:
            while self.rect.y > 780:
                self.rect.y -= 1
            hyppy = False

class Alusta(pygame.sprite.Sprite):
    def __init__(self):
        super(Alusta, self).__init__()
        self.leveys = random.randint(1300, 1700)
        self.surf = pygame.Surface((self.leveys, 50))
        self.surf.fill((10, 10, 10))
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = 1030

class Peli:
    def __init__(self):
        pygame.init()
        pelaaja = Pelaaja()
        alusta = Alusta()
        alusta2 = Alusta()
        alusta2.rect.x = alusta.leveys + 100

        screen = pygame.display.set_mode([1920, 1080])
        pygame.display.set_caption("Skeittaaja rotkoon")

        running = True
        while running:

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    running = False
                elif tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_ESCAPE:
                        running = False
                    elif tapahtuma.key == pygame.K_SPACE:
                        if voi_hypata:
                            pelaaja.hyppy()
            
            #painovoima
            sprite_list = [pelaaja]
            if pelaaja not in pygame.sprite.spritecollide(alusta, sprite_list, False) \
            and pelaaja not in pygame.sprite.spritecollide(alusta2, sprite_list, False):
                voi_hypata = False
                pelaaja.rect.y += 1  
            else:
                voi_hypata = True
            
            alusta.rect.x -= 1
            if alusta.rect.x == -(alusta.leveys):
                alusta = Alusta()
                alusta.rect.x = alusta2.leveys + 200
            alusta2.rect.x -= 1
            if alusta2.rect.x == -(alusta2.leveys):
                alusta2 = Alusta()
                alusta2.rect.x = alusta.leveys + 200

            screen.fill((235, 235, 235))
            screen.blit(pelaaja.surf, pelaaja.rect)
            screen.blit(alusta.surf, alusta.rect)
            screen.blit(alusta2.surf, alusta2.rect)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Peli()