# LIA KASSARDJIAN (31750370)
# LINGUAGEM DE PROGRAMACAO I - PROJETO

#--------------------------PARTE 1-------------------------------

# Importa as bibliotecas
import pygame
import os
import random


pygame.mixer.pre_init(44100,16,2,4096)

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Pé na estrada - LIA KASSARDJIAN")

#--------------------------PARTE 2-------------------------------

colorGround = (124,252,0)
colorStreet = (105,105,105)
colorLine = (255,255,0)
colorCar1 = (178,34,34)
colorCar2 = (139,0,0)
colorCar3 = (128,0,0)
colorGlass = (127,255,212)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
DARK_GREEN = (0,200,0)
DARKER_GREEN = (0,128,0)
BLUE = (0,0,255)
DARK_BLUE = (0,0,200)
RED = (255,0,0)
DARK_RED = (200,0,0)

# Carrega imagens
folder = "img"
cone = pygame.image.load(os.path.join(folder,"cone.png"))
cone = pygame.transform.scale(cone,(76,100))
alce = pygame.image.load(os.path.join(folder,"alce.png"))
alce = pygame.transform.scale(alce,(200,200))
buraco = pygame.image.load(os.path.join(folder,"buraco.png"))
buraco = pygame.transform.scale(buraco,(181,100))
tronco = pygame.image.load(os.path.join(folder,"tronco.png"))
tronco = pygame.transform.scale(tronco,(190,70))
vida = pygame.image.load(os.path.join(folder,"vida.png"))
vida = pygame.transform.scale(vida,(40,40))
estrada = pygame.image.load(os.path.join(folder,"estrada.jpg"))
instru_img = pygame.image.load(os.path.join("img","instru0.png"))
instru_img = pygame.transform.scale(instru_img,(800,600))
teclas_teclado = pygame.image.load(os.path.join("img","setas_teclado.jpg"))
teclas_teclado = pygame.transform.scale(teclas_teclado,(200,200))

folder_sounds = "Sons"

obstaculos = [cone,alce,buraco,tronco,vida]

def desenha_carro(x):
    pygame.draw.polygon(screen,colorCar2,[[x,380],[x+15,420],[x-105,420],[x-90,380]])
    pygame.draw.polygon(screen,colorGlass,[[x-105,420],[x+15,420],[x,430],[x-90,430]])
    pygame.draw.rect(screen,colorCar1,(x-90,430,90,100))
    pygame.draw.polygon(screen,colorCar3,[[x-90,430],[x-90,530],[x-105,540],[x-105,420]])
    pygame.draw.polygon(screen,colorCar3,[[x,430],[x,530],[x+15,540],[x+15,420]])
    pygame.draw.polygon(screen,colorGlass,[[x-90,530],[x-105,540],[x+15,540],[x,530]])
    pygame.draw.polygon(screen,colorCar2,[[x-105,540],[x-90,570],[x,570],[x+15,540]])
    pygame.draw.ellipse(screen,BLACK,[x-115,420,15,60])
    pygame.draw.ellipse(screen,BLACK,[x+12,420,15,60])
    pygame.draw.ellipse(screen,BLACK,[x-115,490,15,60])
    pygame.draw.ellipse(screen,BLACK,[x+12,490,15,60])

def determina_fonte(size):
    return pygame.font.SysFont("comicsansms", size)

# Score na tela de jogo
def escreve_score(font,score):
    texto = str(score)
    while len(texto)<10:
        texto = "0" + texto       
    text = font.render("SCORE " + texto, True, WHITE)
    return text

def toca_musica(nome,repeticoes):
    pygame.mixer.music.load(os.path.join(folder_sounds,nome))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(repeticoes)

