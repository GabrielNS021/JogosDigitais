import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Madeira(pygame.sprite.Sprite):
    def __init__(self):
        super(Madeira, self).__init__()
        self.largura = 200
        self.altura = 30
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.speed = 5

        self.rect.x = SCREEN_WIDTH // 2 - self.largura // 2
        self.rect.y = -self.altura

        espaco = random.randint(1, 5)
        if espaco == 1:
            print(1)
        elif espaco == 2:
            print(2)
        elif espaco == 3:
            print(3)
        elif espaco == 4:
            print(4)
        elif espaco == 5:
            print(5)

    def update(self):
        self.rect.y += self.speed 
        
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()