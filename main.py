#Gabriel Neman Silva - 10403348

import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo da Nave Espacial')

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name):
        super(NaveEspacial, self).__init__()
        self.name = name
        self.alive = True
        self.position = pygame.math.Vector2(screen_width // 2, screen_height // 2)
        self.direction = 0
        self.speed = 5
        self.shield = 100
        self.energy = 100
        self.image = pygame.image.load('nave.png')
        self.image = pygame.transform.scale(self.image, (50, 55))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.balas = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        
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
        
        if keys[K_SPACE]:
            self.shoot()

        self.rect.center = self.position
        self.balas.update()

    def shoot(self):
        bala = TiroNaveEspacial(self.rect.center)
        self.balas.add(bala)

class TiroNaveEspacial(pygame.sprite.Sprite):
    def __init__(self, position):
        super(TiroNaveEspacial, self).__init__()
        self.dano = 10
        self.position = pygame.math.Vector2(position)
        self.speed = 10 
        self.image = pygame.image.load('bala.png')
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.position.y -= self.speed
        
        if self.position.y < 0:
            self.kill()
        
        self.rect.center = self.position

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
        
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        nave.balas.draw(screen) 
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
