import pygame
import sys
import os 
from random import choice


pygame.init()
FPS = 50
size = WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Пасьянс')
clock = pygame.time.Clock()

def start_screen():
    k = 0
    fon = pygame.transform.scale(load_image('zastavka.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(load_image('zastavka1.png'), (WIDTH, HEIGHT))
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

    
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def load_card_image(name, colorkey=None):
    fullname = os.path.join('data', 'cards', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

start_screen()

def move_image():
    bg_color = (60, 170, 60) # Цвет влюбленной жабы
    test_card = pygame.transform.scale(load_card_image('rubashka.png'), (64, 96))
    moving = False
    x, y = 26, 42
    x_new, y_new = 0, 0
    bg_fon = pygame.transform.scale(load_image('table.png'), (WIDTH, HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x < event.pos[0] < x + 64 and y < event.pos[1] < y + 96:
                    moving = True
            if event.type == pygame.MOUSEMOTION:
                if moving:
                    x_new, y_new = event.rel
                    x, y = x + x_new, y + y_new
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                moving = False
    
        screen.blit(test_card, (x, y))

        pygame.display.flip()
        screen.blit(bg_fon, (0, 0))
        
        clock.tick(FPS)




cards = os.listdir('data/cards')
print(cards)


move_image()