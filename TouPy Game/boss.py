import pygame
import sys

class Alien(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.Imagem1= pygame.image.load('imagens/01.PNG')
        self.Imagem2= pygame.image.load('imagens/02.PNG')
        self.Imagem3= pygame.image.load('imagens/03.PNG')
        self.Imagem1= pygame.image.load('imagens/01.1.PNG')
        self.Imagem2= pygame.image.load('imagens/02.2.PNG')
        self.Imagem4= pygame.image.load('imagens/04.PNG')
        
        self.listaImagens = [self.Imagem1,self.Imagem2,self.Imagem3,self.Imagem4]
        self.posImagem = 0
        self.ImagemAlien = self.listaImagens[self.posImagem]

        self.rect = self.ImagemAlien.get_rect()
        
        self.listaDisparo = []
        self.velocidade = 20
        self.rect.top = posy
        self.rect.left = posx
      
        self.configTempo = 1
        self.clock = pygame.time.Clock()
        self.new_way = 5

        self.quantDisparo = 5
        self.contador = 0
        self.direita = True
        self.maxDescida = self.rect.top + 40
        self.relogio = pygame.time.Clock()


    def comportamento(self,tempo):
        if self.configTempo == tempo:
            #print("Entrou")
            self.movimentos()
            self.posImagem += 1
            self.configTempo += 1
            
            if self.rect.left < 160:
                self.rect.left += 10
            else:
                self.rect.left -= 130
    

            if self.posImagem > len(self.listaImagens)-1:
                self.posImagem = 0

    def movimentos(self):
        if not self.new_way:
            self.new_way = 5
            print(self.new_way)
           
                
 
    #def __movimentoLateral(self):
       # pass
    def colocar(self, superficie):
        self.ImagemAlien = self.listaImagens[self.posImagem]
        superficie.blit(self.ImagemAlien, self.rect)
        


    
   
            
