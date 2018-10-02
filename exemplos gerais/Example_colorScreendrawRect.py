#importa a biblioteca pygame
import pygame

#inicializa as módulos dessa biblioteca.
pygame.init()

#Seta o tamanho da janela
screen = pygame.display.set_mode((600,400))

#troca a cor do display para branco
screen.fill((0,0,255))

#definindo as cores do retangulo para vermelho
red = (255,0,0)

#função draw.rect = screen, cor, posição inicial e tamanho
pygame.draw.rect(screen,red,(40,40,90,30), 0)

#atualiza a cor da janela
pygame.display.flip()
