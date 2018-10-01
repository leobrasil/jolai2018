#features: Carrinho não passa das bordas | Seletor de dificuldade | Melhoria no background
import pygame, sys, os,random
from pygame.locals import *


pygame.init()
pygame.font.init()
pygame.display.set_caption('Car avoider')
font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name,72)
game_font2 = pygame.font.SysFont(font_name,35)
game_font3 = pygame.font.SysFont(font_name,20)
recorde = 0
white = (255,255,255)
grey = (128,128,128)
yellow=(255,255,0)
black=(0,0,0)
vel1 = 0
vel2 = 0


screen = pygame.display.set_mode((956,560),0,32)



player_car = {
    'surface' : pygame.image.load('carro.png').convert_alpha(),
    'position' : [478, 280],
    'speed' : {
        'x' : 0,
        'y' : 0
    }
}


clock = pygame.time.Clock()


def background_img_game():
    background_filename = 'background.png'
    background = pygame.image.load(background_filename).convert()
    screen.blit(background,(0,0))

def background_music():
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)


def create_car():
    global vel1,vel2
    return {
        'surface' : pygame.image.load('carro_amarelo2.png').convert_alpha(),
        'position' : [random.randint(1,870), -64],
        'speed' : random.randint(vel1,vel2)
    }


cars = []





def get_rect(obj):
    return Rect(obj['position'][0],
                obj['position'][1],
                obj['surface'].get_width(),
                obj['surface'].get_height())



def player_car_collided():
    car_rect = get_rect(player_car)
    for car in cars:
        if car_rect.colliderect(get_rect(car)):
            return True
    return False





def move_cars():
    for car in cars:
        car['position'][1] += car ['speed']


def remove_cars():
    for car in cars:
        if car['position'][1] > 560:
            cars.remove(car)




def game_intro():
    global game,vel1,vel2
    intro = True
    background_music()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(grey)
        text = game_font.render('Car Avoider', 1,black)
        play_text = game_font2.render('Pressione (J)Fácil (K)Médio (L)Díficil para jogar ou (S) Para Sair', 1,(white))
        credit_text = game_font3.render('Desenvolvido por Gustavo Sadao e Samuel Olivera',1,(white))
        screen.blit(text,(350,220))
        screen.blit(play_text,(120,300))
        screen.blit(credit_text,(10,540))


        key = pygame.key.get_pressed()


        if  key[K_j]:
            vel1 = 10
            vel2 = 20
            game = True

            return game

        if key[K_k]:
            vel1 = 20
            vel2 = 30
            game = True
            return game

        if key[K_l]:
            vel1 = 30
            vel2 = 40
            game = True
            return game
        if key[K_i]:
            vel1 = 60
            vel2 = 80

            game=True
            return game



        if key[K_s]:
            pygame.quit()

        pygame.display.update()



def game_ticks():
    ticks=20
    return ticks


def main():
    global recorde,vel1,vel2
    tempo = 0
    ticks = game_ticks()
    background_music()


    collided=False
    while game:
        background_img_game()
        if not ticks:
            ticks = game_ticks()
            cars.append(create_car())

        else:
            ticks -= 1

        player_car['speed'] = {'x' : 0, 'y' : 0}

        for event in pygame.event.get():
            pressed_key = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_UP]:
            player_car['speed']['y'] = -20
        if pressed_key[K_DOWN]:
            player_car['speed']['y'] = 20
        if pressed_key[K_LEFT]:
            player_car['speed']['x'] = -20
        if pressed_key[K_RIGHT]:
            player_car['speed']['x'] = 20

        if pressed_key[K_m]:
            pygame.mixer.music.stop()

        if player_car['position'][0]>=906:
            player_car['position'][0]=906

        if player_car['position'][0]<=0:
            player_car['position'][0]=0

        if player_car['position'][1]>=460:
            player_car['position'][1]=460

        if player_car['position'][1]<=0:
            player_car['position'][1]=0


        move_cars()


        for car in cars:
            screen.blit(car['surface'],car['position'])


        if not collided:

            collided = player_car_collided()
            player_car['position'][0] += player_car['speed']['x']
            player_car['position'][1] += player_car['speed']['y']
            screen.blit(player_car['surface'],player_car['position'])


            tempo+=1
            score_text= game_font2.render('Pontos: '+str(tempo),1,(yellow))
            screen.blit(score_text,(10,0))

            if tempo>recorde:
                recorde = tempo



        else:

            pygame.mixer.music.stop()


            text = game_font.render('Perdeu', 1,black)

            replay_text = game_font2.render('(R) Jogar Novamente (M) Menu (S) Sair', 1,(0,0,0))

            result_text=game_font2.render('Pontos: '+str(tempo),1,black)

            recorde_text=game_font2.render('Recorde: '+str(recorde),1,black)

            screen.blit(text,(370,220))

            screen.blit(replay_text,(240,300))

            screen.blit(result_text,(10,0))

            screen.blit(recorde_text,(9,530))


            player_car['position'] = [478, 280]



            if pressed_key[K_m]:
                collided=False
                game_intro()

            if pressed_key[K_r]:
                main()

            if pressed_key[K_s]:
                pygame.quit()
                sys.exit()



        pygame.display.update()
        time_passed = clock.tick(50)

        remove_cars()


game_intro()

main()
