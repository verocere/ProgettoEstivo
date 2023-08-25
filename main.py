import sys, pygame
from pygame.locals import *
from bird import Bird 
from tubo import Tubi
pygame.init()

VEL=3
SCREEN_SIZE=(288, 462)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((50,170,170))


FONT = pygame.font.SysFont('Cominc Sans MS', 60, bold=True)




pygame.display.set_caption('Flappy bird')

clock = pygame.time.Clock()
fps = 60

sfondo = pygame.image.load("immagini/sfondo.png")
base = pygame.image.load("immagini/base.png")
gameover = pygame.image.load("immagini/gameover.png")

mioBird=Bird(screen, 30, 200, 70, 70)



def inizializza():
    global basex, punti, tubi, inmezzo
    mioBird.x=30
    mioBird.y=150
    mioBird.vely=0
    tubi=[]
    tubi.append(Tubi(screen))
    basex=0
    punti=0
    inmezzo=False


def disegna_tutto():
    screen.blit(sfondo, (0, 0))
    mioBird.draw()
    
    screen.blit(base, (basex, 400))
    for t in tubi:
        t.avanza_stampa()
    punti_render = FONT.render(str(punti), 1, (255,255,255))
    screen.blit(punti_render, (220, 15))




def game_over():
    screen.blit(gameover, (50, 180))
    pygame.display.update()
    clock.tick(fps)
    
    
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


inizializza()


while True:

    
    mioBird.move()
    

    for tubo in tubi:
        if tubo.x<=-200:
            tubi.remove(tubo)
    if tubi[-1].x<100:
        tubi.append(Tubi(screen))


    basex-=VEL
    if basex<=-45:
        basex=0

    for tubo in tubi:
        if tubo.collisione(mioBird):
            game_over()

    if not inmezzo:
        for t in tubi:
            if t.fra_i_tubi(mioBird):
                inmezzo = True
                break
    if inmezzo:
        inmezzo = False
        for t in tubi:
            if t.fra_i_tubi(mioBird):
                inmezzo = True
                break
        if not inmezzo:
            punti +=1

    if mioBird.rect.bottom>=410:
        game_over()

    disegna_tutto()

    pygame.display.update()
    clock.tick(fps)
