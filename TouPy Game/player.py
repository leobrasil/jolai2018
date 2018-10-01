import pygame
import sys

from pygame.locals import Color

class Player(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player.png").convert_alpha()
        self.vida = pygame.image.load("heart.png").convert_alpha()
        self.rectimg = pygame.Rect(x-12,y-10,10,10)
        self.rect = pygame.Rect(x-5,y-5,10,10)

def criar_jogador():
    return Player(0,0)

def atualizar_jogador(jogador):
    position = pygame.mouse.get_pos()
    px,py = position
    jogador.x = px
    jogador.y = py
    jogador.rect.x = px-9
    jogador.rect.y = py-9
    
def mostrar_jogador(screen,jogador,vidas):
    screen.blit(jogador.image,(jogador.x-29,jogador.y-25))
    pygame.draw.rect(screen,(0,255,0), jogador.rect, 0)
    if vidas == 1:
        screen.blit(jogador.vida,(10,10))
    if vidas == 2:
        screen.blit(jogador.vida,(10,10))
        screen.blit(jogador.vida,(45,10))
    if vidas == 3:
        screen.blit(jogador.vida,(10,10))
        screen.blit(jogador.vida,(45,10))
        screen.blit(jogador.vida,(80,10))
    
    
