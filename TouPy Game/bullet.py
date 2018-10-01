import pygame
import os
import sys
import random
import padroes
            

#pygame.display.update()

def bullet(screen,tipo):
    if tipo == 2: ## PADRAO ALEATORIO
        ## Criar os padroes de bullets aqui
        lista = []
        lista = padroes.padrao3(lista,screen)
        return lista
    if tipo == 1: ## PADRAO ALEATORIO
        ## Criar os padroes de bullets aqui
        lista = []
        lista = padroes.padrao2(lista,screen)
        return lista
    if tipo == 3:
        lista = []
        lista = padroes.padrao4 (lista,screen)
        return lista
    if tipo == 4:
        lista = []
        lista = padroes.padrao5 (lista,screen)
        return lista
    if tipo == 5:
        lista = []
        lista = padroes.padrao6 (lista,screen)
        return lista
    if tipo == 6:
        lista = []
        lista = padroes.padrao7 (lista,screen)
        return lista
    if tipo == 7:
        lista = []
        lista = padroes.padrao8 (lista,screen)
        return lista
    else:
        ## Criar os padroes de bullets aqui
        lista = []
        lista = padroes.padrao1(lista,screen)
        return lista

def adicionar_balas(lista,nova_lista):
    lista = lista + nova_lista
    return lista

def atualizar_balas(lista):
    for j in range(0,len(lista)):
        if lista[j].y < 600:
            lista[j].y += lista[j].velo
            lista[j].rect = pygame.Rect(lista[j].x,lista[j].y,18,18)
            #return lista

def mostrar_balas(screen,lista):
    for j in range(0,len(lista)):
        #image = lista[j].image
        #screen.blit(image,(lista[j].x,lista[j].y))
        x = lista[j].x
        y = lista[j].y
        rect = lista[j].rect
        pygame.draw.rect(screen,(255,0,0),rect,0)
        
def checar_colisao(player_rect,lista,placar):
    colision_check = 0
    colidiu = False
    for colision_check in range (0,len(lista)):
        colisao = lista[colision_check].rect
        if colisao.colliderect(player_rect):
            #print("Colisao X:",colisao.x," Y:",colisao.y)
            placar = placar - 1
            colidiu = True
            colisao = colision_check
    if colidiu == True:
        lista = []
    return [lista,placar]

def excluir_bala(lista):
    if len(lista) > 1:
        for j in range(0,len(lista)):
            a = lista[j]
            if a.y >= 600:
                del lista[j]
                #print (len(lista))
            return lista
    else:
        lista = []
        return lista
#while True:
 #   px,py = pygame.mouse.get_pos()
  #  for event in pygame.event.get():
   #     if event.type == pygame.KEYDOWN:
    #        if event.key ==pygame.K_DOWN:
     #           bullet()
    
