import sys, pygame
from random import randint
from pygame.locals import *

pygame.init()
VEL=3

tubo_giu = pygame.image.load("immagini/tubo.png")
tubo_su = pygame.transform.flip(tubo_giu, False, True)



class Tubi:
    def __init__(self, screen) -> None:
        self.x=350
        self.y=randint(-75, 150)
        self.screen=screen
        self.rect_su=pygame.rect.Rect(self.x, self.y-210, tubo_su.get_width(), tubo_su.get_height())
        self.rect_giu=pygame.rect.Rect(self.x, self.y+210, tubo_giu.get_width(), tubo_giu.get_height())

    def avanza_stampa(self):
        self.x-=VEL
        self.rect_su.x=self.x
        self.rect_giu.x=self.x
        self.screen.blit(tubo_giu, self.rect_giu)
        self.screen.blit(tubo_su, self.rect_su)


    def collisione(self, bird):
        margine = 25
        uccello_lato_dx = bird.x + bird.width - margine
        uccello_lato_sx = bird.x + margine
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        uccello_lato_su = bird.y + margine
        uccello_lato_giu = bird.y + bird.height - margine
        tubi_lato_su = self.y + 110
        tubi_lato_giu = self.y + 210

        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                return True
        return False
    

    def fra_i_tubi(self, bird):
        margine = 25
        uccello_lato_dx = bird.x + bird.width - margine
        uccello_lato_sx = bird.x + margine
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            return True