import pygame
from random import randrange
from pygame.locals import *
import os
import sys
import bullet
import player
import random
import timer
import boss
from threading import Timer


pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"

## Definindo a propriedades da tela
#global screen
#screen = pygame.display.set_mode((400,600))
#pygame.display.set_caption("Carregando Imagem")
## 
    

##CLASSE PLAYER
def jogo():
    ##iniciando a tela
    ## Definindo a propriedades da tela
    global screen
    screen = pygame.display.set_mode((400,600))
    pygame.display.set_caption("TouPy")
    pygame.mouse.set_visible(False)
    ## 
    #Movendo a imagem vertical e horizontalmente com evento do teclado
    x=1
    y=1
    global score
    vida = 3
    ## CRIANDO O JOGADOR PELA CLASSE
    jogador = player.criar_jogador()
    inimigo = boss.Alien(15,15)
    ## variaveis 
    tiro = []
    novo_tiro = []
    comecar = 0
    jogo_rodando = True
    perdeu = False
    comeco_tempo = 0
    new_way = 60
    bg = pygame.image.load("bg.png").convert_alpha()
    ## Pegando o comeco do jogo em TICKS
    ## CRIANDO PELA CLASSE
    while jogo_rodando:
        tempo = int(pygame.time.get_ticks()/1000) 
        if perdeu == False:
            ## Pegando eventos de tecla!
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if comecar != 1:
                                comecar = 1
                                comeco_tempo = pygame.time.get_ticks()
            ## Criando tela
            screen.fill((255, 255, 255)) ## Colorindo a tela
            ## Texto e Score
            fonte = pygame.font.Font(None, 50) ## Criar a fonte
            vidas = fonte.render(str(vida), 1, (255, 255, 255)) 
            screen.blit(vidas,(10,10))
            if comecar == 1:
                screen.blit(bg,(0,0))
            ## Jogador
            
            ## BULLETS
                inimigo.colocar(screen)
                inimigo.comportamento(tempo)
            if comecar == 1:
                bullet.atualizar_balas(tiro)
                bullet.mostrar_balas(screen,tiro)
                tiro,vida = bullet.checar_colisao(jogador.rect,tiro,vida)
                tiro = bullet.excluir_bala(tiro)
                tempo_vivo = (pygame.time.get_ticks()-comeco_tempo) // 100
                pontuacao = fonte.render(str(tempo_vivo),1,(255,255,255)) ## ESSA É A PONTUACAO DO JOGADOR
                screen.blit(pontuacao,(300,10))
                ## Boss e timer
                clock = timer.setar_timer(1000)
                if clock == True:
                    aleatorio = random.randint(1, 7)
                    tiros_boss =  bullet.bullet(screen,aleatorio)
                    tiro = bullet.adicionar_balas(tiro,tiros_boss)
             
            ## Pontuacao
            if comecar == 0:
                texto_inicial = fonte.render("Clique para começar!",1,(0,0,0))
                screen.blit(texto_inicial,(25,300))
            player.atualizar_jogador(jogador)
            player.mostrar_jogador(screen,jogador,vida)
            pygame.display.update()
        if perdeu == True:
            jogo_rodando= False
            score = tempo_vivo
            pygame.quit() ## Recomendo colocar um Return pontuacao... Voce sabe tê!
            import Login
        elif vida <= 0:
            perdeu = True
jogo()
