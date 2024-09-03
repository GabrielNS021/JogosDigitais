#Gabriel Neman Silva - 10403348

import pygame
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo da Nave Espacial')

# Classe NaveEspacial herdando de Sprite
class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name):
        super(NaveEspacial, self).__init__()
        self.name = name
        self.alive = True
        self.position = pygame.math.Vector2(screen_width // 2, screen_height // 2)
        self.direction = 0  # Direção inicial (0 graus)
        self.speed = 5  # Velocidade da nave
        self.shield = 100
        self.energy = 100
        self.image = pygame.image.load('nave.png')
        self.image = pygame.transform.scale(self.image, (50, 55))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Movimentação
        if keys[K_LEFT] or keys[K_a]:
            self.position.x -= self.speed

        if keys[K_RIGHT] or keys[K_d]:
            self.position.x += self.speed

        if keys[K_DOWN] or keys[K_s]:
            self.position.y += self.speed

        if keys[K_UP] or keys[K_w]:
            self.position.y -= self.speed

        if keys[K_n]:
            self.speed += 1

        if keys[K_m]:
            self.speed -= 1
        
        # Atualiza a posição do retângulo da nave
        self.rect.center = self.position

class TiroNaveEspacial(pygame.sprite.Sprite):
    def __inti__(self, dano):
        super(TiroNaveEspacial, self).__init__()
        self.dano = dano
        self.direction = 0
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()

        #if keys[K_SPACE]:

# Função principal do jogo
def main():
    nave = NaveEspacial("Nave 1")
    all_sprites = pygame.sprite.Group()
    all_sprites.add(nave)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        all_sprites.update()
        
        screen.fill((0, 0, 0))  # Preenche o fundo de preto
        all_sprites.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
    