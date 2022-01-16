import pygame
import sys 
import os

def run():
    pygame.init()
    size = WIDTH, HEIGHT = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Перетаскивание')
    bg_color = (255, 255, 0) 
    moving = False
    x, y = 0, 0
    x_new, y_new = 0, 0
    test_card = pygame.transform.scale(load_card_image('rubashka.png'), (64, 96))
    test_card1 = pygame.transform.scale(load_card_image('t.kr.png'), (64, 96))



    while True:
        screen.blit(test_card1, (x + 10, y))
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
        screen.fill((bg_color))   


def load_card_image(name, colorkey=None):
    fullname = os.path.join('data', 'cards', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


run()