def cria_botao(cor1,cor2,x,y,width,height,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width>mouse[0]>x and y+height>mouse[1]>y:
        pygame.draw.rect(screen, cor2,(x,y,width,height))
        if click[0]==1 and action!=None:
            toca_musica("button.mp3",0)
            if action=="exit":
                pygame.quit()
                quit()
            return True
    else:
        pygame.draw.rect(screen, cor1,(x,y,width,height))

# Ranking na tela final
def exibe_ranking(texto_ranking):
    screen.blit(texto_ranking,(20,220))
    pos_ini_ranking = 260
    lst_ranking = lista_score
    lst_ranking.sort()
    i = 0
    while lst_ranking!=[] and i<10:
        ultima_pos = lst_ranking[len(lst_ranking)-1]
        pos_ranking = determina_fonte(30).render(str(i+1)+"º ..............." +str(ultima_pos),True,BLACK)
        screen.blit(pos_ranking, (50,pos_ini_ranking))
        pos_ini_ranking += 30
        i += 1
        lst_ranking = lst_ranking[:len(lst_ranking)-1]

# Tempo de jogo na tela de jogo
def escreve_tempo(tempo,nivel):
    horas = tempo//3600000
    minutos = tempo//60000 - 60*horas
    segundos = tempo//1000 - 60*minutos
    horas_texto = str(horas)
    minutos_texto = str(minutos)
    segundos_texto = str(segundos)
    if len(minutos_texto)<2:
        minutos_texto = "0" + minutos_texto
    if len(horas_texto)<2:
        horas_texto = "0" + horas_texto
    if len(segundos_texto)<2:
        segundos_texto = "0" + segundos_texto

    if segundos==15+15*nivel and nivel<=5:
        nivel+=1
    return determina_fonte(15).render(horas_texto+":"+minutos_texto+":"+segundos_texto,True,BLACK),nivel

lista_score = []

iniciar = False

instrucoes = False

final = False

#--------------------------PARTE 3-------------------------------

def tela_inicial():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    botao_iniciar = determina_fonte(35).render("Iniciar jogo", True, WHITE)
    botao_instrucoes = determina_fonte(35).render("Instruções", True, WHITE)
    titulo = determina_fonte(70).render("Pé na estrada", True, BLACK)
    
    screen.blit(estrada,(0,0))

    screen.blit(titulo,(225,30))
         
    iniciar = cria_botao(GREEN,DARK_GREEN,150,300,200,70,"play")
    screen.blit(botao_iniciar,(157,307))

    instrucoes = cria_botao(BLUE,DARK_BLUE,430,300,200,70,"notplay")
    screen.blit(botao_instrucoes,(440,307))

    pygame.display.flip()

    return iniciar, instrucoes


def intrucoes():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    texto_instrucoes = ['Utilize as teclas direita e esquerda ou "a" e "d" para movimentar o carro.','Desvie dos obstáculos e adquira vidas.']
    instrucao = [determina_fonte(20).render(texto_instrucoes[0], True,BLACK),determina_fonte(20).render(texto_instrucoes[1], True, BLACK)]
    botao_jogar = determina_fonte(35).render("Jogar!",True,WHITE)

    # Texto e figuras na tela:
    screen.blit(instru_img,(0,0))
    screen.blit(teclas_teclado, (300,50))
    pygame.draw.rect(screen,RED,(300,147,70,70),5)
    pygame.draw.rect(screen,RED,(432,147,70,70),5)
    screen.blit(instrucao[0], (60,270))
    screen.blit(instrucao[1], (225,300))
    iniciar = cria_botao(BLUE,DARK_BLUE,620,500,130,60,"play")
    screen.blit(botao_jogar,(630,505))

    pygame.display.flip()

    return iniciar
    
    
def tela_final(iniciar,score):
    voce_perdeu = determina_fonte(70).render("Você perdeu!",True,RED)
    texto_ranking = determina_fonte(30).render("Melhores pontuações até agora:",True,BLACK)
    botao_final = determina_fonte(35).render("Jogar novamente!",True,WHITE)
    botao_sair = determina_fonte(35).render("Sair do jogo",True,WHITE)

    while not iniciar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        screen.blit(estrada,(0,0))
        screen.blit(voce_perdeu,(200,30))
        sua_pontuacao = determina_fonte(35).render("Sua pontuação foi: "+str(score),True,BLACK)
        screen.blit(sua_pontuacao,(230,150))
        
        exibe_ranking(texto_ranking)    

        iniciar = cria_botao(BLUE,DARK_BLUE,490,400,302,60,"play")
        screen.blit(botao_final,(500,405))

        cria_botao(RED,DARK_RED,530,500,220,60,"exit")
        screen.blit(botao_sair, (540,505))

        pygame.display.flip()

    return final,iniciar    


def jogo(iniciar):
    clock = pygame.time.Clock()
    tempo = 0
    vidas = 5
    i = 0
    score = 0
    positionCar = [445,380]
    speedCar = [30,30]
    cria = True
    nivel = 0
    menos10 = determina_fonte(35).render("-10", True, RED)
    mais10 = determina_fonte(35).render("+10", True, DARKER_GREEN)
    # Posicoes para desenhos/imagens na tela:
    inicio_img_vidas = -40
    listaPosicoes1 = [-20,40,100]
    listaPosicoes2 = [180,240,300]
    listaPosicoes3 = [380,440,500]

    toca_musica("startup.mp3",0)
        

    while iniciar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

        if vidas==0 or score>=9999999999:
            iniciar = False
            final = True
            pygame.mixer.music.stop()
            break

        
        screen.fill(colorGround)
        pygame.draw.rect(screen,colorStreet,(100,0,600,600))
        pygame.draw.rect(screen,colorLine,(110,0,10,600))
        pygame.draw.rect(screen,colorLine,(680,0,10,600))

        # Eventos do teclado
        pressed = pygame.key.get_pressed()

        if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and positionCar[0]>=220 :
            positionCar[0] -= speedCar[0]
        if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and positionCar[0]<=670:
            positionCar[0] += speedCar[0]

        pygame.draw.rect(screen,colorLine,(395,listaPosicoes1[i],10,100))
        pygame.draw.rect(screen,colorLine,(395,listaPosicoes2[i],10,100))
        pygame.draw.rect(screen,colorLine,(395,listaPosicoes3[i],10,100))

        desenha_carro(positionCar[0])

        # Cria obstaculos
        if cria==True:
            X_obst = random.randint(100,600)
            Y_obst = 0
            j = random.randint(0,4)
            obstaculo = obstaculos[j]
            width = obstaculo.get_width()
            height = obstaculo.get_height()
            cria=False
            
        # Soma vidas e verifica colisao
        if j==4:
            if (positionCar[1]<=Y_obst+height and positionCar[1]+190>=Y_obst)and ((positionCar[0]>=X_obst and positionCar[0]<=X_obst+width) or (positionCar[0]-90>=X_obst and positionCar[0]-90<=X_obst+width) or (X_obst>=positionCar[0]-90 and X_obst<=positionCar[0])):
                cria=True
                pygame.mixer.music.stop()
                toca_musica("collectLife.mp3",0)
                if vidas<10:
                    vidas += 1
                
            else:
                screen.blit(obstaculo,(X_obst,Y_obst))
                Y_obst += 20
                score += 1
            if Y_obst>=800:
                cria=True

        # Verifica colisao com obstaculos
        else:
            if Y_obst>=800:
                cria=True
                score += 10
                pontos = mais10
                screen.blit(pontos,(740, 30))

            if (positionCar[1]<=Y_obst+height and positionCar[1]+190>=Y_obst)and ((positionCar[0]>=X_obst and positionCar[0]<=X_obst+width) or (positionCar[0]-90>=X_obst and positionCar[0]-90<=X_obst+width)):
                cria=True
                score-=10
                vidas -= 1
                pontos = menos10
                screen.blit(pontos,(740, 30))

                pygame.mixer.music.stop()
                toca_musica("crash.wav",0)

                
            else:
                screen.blit(obstaculo,(X_obst,Y_obst))
                Y_obst += 20
                score += 1


            if not pygame.mixer.music.get_busy():
                toca_musica("drive.mp3",-1)

        # Imagem do numero de vidas na tela
        for cont_vidas in range(vidas):
            inicio_img_vidas += 45
            screen.blit(vida,(inicio_img_vidas,5))
        inicio_img_vidas = -40

        if vidas==1:
            toca_musica("beep.mp3",0)

        # Texto de pontos na tela
        text = escreve_score(determina_fonte(30),score)
        screen.blit(text,(500,5))

        tempo_jogo = escreve_tempo(tempo,nivel)

        # Nivel do jogo
        nivel = tempo_jogo[1]
        if nivel==0:
            pygame.time.delay(110)
        if nivel==1:
            pygame.time.delay(90)
        if nivel==2:
            pygame.time.delay(70)
        if nivel==3:
            pygame.time.delay(50)
        if nivel==4:
            pygame.time.delay(30)
        if nivel==5:
            pygame.time.delay(10)

        # Tempo de jogo
        texto_tempo = tempo_jogo[0]
        tempo += clock.tick()
        screen.blit(texto_tempo,(20,550))

        i+=1
        if i==3:
            i = 0

        pygame.display.flip()
        
    lista_score.append(score)
    return final,iniciar,score
    

def Main(iniciar,instrucoes):
    #-------------------------- LOOP PRINCIPAL -------------------------------
    while True:
        #-------------------------- TELA INICIAL -------------------------------
        while not iniciar and not instrucoes:
            iniciar, instrucoes = tela_inicial()[0], tela_inicial()[1]

        #-------------------------- LOOP DO JOGO -------------------------------
        if iniciar:
            resultado = jogo(iniciar)
            final = resultado[0]
            iniciar = resultado[1]
            score = resultado[2]
            if final:
                toca_musica("game_over.mp3",0)
                jogar_novamente = tela_final(iniciar,score)
                final = jogar_novamente[0]
                iniciar = jogar_novamente[1]

        else:
            while instrucoes and not iniciar:
                iniciar = intrucoes()
                
Main(iniciar,instrucoes)
            
