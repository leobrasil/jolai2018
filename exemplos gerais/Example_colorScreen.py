#importa a biblioteca pygame
import pygame

#inicializa as módulos dessa biblioteca.
pygame.init()

#Seta o tamanho da janela
screen = pygame.display.set_mode((600,400))

#troca a cor da janela para branco
screen.fill((255,255,255))

#atualiza a cor da janela
pygame.display.flip()
