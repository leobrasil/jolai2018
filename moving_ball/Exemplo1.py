import pygame
import os
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Carregando Imagem")
screen.fill((0, 0, 0))

# cria uma pasta e carrega a imagem
folder = "img"
image = pygame.image.load(os.path.join(folder,"ball.png"))

# obtém as dimensões da imagem
largura_imagem, altura_imagem = image.get_rect().size
print(largura_imagem)
print(altura_imagem)

# redimensiona a imagem para que fique com a metade da largura e da altura
image = pygame.transform.scale(image, (int(largura_imagem/4), int(altura_imagem/4)))
largura_imagem, altura_imagem = image.get_rect().size
print(largura_imagem)
print(altura_imagem)

#movendo a imagem horizontalmente
x=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    screen.blit(image, (x,100))
    
    x+=1
    #se a imagem ultrapassar a extremidade da tela, mova-se de volta
    if x>600:
        x -= 600
    pygame.display.update()




