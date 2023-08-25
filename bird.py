import sys, pygame
from pygame.locals import *

pygame.init()
 

bird = pygame.image.load("immagini/bird_trasparente.png")


GRAVITA=0.3
SALTO=-5



class Bird:
    def __init__(self, screen, x, y, width, height) -> None:
        self.screen=screen
        self.x=x
        self.y=y
        self.vely=0
        self.width=width
        self.height=height
        self.image = bird.convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect=pygame.Rect(self.x, self.y, self.width,self.height)

    def draw(self):
        self.rect=pygame.Rect(self.x, self.y, self.width,self.height)
        self.screen.blit(self.image, self.rect)


    def move(self):
        self.vely+=GRAVITA
        self.y+=self.vely
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.vely = SALTO
            if event.type == pygame.QUIT:
                pygame.quit()
