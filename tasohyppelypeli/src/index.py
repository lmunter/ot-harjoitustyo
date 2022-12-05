import pygame
from platform import Platform
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        player = Player()
        platform = Platform()
        platform2 = Platform()
        platform2.rect.x = platform.width + 100

        screen = pygame.display.set_mode([1920, 1080])
        pygame.display.set_caption("Skeittaaja rotkoon")

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        if can_jump:
                            player.jump()
            
            #painovoima
            sprite_list = [player]
            if player not in pygame.sprite.spritecollide(platform, sprite_list, False) \
            and player not in pygame.sprite.spritecollide(platform2, sprite_list, False):
                can_jump = False
                player.rect.y += 1  
            else:
                can_jump = True
            
            platform.rect.x -= 1
            if platform.rect.x == -(platform.width):
                platform = Platform()
                platform.rect.x = platform2.width + 200
            platform2.rect.x -= 1
            if platform2.rect.x == -(platform2.width):
                platform2 = Platform()
                platform2.rect.x = platform.width + 200

            screen.fill((235, 235, 235))
            screen.blit(player.surf, player.rect)
            screen.blit(platform.surf, platform.rect)
            screen.blit(platform2.surf, platform2.rect)
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Game()