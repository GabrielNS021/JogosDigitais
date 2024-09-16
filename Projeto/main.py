import pygame
from pygame.locals import *
from obstaculos import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Nave Espacial')

def main():
    all_sprites = pygame.sprite.Group()

    madeira = Madeira()
    all_sprites.add(madeira)

    ADD_MADEIRA = USEREVENT + 1
    pygame.time.set_timer(ADD_MADEIRA, 1000)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # A verificação do evento ADD_MADEIRA precisa estar aqui, dentro do loop de eventos
            if event.type == ADD_MADEIRA:
                madeira = Madeira()
                all_sprites.add(madeira)

        all_sprites.update()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
