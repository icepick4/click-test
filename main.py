"""jeu de cps"""
from time import time
import pygame

pygame.display.init()

#set the window
window_size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(window_size)

#gestion des cliques
CLICKS = 0
click_font = pygame.font.SysFont("Andalé Mono",50)
click_surface = click_font.render(f"CLICKS : {CLICKS}",True,(0,0,0))
click_rect = click_surface.get_rect(midtop=(window_size[0]/2,window_size[1]/2))

#gestion du temps et du départ de la partie
TIMER = 10
start = time()
timer_font = pygame.font.SysFont("Andalé Mono",50)
timer_surface = timer_font.render(f"TIMER : {TIMER}s", True,(0,0,0))
timer_rect = timer_surface.get_rect(midbottom=(window_size[0]/2,window_size[1]/2))
PLAYING = True
PARTYSTART = False

#gestion de l'affichage du score
SCORE = 0
score_font = pygame.font.SysFont("Andalé Mono", 50)
score_surface = score_font.render(f"Score : {SCORE} CPS", True, (0,0,0))
score_rect = score_surface.get_rect(midtop=(-100,-100))

#bouton pour fermer la fenetre
end_font = pygame.font.SysFont("Andalé Mono", 50)
end_surface = end_font.render("CLOSE", True, (0,0,0))
end_rect = end_surface.get_rect(topright=(window_size[0]-10,10))

while PLAYING:
    for event in pygame.event.get():
        if event.type == 256:
            PLAYING = False
        elif event.type == 5and event.button == 1 :
            #si la partie n'a pas encore débuté
            if window_size[0]-140 < event.pos[0] < window_size[0] and 10 < event.pos[1] < 40:
                PLAYING = False
            if CLICKS == 0:
                PARTYSTART = True
                start = time()
            #sinon on incrémente les cliques et son affichage
            CLICKS+=1
            click_surface = click_font.render(f"CLICKS : {CLICKS}",True,(0,0,0))

    #si le chrono est dépassé, on affiche le résultat
    if TIMER <= 0:
        SCORE = CLICKS/10
        score_surface = score_font.render(f"Score : {SCORE} CPS", True, (0,0,0))
        score_rect = score_surface.get_rect(topleft=(0,0))
        #les deux états qui définissent le début d'une partie ou non
        CLICKS = 0
        PARTYSTART = False
    if PARTYSTART:
        TIMER = 10 - (time() - start)
    else:
        TIMER = 10

    #affichage du timer en temps réel
    timer_surface = timer_font.render(f"TIMER : {round(TIMER,1)}s", True,(0,0,0))
    #on rempli l'écran avec les surfaces : clicks, timer, score
    screen.fill((255,255,255))
    screen.blit(click_surface,click_rect)
    screen.blit(timer_surface,timer_rect)
    screen.blit(score_surface,score_rect)
    screen.blit(end_surface,end_rect)
    pygame.display.flip()
pygame.display.quit()
