#MARS
from time import time
import sys, pygame
import random

pygame.init()

#CORES:
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHT_BLUE = (70,70,255)

#SETAR TELA:
tela = (800, 600)
screen = pygame.display.set_mode(tela)
screen.fill(WHITE)

#SONS
mus = True
tiro_player=pygame.mixer.Sound("arminha.wav")
tiro_player.set_volume(.5)
pygame.mixer.music.load("intro.mp3")
acertou_inimigo = pygame.mixer.Sound("hit.WAV")
NANI = pygame.mixer.Sound("nani.WAV")
acertou_inimigo.set_volume(.5)
game_over = pygame.mixer.Sound("game_over.ogg")
game_over.set_volume(.7)
perdeu_vida = pygame.mixer.Sound("perdeu_vida.ogg")
pygame.mixer.set_num_channels(50)

#TÍTULO:
pygame.display.set_caption("MARS")

#IMPORTANDO NAVE:
nave = pygame.image.load("nave.png").convert_alpha()
x_nave = 0
y_nave = 200

#PONTUACÃO
pontos = 0
ultimo_blit = 0

#IMAGEM DE FUNDO:
espaco = pygame.image.load("space.jpg").convert_alpha()
instrucao = pygame.image.load("instrucao_menu.png").convert_alpha()
acabou = pygame.image.load("over.png").convert_alpha()
score = pygame.image.load("score.png").convert_alpha()

#INIMIGOS:
inimigo_01 = pygame.image.load("mob1.png").convert_alpha()
inimigo_02 = pygame.image.load("mob2.png").convert_alpha()
inimigo_03 = pygame.image.load("mini_boss.png").convert_alpha()
inimigo_04 = pygame.image.load("boss.png").convert_alpha()
explosao_monstro = pygame.image.load("explosao.png").convert_alpha()
explosao_boss = pygame.image.load("explosao_boss.jpg").convert_alpha()
lista_inimigos=[[inimigo_01,69,68],[inimigo_02,57,47],[inimigo_03,300,273],[inimigo_04,350,331]]
inimigos_na_tela = []
tempo_spawn_inimigo = 0
lista_explosao=[]

#TIROS:
red_bullets = []
bullets_boss = []
bullets = []
lista_pos_boss = [4, 2, 0, -2, -4]
lista_pos_mini = [2, 0, -2]

#lista de numero de inimigos por wave
lista_waves_inimigos_fases = [4,4,5,5,6,4,4,1,1,0]
indice_lista_waves = 0
nivel_fase = 1

#LEVEL_IMAGENS:
lvl_01 = pygame.image.load("level_1.png").convert_alpha()
lvl_02 = pygame.image.load("level_2.png").convert_alpha()
lvl_final = pygame.image.load("level_final.png").convert_alpha()
stage = pygame.image.load("stage_clear.png").convert_alpha()
mostrar_level = True
transi_flag = True

#CLOCK:
clock = pygame.time.Clock()

#INTRO:
i=1
intro = True
empresa = pygame.image.load("logo.png").convert_alpha()
game_logo = pygame.image.load("game_logo.png").convert_alpha()

#MENU:
menu = True
inst = True

#RAKING
lista_rank = [000, 000, 000]
lista_nome =["AAA", "AAA", "AAA"]
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#PLAYER
vidas = 3
lista_x_vidas=[0, 80, 160]
imagem_vida = pygame.transform.scale(nave, (66, 33))
recomeco=True

def text_objects(text, font):
  textSurface = font.render(text, True, BLACK)
  return textSurface, textSurface.get_rect()

def introducao():
    i=1
    global intro
    while i<256:
        empresa.set_alpha(i)
        screen.blit(empresa,[300,200])
        intro = False
        i+=1
        clock.tick(60)
        pygame.display.flip()
        
def transicao():
    x = 0
    y = 200
    x_boss = 1000
    y_boss = 200
    flag = False
    pygame.mixer.music.stop()
    NANI.play()
    while True:
        blitar_espaco()
        screen.blit(nave, [x,y])
        screen.blit(inimigo_04, [x_boss,y_boss])
        
        if x < 250: 
            x += 3
        if x >=250 and x<=300:
            text = 'OMAE WA MOU SHINDEIRU!!!'
            fonte = pygame.font.Font("freesansbold.ttf", 25)
            mensagem = fonte.render(text, 1, RED)
            screen.blit(mensagem, (160, 160))
        if x >= 250  and x_boss >= 550:
            x_boss -= 3
            if x_boss <= 550:
                flag = True
        if flag:
            if x_boss>=500 and x_boss <=700:
              text2 = 'NANI!!!'
              fonte = pygame.font.Font("freesansbold.ttf", 25)
              mensagem = fonte.render(text2, 1, RED)
              screen.blit(mensagem, (600, 180))
            x_boss += 7
            if x_boss > 800:
                x += 5
            if x > 800:
                global transi_flag
                transi_flag = False
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(80)
    pygame.mixer.music.play(-1)
        
    
