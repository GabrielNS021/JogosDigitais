#Gabriel Neman Silva - 10403348

import pygame
import random
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo dos Circulos')

circulo_tamanho = [20, 40, 60]
circulo_cor = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] 
circulo_quantidade = 10

class Circulo(pygame.sprite.Sprite):
    def __init__(self, tamanho, cor):
        super().__init__()
        self.tamanho = tamanho
        self.cor = cor
        self.image = pygame.Surface((tamanho * 2, tamanho * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, cor, (tamanho, tamanho), tamanho)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - tamanho * 2)
        self.rect.y = random.randint(0, screen_height - tamanho * 2)
        self.dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
        self.dy = random.choice([-1, 1]) * random.uniform(0.5, 2)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.dx = -self.dx
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.dy = -self.dy

def main():
    all_sprites = pygame.sprite.Group()

    for _ in range(circulo_quantidade):
        tamanho = random.choice(circulo_tamanho)
        cor = random.choice(circulo_cor)
        circle = Circulo(tamanho, cor)
        all_sprites.add(circle)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        all_sprites.update()
        
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
