import pygame
import os

class Pelaaja(pygame.sprite.Sprite):
    def __init__(self):
        super(Pelaaja, self).__init__()
        self.surf = pygame.Surface((25, 75))
        self.surf.fill((205, 205, 205))
        self.rect = self.surf.get_rect()
pygame.init()
pelaaja = Pelaaja()

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
    pygame.display.flip()

pygame.quit()