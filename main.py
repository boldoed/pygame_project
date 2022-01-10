import pygame
import sys
import os 


pygame.init()
FPS = 50
size = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def start_screen():
    # intro_text = ["ЗАСТАВКА", "",
    #               "Правила игры",
    #               "Если в правилах несколько строк,",
    #               "приходится выводить их построчно"]
    k = 0
    fon = pygame.transform.scale(load_image('zastavka.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(load_image('zastavka1.png'), (WIDTH, HEIGHT))
    # font = pygame.font.Font(None, 30)
    # text_coord = 50
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('white'))
    #     intro_rect = string_rendered.get_rect()
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     intro_rect.x = 10
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN) and k == 0:
                screen.blit(fon1, (0, 0))
                k += 1
            elif (event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN) and k != 0:
                return
                # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

# def load_level(filename):
#     filename = "data/" + filename
#     # читаем уровень, убирая символы перевода строки
#     with open(filename, 'r') as mapFile:
#         level_map = [line.strip() for line in mapFile]

#     # и подсчитываем максимальную длину    
#     max_width = max(map(len, level_map))

#     # дополняем каждую строку пустыми клетками ('.')    
#     return list(map(lambda x: x.ljust(max_width, '.'), level_map))


# tile_images = {
#     'wall': load_image('box.png'),
#     'empty': load_image('grass.png')
# }
# player_image = load_image('mario.png')

# tile_width = tile_height = 50

# основной персонаж
# player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
# tiles_group = pygame.sprite.Group()
# player_group = pygame.sprite.Group()


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, tile_type, pos_x, pos_y):
#         super().__init__(tiles_group, all_sprites)
#         self.image = tile_images[tile_type]
#         self.rect = self.image.get_rect().move(
#             tile_width * pos_x, tile_height * pos_y)


# class Player(pygame.sprite.Sprite):
#     def __init__(self, pos_x, pos_y):
#         super().__init__(player_group, all_sprites)
#         self.image = player_image
#         self.rect = self.image.get_rect().move(
#             tile_width * pos_x + 15, tile_height * pos_y + 5)

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0
        
    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
    
    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)

# def generate_level(level):
#     new_player, x, y = None, None, None
#     for y in range(len(level)):
#         for x in range(len(level[y])):
#             if level[y][x] == '.':
#                 Tile('empty', x, y)
#             elif level[y][x] == '#':
#                 Tile('wall', x, y)
#             elif level[y][x] == '@':
#                 Tile('empty', x, y)
#                 new_player = Player(x, y)
#     # вернем игрока, а также размер поля в клетках            
#     return new_player, x, y

start_screen()
# player, level_x, level_y = generate_level(load_level('map1.txt'))

running = True
camera = Camera()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player.rect.x -= 50
        #     if event.key == pygame.K_RIGHT:
        #         player.rect.x += 50
        #     if event.key == pygame.K_UP:
        #         player.rect.y -= 50
        #     if event.key == pygame.K_DOWN:
        #         player.rect.y += 50
    # изменяем ракурс камеры
    # camera.update(player); 
    # обновляем положение всех спрайтов
    for sprite in all_sprites:
        camera.apply(sprite)


    screen.fill(pygame.Color(0, 0, 0))
    # tiles_group.draw(screen)
    # player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)