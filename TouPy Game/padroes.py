import pygame
import random
## Classe Tiro -- NAO MECHE AQUI
class tiro():
    def __init__(self,x,y,velo,screen):
        self.x = x
        self.y = y
        self.velo = velo
        #self.image = pygame.image.load("ini.jpg")
        self.rect = pygame.Rect(x+10,y+10,x,y)


def padrao1(lista,screen):
    for a in range (0,11):
        lista.append(tiro(random.randint(0,380),random.randint(0,100),random.randint(1,10)/10,screen))
    return lista

def padrao2(lista,screen):
    ataque1 = [[50,0],[50,18],[50,36],[50,54],[100,0],[100,18],[100,36],[100,54],[150,0],[150,18],[150,36],[150,54]]
    for a in range (0,len(ataque1)):
        lista.append(tiro(ataque1[a][0],ataque1[a][1],0.7,screen))
    return lista

def padrao3(lista,screen):
    ataque1 = [[350,0],[350,18],[350,36],[350,54],[300,0],[300,18],[300,36],[300,54],[250,0],[250,18],[250,36],[250,54]]
    for a in range (0,len(ataque1)):
        lista.append(tiro(ataque1[a][0],ataque1[a][1],0.7,screen))
    return lista

def padrao4(lista,screen):
    ataque2 = [[18,-15], [65, -3], [94,20],[134,38], [174,56], [214,74], [254,92], [294,110], [327,128], [364,146], [45,-80], [86,-46] , [120,-16], [150,6], [200, 26],[260,46],[320,66], [360,86],[380,106],[0,-100]]
    for a in range (0,len(ataque2)):
        lista.append(tiro(ataque2[a][0],ataque2[a][1],0.3,screen))
    return lista

def padrao5(lista,screen):
    ataque2 = [[-4, -3], [30, 10], [64, 23], [98, 36], [132, 49], [166, 62 ], [200, 75], [234, 62], [268, 49], [302, 36], [336, 23],[370, 10], [400, 4]]
    for a in range (0,len(ataque2)):
        lista.append(tiro(ataque2[a][0],ataque2[a][1],0.5,screen))
    return lista

def padrao6(lista,screen):
    ataque2 = [[0,15], [15,15]]
    for a in range (0,len(ataque2)):
        lista.append(tiro(ataque2[a][0],ataque2[a][1],0.5,screen))
    return lista

def padrao7(lista,screen):
    ataque2 = [[365,15], [383,15]]
    for a in range (0,len(ataque2)):
        lista.append(tiro(ataque2[a][0],ataque2[a][1],0.3,screen))
    return lista

def padrao8(lista,screen):
    ataque2 = [[0, 40], [0, 58], [18,40], [18,58], [68,40], [68,58], [86,40], [86,58], [136,40], [136,58], [154,40], [154,58], [204,40], [204,58], [222,40], [222,58], [272,40], [272,58], [290,40], [290,58], [340,40], [340,58],[358,40], [358,58], [395,40], [395,58]]
    for a in range (0,len(ataque2)):
        lista.append(tiro(ataque2[a][0],ataque2[a][1],0.3,screen))
    return lista 
