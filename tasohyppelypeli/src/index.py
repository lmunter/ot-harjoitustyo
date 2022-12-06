import pygame
from my_platform import Platform
from player import Player

class Game:
    def __init__(self):
        pygame.init()

        #luodaan oliot
        self.player = Player()
        self.platform = Platform()
        self.platform2 = Platform()
        self.platform2.rect.x = self.platform.width + 100

        screen = pygame.display.set_mode([1920, 1080])
        pygame.display.set_caption("Skeittaaja rotkoon")

        #pelisilmukka
        self.running = True
        while self.running:
            self.check_events()

            self.gravity(self.player, self.platform, self.platform2)

            self.platform.rect.x -= 1
            self.platform2.rect.x -= 1

            screen.fill((235, 235, 235))
            screen.blit(self.player.surf, self.player.rect)
            screen.blit(self.platform.surf, self.platform.rect)
            screen.blit(self.platform2.surf, self.platform2.rect)
            pygame.display.flip()

        pygame.quit()

    def recycle_platforms(self):
        if self.platform.rect.x == -(self.platform.width):
            self.platform = Platform()
            self.platform.rect.x = self.platform2.width + 200
        if self.platform2.rect.x == -(self.platform2.width):
            self.platform2 = Platform()
            self.platform2.rect.x = self.platform.width + 200


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    if self.can_jump:
                        self.player.jump()

    def gravity(self, player, platform1, platform2):
        sprite_list = [player]
        if player not in pygame.sprite.spritecollide(platform1, sprite_list, False) \
        and player not in pygame.sprite.spritecollide(platform2, sprite_list, False):
            self.can_jump = False
            self.player.rect.y += 1
        else:
            self.can_jump = True

if __name__ == "__main__":
    Game()