def instruir():
    global inst
    while inst:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            	pygame.quit()
            	sys.exit()
            rato = pygame.mouse.get_pos()
            pres = pygame.mouse.get_pressed()[0]
            screen.blit(espaco,[0, 0])
            screen.blit(instrucao,[65,100])
            #botao 1
            pygame.draw.rect(screen, GREEN, (350,500,100,50))
            
            if 350+100 > rato[0]>350 and 500+50> rato[1]> 500:
                pygame.draw.rect(screen, RED, (350,500,100,50))
                if pres:
                    inst = False
            smallText=pygame.font.Font("freesansbold.ttf",18)
            textSurf, textRect = text_objects("Jogar",smallText)
            textRect.center = ( (350+(100/2)), (500+(50/2)) )
            screen.blit(textSurf, textRect)
            pygame.display.update()
        
def iniciar_menu(menu):
    while menu:
        mouse = pygame.mouse.get_pos()
        pres = pygame.mouse.get_pressed()[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        screen.blit(game_logo, [240,140])
        if 200+100 > mouse[0]>200 and 400+50> mouse[1]> 400:
            pygame.draw.rect(screen, RED, (200,400,100,50))
            if pres:
                menu = False
                break
        else:
            pygame.draw.rect(screen, GREEN, (200,400,100,50))
        
        if 500+100 > mouse[0]>500 and 400+50> mouse[1]> 400:
            pygame.draw.rect(screen, RED, (500,400,100,50))
            if pres:
                menu = False
                instruir()
        else:
            pygame.draw.rect(screen, GREEN, (500,400,100,50))
        #botao 1
        smallText=pygame.font.Font("freesansbold.ttf",18)
        textSurf, textRect = text_objects("Começar",smallText)
        textRect.center = ( (200+(100/2)), (400+(50/2)) )
        screen.blit(textSurf, textRect)
        #botao 2
        smallText=pygame.font.Font("freesansbold.ttf",18)
        textSurf, textRect = text_objects("Instruções",smallText)
        textRect.center = ( (500+(100/2)), (400+(50/2)) )
        screen.blit(textSurf, textRect)

        pygame.display.update()
    return False

def mostrar_resultado():
  global pontos
  global tempo
  global vidas
  if vidas < 0:
    vidas = 0
  resultado = "Seus pontos: " + str(pontos)
  temporal = "Seu tempo total: " + str(int(tempo))
  nome1 = '1st ' + str(lista_nome[0]) + " - " + str(lista_rank[0])
  nome2 = '2nd ' + str(lista_nome[1]) + " - " + str(lista_rank[1])
  nome3 = '3rd ' + str(lista_nome[2]) + " - " + str(lista_rank[2])
  fonte1 = pygame.font.Font("freesansbold.ttf", 25)
  smallText = pygame.font.Font("freesansbold.ttf",18)
  textSurf, textRect = text_objects("Jogar Novamente", smallText)
  textRect.center = ( (300 + (200/2)), (500+(50/2)))
  mensagem3 = fonte1.render(nome1, 1, WHITE)
  mensagem4 = fonte1.render(nome2, 1, WHITE)
  mensagem5 = fonte1.render(nome3, 1, WHITE)
  while True:
    mouse = pygame.mouse.get_pos()
    pres = pygame.mouse.get_pressed()[0]
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.blit(espaco, [0,0])
    pygame.draw.rect(screen, LIGHT_BLUE, (100, 100, 600, 375))
    screen.blit(score, [250, 50])
    mensagem1 = fonte1.render(resultado, 1, WHITE)
    mensagem2 = fonte1.render(temporal, 1, WHITE)
    screen.blit(mensagem1, (295, 400))
    screen.blit(mensagem2, (295, 430))
    screen.blit(mensagem3, (200, 180))
    screen.blit(mensagem4, (200, 210))
    screen.blit(mensagem5, (200, 240))
    if 300 + 200 > mouse[0] > 300 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(screen, RED, (300, 500, 200, 50))
            if pres:
                menu = True
                break
    else:
      pygame.draw.rect(screen, GREEN, (300,500,200,50))
    screen.blit(textSurf, textRect)
    pygame.display.update()


def apresentar_level(lvl):
  cont = 0
  while True:
    screen.fill(WHITE)
    screen.blit(lvl, [0,225])
    pygame.display.update()
    cont+=1
    if cont == 250:
      return False
      break

def colisao(x_nave,x_max,y_nave,y_max,w_nave,w_max,h_nave,h_max,condição):
  if condição:
    if  x_nave <= x_max :
      x_nave = x_max
    if x_nave + w_nave >= x_max + w_max:
      x_nave = (x_max + w_max) - w_nave
    if y_nave <= y_max:
      y_nave = y_max
    if y_nave + h_nave >= y_max + h_max:
      y_nave = (y_max + h_max) - h_nave
  return x_nave, y_nave

def atirar(x_tiro, y_tiro, last_time):
  if time()-last_time>0.2:
    pygame.mixer.Sound.play(tiro_player)
    tiro_player.play()
    bullets.append(x_nave+82)
    bullets.append(y_nave+26)
    last_time=time()
  return last_time

def blitar_tiro_player():
  for b in range(0,len(bullets),2):
        bullets[b] += 10

  for b in range(0,len(bullets),2):
        if len(bullets) > 0:
            if bullets[0] > 800:
                del bullets[b + 1]
                del bullets[b]
                
  for b in range(0,len(bullets),2):
        pygame.draw.rect(screen, GREEN, (bullets[b], bullets[b+1], 10, 5))

def acertar_tiro_player():
    global pontos
    global tempo
    if len(bullets)>0:
        cont=0
        while cont<len(bullets):
            for a in range(len(inimigos_na_tela)):
                if bullets[cont]<=inimigos_na_tela[a][1]+ inimigos_na_tela[a][4]<=bullets[cont]+inimigos_na_tela[a][4] and inimigos_na_tela[a][2]<=bullets[cont+1]+5<=inimigos_na_tela[a][2]+inimigos_na_tela[a][5]:
                    acertou_inimigo.play(1)
                    del bullets[cont+1]
                    del bullets[cont]
                    inimigos_na_tela[a][6] -= 2
                    if inimigos_na_tela[a][6] == 0:
                        tempo_ini=tempo
                        explosao(inimigos_na_tela[a][1],inimigos_na_tela[a][2],inimigos_na_tela[a][0],tempo_ini)
                        pontos += 100
                        if inimigos_na_tela[a][0]==2:
                          pontos += 400
                        if inimigos_na_tela[a][0]==3:
                          pontos += 900
                        del inimigos_na_tela[a]
                    cont -= 2
                    break
            cont += 2
def explosao(x_exp,y_exp,tipo_exp,tempo_ini):
  global lista_explosao
  global tempo
  lista=[]
  lista.append(tipo_exp)
  lista.append(x_exp)
  lista.append(y_exp)
  lista.append(tempo_ini)
  lista_explosao.append(lista)
  

def blitar_explosao(lista_explosao,tempo):
  if len(lista_explosao)>0:
    i=0
    while i<len(lista_explosao):
      if lista_explosao[i][0] <=1:
        screen.blit(explosao_monstro,(lista_explosao[i][1],lista_explosao[i][2]))
      if lista_explosao[i][0] >=2:
        screen.blit(explosao_boss,(lista_explosao[i][1],lista_explosao[i][2]))
      if tempo - lista_explosao[i][3]>=0.3:
        del lista_explosao[i]
        i-=1
      i+=1

    
def barra_de_vida_boss(vida):
  barra = 600 - vida
  pygame.draw.rect(screen, RED, (770, 0, 30, 600))
  pygame.draw.rect(screen, GREEN, (770, barra, 30, 600))
  return barra

def pontuar():
  global pontos
  text = 'score: '+str(pontos)
  fonte = pygame.font.Font("freesansbold.ttf", 25)
  mensagem = fonte.render(text, 1, (255, 255, 255))
  screen.blit(mensagem, (10, 10))


def mostrar_tempo(tempo,ultimo_blit):
  tempo=int(tempo)
  text = str(ultimo_blit)
  fonte = pygame.font.Font("freesansbold.ttf", 25)
  mensagem = fonte.render(text, 1, (255, 255, 255))
  if ultimo_blit != tempo:
    ultimo_blit=tempo
  screen.blit(mensagem, (380, 10))
  return ultimo_blit

  
def mostrar_pontuacao(tempo):
  global pontos
  pontos -= int(tempo)

def gerar_inimigos(inimigos_na_tela,num_inimigos, lista_y_inimigo,cont,bosses):
  x_inimigo = 900
  if bosses==0:
    tipo_inimigo=random.randint(0,1)
    status_inimigo=[tipo_inimigo,x_inimigo,lista_y_inimigo[cont]*cont,True,lista_inimigos[tipo_inimigo][1],lista_inimigos[tipo_inimigo][2],12]
    inimigos_na_tela.append(status_inimigo)
  if bosses==1:
    tipo_inimigo=2
    status_inimigo=[tipo_inimigo,x_inimigo,lista_y_inimigo[cont]*cont,True,lista_inimigos[tipo_inimigo][1],lista_inimigos[tipo_inimigo][2],200]
    inimigos_na_tela.append(status_inimigo)
  if bosses==2:
    tipo_inimigo=3
    status_inimigo=[tipo_inimigo,x_inimigo,lista_y_inimigo[cont]*cont,True,lista_inimigos[tipo_inimigo][1],lista_inimigos[tipo_inimigo][2],600]
    inimigos_na_tela.append(status_inimigo)
    

def apresentar_clear():
  pygame.time.delay(500)
  screen.blit(stage, [0, 225])
  global bullets
  bullets = []
  global red_bullets
  red_bullets = []
  global bullets_boss
  bullets_boss = []
  pygame.display.update()
  pygame.time.delay(2000)

def recomecar_jogo(tempo,metodo):
  global bullets
  bullets = []
  global red_bullets
  red_bullets = []
  global bullets_boss
  bullets_boss = []
  global pontos
  pontos=0
  global x_nave
  x_nave = 0
  global y_nave
  y_nave = 200
  global indice_lista_waves
  indice_lista_waves=0
  global nivel_fase
  nivel_fase=1
  global mostrar_level
  mostrar_level=True
  global menu
  menu = True
  global inst
  inst = True
  global vidas
  vidas=3
  global lista_x_vidas
  lista_x_vidas=[0,80,160]
  global transi_flag
  transi_flag = True
  global seconds
  seconds=pygame.time.get_ticks()-tempo
  global inimigos_na_tela
  inimigos_na_tela = []
  global recomeco
  recomeco=False
  pygame.display.update()
  if metodo==2:
    return nivel_fase, indice_lista_waves, mostrar_level
  else:
    return lista_x_vidas, menu, vidas
    
def acrescentar_inimigos(nivel_fase,num_waves,num_inimigos,inimigos_na_tela,indice_lista_waves,mostrar_level,tempo):
  if nivel_fase == 1:
    if mostrar_level:
      mostrar_level= apresentar_level(lvl_01)
    if len(inimigos_na_tela)==0:
    #if seconds-tempo_spawn_inimigo>=3:
      #tempo_spawn_inimigo=seconds
      lista_y_inimigo=[]
      for i in range(1,num_inimigos+1):
        lista_y_inimigo.append(500//4)
      for i in range(num_inimigos):
        gerar_inimigos(inimigos_na_tela, num_inimigos, lista_y_inimigo, i, 0)
      if indice_lista_waves == 5:
        apresentar_clear()
        nivel_fase = 2
        mostrar_level = True
      indice_lista_waves += 1
    
  if nivel_fase == 2:
      if mostrar_level:
          mostrar_level= apresentar_level(lvl_02)
      if len(inimigos_na_tela)==0:
    #if seconds-tempo_spawn_inimigo >= 3:
      #tempo_spawn_inimigo=seconds
        lista_y_inimigo=[]
        for i in range(1,num_inimigos+1):
          lista_y_inimigo.append(500//4)
        for i in range(num_inimigos):
          if indice_lista_waves == 7:
            gerar_inimigos(inimigos_na_tela,num_inimigos, lista_y_inimigo,i,1)
          if indice_lista_waves < 7:
            gerar_inimigos(inimigos_na_tela,num_inimigos, lista_y_inimigo,i,0)
        if indice_lista_waves == 8:
          apresentar_clear()
          nivel_fase=3
          mostrar_level=True
          indice_lista_waves-=1
        indice_lista_waves+=1

  if nivel_fase == 3:
    if mostrar_level:
      mostrar_level= apresentar_level(lvl_final)
    if len(inimigos_na_tela)==0:
    #if seconds-tempo_spawn_inimigo>=3:
      #tempo_spawn_inimigo=seconds
        lista_y_inimigo=[]
        for i in range(1,num_inimigos+1):
          lista_y_inimigo.append(500//4)
        #BOSS
        for i in range(num_inimigos):
          gerar_inimigos(inimigos_na_tela,num_inimigos, lista_y_inimigo,i,2)
        if indice_lista_waves == 9:
          apresentar_clear()
          mostrar_pontuacao(tempo)
          rankear()
          mostrar_resultado()
          return recomecar_jogo(tempo,2)
        indice_lista_waves+=1
          
  
  return nivel_fase,indice_lista_waves,mostrar_level

def movimentacao_inimigo(inimigos_na_tela, count):
    if 700<inimigos_na_tela[count][1]<=900 and inimigos_na_tela[count][0]<=1:
      inimigos_na_tela[count][1],  inimigos_na_tela[count][2]= colisao(inimigos_na_tela[count][1], 0, inimigos_na_tela[count][2], 0, lista_inimigos[inimigos_na_tela[count][0]][1], 800, lista_inimigos[inimigos_na_tela[count][0]][2], 600,False)
      inimigos_na_tela[count][1]-=1
    elif 450<inimigos_na_tela[count][1]<=900 and inimigos_na_tela[count][0]>=2:
      inimigos_na_tela[count][1],  inimigos_na_tela[count][2]= colisao(inimigos_na_tela[count][1], 0, inimigos_na_tela[count][2], 0, lista_inimigos[inimigos_na_tela[count][0]][1], 800, lista_inimigos[inimigos_na_tela[count][0]][2], 600,False)
      inimigos_na_tela[count][1]-=1
   
    else:
      inimigos_na_tela[count][1],  inimigos_na_tela[count][2]= colisao(inimigos_na_tela[count][1], 0, inimigos_na_tela[count][2], 0, lista_inimigos[inimigos_na_tela[count][0]][1], 800, lista_inimigos[inimigos_na_tela[count][0]][2], 600,True)

      if inimigos_na_tela[count][2] == 600-lista_inimigos[inimigos_na_tela[count][0]][2]:
        inimigos_na_tela[count][3]=False

      if inimigos_na_tela[count][2] == 0:
        inimigos_na_tela[count][3]=True
    
      if inimigos_na_tela[count][3]:
        inimigos_na_tela[count][2]+=2
      
      if inimigos_na_tela[count][3]==False:
        inimigos_na_tela[count][2]-=2
      opt = random.randint(0,100)
      if opt == 7:
        atirar_inimigos(inimigos_na_tela[count][1],inimigos_na_tela[count][2], inimigos_na_tela[count][4],inimigos_na_tela[count][5])
      if opt == 87 and inimigos_na_tela[count][0] == 3:
        atirar_boss(inimigos_na_tela[count][1],inimigos_na_tela[count][2], inimigos_na_tela[count][4],inimigos_na_tela[count][5], 5)
      if opt == 45 and inimigos_na_tela[count][0] == 2:
        atirar_boss(inimigos_na_tela[count][1],inimigos_na_tela[count][2], inimigos_na_tela[count][4],inimigos_na_tela[count][5], 3)
    screen.blit(lista_inimigos[inimigos_na_tela[count][0]][0],[inimigos_na_tela[count][1], inimigos_na_tela[count][2]])
    return inimigos_na_tela[count][1],  inimigos_na_tela[count][2]

def spawn_inimigos(count):
      for i in range(len(inimigos_na_tela)):
        inimigos_na_tela[count][1],  inimigos_na_tela[count][2] = movimentacao_inimigo(inimigos_na_tela, i)
        count+=1
      return 0

def blitar_espaco():
    screen.blit(espaco,[0, 0])

def blitar_personagem():
    screen.blit(nave, [x_nave, y_nave])

def atirar_inimigos(x_inimigo, y_inimigo, w_inimigo, h_inimigo):
  red_bullets.append(x_inimigo)
  red_bullets.append(y_inimigo + h_inimigo/2)

def atirar_boss(x_boss, y_boss, w_boss, h_boss, num_tiro):
  for i in range(num_tiro):
    bullets_boss.append(x_boss)
    bullets_boss.append(y_boss + h_boss // 2)

def blitar_tiro_inimigo():
  for r in range(0,len(red_bullets),2):
        red_bullets[r] -= 6
  for r in range(0,len(red_bullets),2):
      if len(red_bullets) > 0:
          if red_bullets[0] < 0:
              del red_bullets[1]
              del red_bullets[0]  
  for r in range(0 , len(red_bullets) , 2):
        pygame.draw.rect(screen, RED, (red_bullets[r], red_bullets[r+1], 10, 5))

def blitar_tiro_boss():
  if indice_lista_waves == 9:
    cont = 0
    for r in range(0,len(bullets_boss),2):
      bullets_boss[r+1] += lista_pos_boss[cont]
      bullets_boss[r] -= 5
      cont += 1
      if cont > 4:
        cont = 0
    for r in range(0,len(bullets_boss),2):
        if len(bullets_boss) > 0:
            if bullets_boss[0] < 0:
                del bullets_boss[1]
                del bullets_boss[0]  
    for r in range(0 , len(bullets_boss) , 2):
      pygame.draw.circle(screen, RED, [bullets_boss[r], bullets_boss[r+1]], 10)

  else:
    cont = 0
    for r in range(0,len(bullets_boss),2):
      bullets_boss[r+1] += lista_pos_mini[cont]
      bullets_boss[r] -= 5
      cont += 1
      if cont > 2:
        cont = 0
    for r in range(0,len(bullets_boss),2):
        if len(bullets_boss) > 0:
            if bullets_boss[0] < 0:
                del bullets_boss[1]
                del bullets_boss[0]  
    for r in range(0 , len(bullets_boss) , 2):
      pygame.draw.circle(screen, RED, [bullets_boss[r], bullets_boss[r+1]], 10)

      
def verificar_tiro_inimigo(x_nave,y_nave,vidas,lista_x_vidas):
  if len(red_bullets)>0:
        cont=0
        while cont<len(red_bullets):
            if red_bullets[cont] <= x_nave+82 <= red_bullets[cont] + 82 and y_nave <= red_bullets[cont+1]+5 <= y_nave + 43:
                perdeu_vida.play(0)
                del red_bullets[cont+1]
                del red_bullets[cont]
                vidas -= 1
                if vidas >= 0:
                  del lista_x_vidas[vidas]
                
                cont -= 2
            cont += 2
  if len(bullets_boss)>0:
        cont=0
        while cont<len(bullets_boss):
            if bullets_boss[cont]<=x_nave+82<=bullets_boss[cont]+82 and y_nave <= bullets_boss[cont+1] + 5 <= y_nave+43:
                del bullets_boss[cont+1]
                del bullets_boss[cont]
                vidas -= 1
                if vidas >= 0:
                  del lista_x_vidas[vidas]
                
                cont -= 2
            cont += 2
  return vidas, lista_x_vidas

def perder_jogo():
  pygame.mixer.music.stop()
  game_over.play(0)
  cont = 600
  cont2 = 0
  while True:
    screen.fill(BLACK)
    screen.blit(acabou, [0, cont])
    pygame.display.flip()
    if cont >= 0:
      cont -= 0.5
    else:
      cont2 += 1
    if cont2 > 250:
      rankear()
      break
  
def blitar_vidas(vidas, lista_x_vidas,tempo):
  menu = False
  if vidas >= 0:
    for i in range(len(lista_x_vidas)):
      screen.blit(imagem_vida, [lista_x_vidas[i],550])
  else:
    mostrar_pontuacao(tempo)
    perder_jogo()
    mostrar_resultado()
    menu = True
    return recomecar_jogo(tempo,1)
  return lista_x_vidas, menu, vidas

def rankear():
  global pontos
  if pontos >= lista_rank[2]:
    lista_rank[2] = pontos
    lista_rank.sort()
    lista_rank.reverse()
    indice = lista_rank.index(pontos)
    nome = colocar_nome()
    lista_nome[2] = nome
    for i in range(indice, len(lista_nome)):
      aux = lista_nome[i]
      lista_nome[i] = lista_nome[indice]
      lista_nome[indice] = aux

def colocar_nome():
    cont = 0
    cont_nome = 0
    letra_nome = [alfabeto[0], alfabeto[0], alfabeto[0]]
    textao = "INSIRA SUAS INICIAIS: "
    instrucao = "Para trocar de letras, utilize as setas."
    instrucao2 = "Para confirmar, pressione a tecla SPACE!"
    fonte1 = pygame.font.Font("freesansbold.ttf", 25)
    fonte2 = pygame.font.Font("freesansbold.ttf", 40)
    fonte3 = pygame.font.Font("freesansbold.ttf", 60)
    mensagem4 = fonte2.render(textao, 1, WHITE)
    mensagem5 = fonte1.render(instrucao, 1, WHITE)
    mensagem6 = fonte1.render(instrucao2, 1, WHITE)

    while True:
        screen.fill(BLACK)
        mensagem1 = fonte3.render(letra_nome[0], 1, WHITE)
        mensagem2 = fonte3.render(letra_nome[1], 1, WHITE)
        mensagem3 = fonte3.render(letra_nome[2], 1, WHITE)
        screen.blit(mensagem1, (320, 250))
        screen.blit(mensagem2, (370, 250))
        screen.blit(mensagem3, (420, 250))
        screen.blit(mensagem4, (170, 100))
        screen.blit(mensagem5, (100, 400))
        screen.blit(mensagem6, (100, 450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if cont < 25:
                   cont += 1
                else:
                   cont = 0
            if keys[pygame.K_LEFT]:
                if cont < 0:
                   cont = 25
                else:
                   cont -= 1
            if keys[pygame.K_SPACE]:
                if cont_nome == 2:
                  nome_final = ''
                  for i in range(3):
                    nome_final += letra_nome[i]
                  return nome_final
                cont_nome += 1
                cont = 0
        letra_nome[cont_nome] = alfabeto[cont]
        pygame.display.update()

def musica():
     pygame.mixer.music.play(-1)
     pygame.display.update()

last_time = 0

while True:
    #MENU:
    if mus:
        musica()
        pygame.time.delay(2000)
        mus=False
    #INTRO:
    if intro:
      introducao()
    #MENU:
    if menu:
      menu = iniciar_menu(menu)
    #CUT SCENE:
    if transi_flag:
      transicao()
      start_ticks=pygame.time.get_ticks() 
    seconds = (pygame.time.get_ticks() - start_ticks)/1000
    tempo = seconds
    blitar_espaco()
    lista_x_vidas, menu, vidas = blitar_vidas(vidas,lista_x_vidas,tempo)
    blitar_explosao(lista_explosao,tempo)

    if recomeco:
      nivel_fase,indice_lista_waves,mostrar_level = acrescentar_inimigos(nivel_fase,len(lista_waves_inimigos_fases),lista_waves_inimigos_fases[indice_lista_waves],inimigos_na_tela,indice_lista_waves,mostrar_level,tempo)

    spawn_inimigos(0)
    blitar_personagem()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and keys[pygame.K_a]:
    	x_nave += 4
    if keys[pygame.K_d]:
        x_nave += 4
    if keys[pygame.K_a]:
        x_nave -= 4
    if keys[pygame.K_w]:
        y_nave -= 4
    if keys[pygame.K_s]:
        y_nave += 4
    if keys[pygame.K_SPACE]:
      last_time=atirar(x_nave,y_nave,last_time)
    blitar_tiro_player()
    blitar_tiro_inimigo()
    blitar_tiro_boss()
    vidas, lista_x_vidas = verificar_tiro_inimigo(x_nave,y_nave,vidas,lista_x_vidas)
    acertar_tiro_player()
    pontuar()
    ultimo_blit = mostrar_tempo(tempo,ultimo_blit)
    if indice_lista_waves == 9 and len(inimigos_na_tela) > 0:
      barra_verde = barra_de_vida_boss(inimigos_na_tela[0][6])
    x_nave,y_nave = colisao(x_nave, 0, y_nave, 0, 88, 800, 43, 600, True)
    pos_nave=pygame.Rect(x_nave,y_nave,88,43)
    for a in range(len(inimigos_na_tela)):
      inimigo=pygame.Rect(inimigos_na_tela[a][1],inimigos_na_tela[a][2],inimigos_na_tela[a][4],inimigos_na_tela[a][5])
      if pos_nave.colliderect(inimigo):
        x_nave=inimigos_na_tela[a][1]-88
    if recomeco == False:
      recomeco=True
    clock.tick(60)
    pygame.display.update()
