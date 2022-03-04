import pygame
from pygame.locals import *
from time import time
pygame.init()

#set the window
windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)

#gestion des cliques
clicks = 0
clicksFont = pygame.font.SysFont("Andalé Mono",50)
clicksSurface = clicksFont.render("CLICKS : {0}".format(clicks),True,(0,0,0))
clicksRect = clicksSurface.get_rect(midtop=(windowSize[0]/2,windowSize[1]/2))

#gestion du temps et du départ de la partie
timer = 10
start = time()
timerFont = pygame.font.SysFont("Andalé Mono",50)
timerSurface = timerFont.render("TIMER : {0}s".format(timer), True,(0,0,0))
timerRect = timerSurface.get_rect(midbottom=(windowSize[0]/2,windowSize[1]/2))
playing = True
partyStart = False

#gestion de l'affichage du score
score = 0
scoreFont = pygame.font.SysFont("Andalé Mono", 50)
scoreSurface = scoreFont.render("Score : {} CPS".format(score), True, (0,0,0))
scoreRect = scoreSurface.get_rect(midtop=(-100,-100))

#bouton pour fermer la fenetre
endFont = pygame.font.SysFont("Andalé Mono", 50)
endSurface = endFont.render("CLOSE", True, (0,0,0))
endRect = endSurface.get_rect(topright=(windowSize[0]-10,10))

while playing:
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            #si la partie n'a pas encore débuté
            if windowSize[0]-120 < event.pos[0] < windowSize[0] and 10 < event.pos[1] < 40:
                playing = False
            if clicks == 0:
                partyStart = True
                start = time()
            #sinon on incrémente les cliques et son affichage
            clicks+=1
            clicksSurface = clicksFont.render("CLICKS : {0}".format(clicks),True,(0,0,0))
            clicksRect = clicksSurface.get_rect(midtop=(windowSize[0]/2,windowSize[1]/2))

    #si le chrono est dépassé, on affiche le résultat    
    if timer <= 0:
        score = clicks/10
        scoreSurface = scoreFont.render("Score : {} CPS".format(score), True, (0,0,0))
        scoreRect = scoreSurface.get_rect(topleft=(0,0))
        #les deux états qui définissent le début d'une partie ou non
        clicks = 0
        partyStart = False
    if partyStart:
        timer = 10 - (time() - start)
    else:
        timer = 10

    #affichage du timer en temps réel
    timerSurface = timerFont.render("TIMER : {0}s".format(round(timer,1)), True,(0,0,0))
    timerRect = timerSurface.get_rect(midbottom=(windowSize[0]/2,windowSize[1]/2))

    #on rempli l'écran avec les surfaces : clicks, timer, score
    screen.fill((255,255,255))
    screen.blit(clicksSurface,clicksRect)
    screen.blit(timerSurface,timerRect)
    screen.blit(scoreSurface,scoreRect)
    screen.blit(endSurface,endRect)
    pygame.display.flip()
pygame.quit()

                
                
        

