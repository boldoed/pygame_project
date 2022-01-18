import pygame
import os 
import sys
from random import choice
import utility


pygame.init()
FPS = 50
size = WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Пасьянс')
clock = pygame.time.Clock()

cards = os.listdir('data/cards')

def start_screen():
    k = 0
    fon = pygame.transform.scale(utility.load_image('zastavka.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(utility.load_image('zastavka1.png'), (WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN) and k == 0:
                screen.blit(fon1, (0, 0))
                k += 1
            elif (event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN) and k != 0:
                return
        pygame.display.flip()
        clock.tick(FPS)

start_screen()

def move_image():
    bg_color = (60, 170, 60) # Цвет влюбленной жабы
    move_card = rand_card()
    rand1 = pygame.transform.scale(utility.load_card_image(move_card[0]), (64, 96))
    rand2 = pygame.transform.scale(utility.load_card_image(move_card[1]), (64, 96))
    print(move_card)
    print(rand_card)
    moving_xy = False
    moving_qw = False
    x, y = 26, 42
    q, w = 126, 42
    x_new, y_new = 0, 0
    q_new, w_new = 0, 0

    bg_fon = pygame.transform.scale(utility.load_image('table.png'), (WIDTH, HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x < event.pos[0] < x + 64 and y < event.pos[1] < y + 96:
                    moving_xy = True
                if q < event.pos[0] < q + 64 and w < event.pos[1] < w + 96:
                    moving_qw = True
            if event.type == pygame.MOUSEMOTION:
                if moving_xy:
                    x_new, y_new = event.rel
                    x, y = x + x_new, y + y_new
                if moving_qw:
                    q_new, w_new = event.rel
                    q, w = q + q_new, w + w_new
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving_xy = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving_qw = False

        screen.blit(rand2, (q, w))
        screen.blit(rand1, (x, y))
        
        pygame.display.flip()
        screen.blit(bg_fon, (0, 0))
        
        
        clock.tick(FPS)

def rand_card():
    card_list = []
    for i in range(2):
        rand_c = choice(cards)
        #rand_cc = pygame.transform.scale(utility.load_card_image(rand_c), (64, 96))
        card_list.append(rand_c)
        cards.remove(rand_c)



    return card_list

rand_card()
move_image()



# class Card(object):
#     def __init__(self, val, suit):
#         self.card_tex = pygame.transform.scale(utility.load_card_image(f'{val}.{suit}.png'), (64, 96))
#         self.card_back_tex = pygame.transform.scale(utility.load_image('rubashka.png'), (64, 96))
#         self.suit = suit
#         self.value = val
#         self.revealed = False


#     def draw(self, screen, pos):
#         if self.revealed:
#             screen.blit(self.card_tex, pos)
#         else:
#             screen.blit(self.card_back_tex, pos)

# Card('2', 'bu')





