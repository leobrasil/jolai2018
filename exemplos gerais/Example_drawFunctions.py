#importa a biblioteca pygame
import pygame
from math import pi
 
#inicializa as módulos dessa biblioteca.
pygame.init()
 
# Define as cores que serão usadas no formato RGB
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
#Seta o tamanho da janela
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
     
# Pinta a tela de branco
screen.fill(WHITE)
 
# 1) Desenha na tela uma linha verde saindo de (0,0) até (50,75)
# 5 pixels de largura.
pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
 
# 2) Desenha um segmento de linha preta partindo de (0,80) até (220,30) 
# 5 pixels wide. False deixa segmento aberto e True fecha o segmento
pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    
# 3) Desenha na tela uma linha verde com antialiasing saindo de (0,50) até (50,80)
# 5 pixels de largura. True habilita o antialising
pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)

# 4) Desenha um retângulo preto na tela: posição 150 e 10; largura 50; altura 20
pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

# 5) Desenha um retângulo preto na tela: posição 75 e 10; largura 50; altura 20
#e espessura da linha 2 pixels
pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
     
# 6) Desenha uma elipse usando um retangulo na cor vermelha: posição 300 e 10; altura 50; altura 20 
pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

# 7) Desenha uma elipse usando um retangulo na cor vermelha: posição 300 e 10; altura 50; altura 20;
#e espessura da linha 2 pixels
pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

# 8) Desenha um triangulo usando comandos de poligono e espessura 5 pixesls 
pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
  
# 9) Desenha um circulo
pygame.draw.circle(screen, BLUE, [60, 250], 40)

# 10) Desenha partes de uma elipse. 
# Usa radianos para determinar o ângulo do desenho.
pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    
# Atualiza a tela
pygame.display.flip()
 

