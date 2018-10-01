import pygame
import bullet

#pygame.init()

#screen = pygame.display.set_mode((400,600))
#pygame.display.set_caption("TouPy")
relogio = pygame.time.get_ticks()
relogioOn = False

def contagem_relogio(tempo): ## ELE FAZ O CALCULO DO TEMPO
    horas_agora = pygame.time.get_ticks()
    global relogio
    if horas_agora >= (relogio + tempo):
        return True
    return False

def setar_relogio(): ## ELE CRIA OS RELOGIOS
    global relogio
    global relogioOn
    relogio = pygame.time.get_ticks()
    relogioOn = True

def setar_timer(tempo): ## ELE CRIA O RELOGIO E VE SE NAO EXISTE, SE QUISER 
    global relogio ## PODE USAR ESTA FUNCAO PARA SE REPETIR
    global relogioOn
    if relogioOn == False:
        setar_relogio()
    else:
        a = contagem_relogio(tempo)
        if a == True:
            relogioOn = False
            return True
        else:
            return None
def check_timer(tempo): ## ELE CHECA SE O TEMPO BATEU
    global relogioOn
    if relogioOn == True:
        a = contagem_relogio(tempo)
        if a == True:
            relogioOn = False
            print ("Tiro")
        else:
            return None
#while True:
#    screen.fill((255,255,255))
#    fonte = pygame.font.Font(None, 50) ## Criar a fonte
#    tempo_vivo = (pygame.time.get_ticks()) // 1000
#    pontuacao = fonte.render(str(tempo_vivo),1,(0,0,0))
#    screen.blit(pontuacao,(300,10))
#    ## relogio
#    for event in pygame.event.get():
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            if event.button == 1:
#                print("aaa")
#                setar_timer(1000)
#    check_timer(1000) ## SE VOCE UTILIZAR SETAR_TIMER AQUI, ELE VAI SEMPRE ATIRAR EM TAL INTERVALO
#    pygame.display.update()

