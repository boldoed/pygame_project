import pygame,sys,os
import random
# Define some colors  лкм - рисуем кубик в клетку, пкм - стираем кубик(закрашиваем белым)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
pygame.init()
# окно
action = False

n=4# количество клеток квадратного поля игры
width  = 48#ширина клетки( и объекта)
height = 48#высота клетки ( и объекта)
playr = None
margin = 5# промежуток между клетками
x=None
y=None
window = pygame.display.set_mode(((width +margin)*n+margin,(height+margin)*n+margin))# создаём окно
pygame.display.set_caption('Masha and Misha') # титул строка
screen = pygame.Surface(((width +margin)*n+margin,(height+margin)*n+margin)) # создаем игровое поле(экран)
all_s = []

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.image=pygame.image.load(filename) # создаем рисунок-загрузка из файла
        self.action = False
        self.rect = self.image.get_rect() # представляем его прямоугольником
        
        self.w = self.image.get_width()   #ширина
        self.h = self.image.get_height()  #высота
        all_s.append(self)       
       
        self.row = None
        self.column = None
    def bum (self):# проверка попадания мышки на объект
       
        if self.x<mp[0]<self.x+self.w and self.y<mp[1]<self.y+self.h:           
            self.action = True# объект активирован                         
        else:
            self.action = False# для избежания случая активации одновременно
                               #  двух объектов           
           
           
    
    def mouv(self):# функция перемещения объекта
        a = self.x # первоначальные координаты объекта
        b = self.y        
       
        if e.key == pygame.K_LEFT:
            if self.x >margin and self.action == True:
                self.x -= margin+width                                               
                self.action = False# запрет на перемещение               
                grid[ b // (height + margin)][ a // (width + margin)] =0
              
        if e.key == pygame.K_RIGHT:
            if self.x <(width +margin)*(n-1)and self.action == True:
                self.x += margin+width               
                self.action = False
                grid[ b // (height + margin)][ a // (width + margin)] =0
        if e.key == pygame.K_UP:
            if self.y >margin and self.action == True:
                self.y -=height+margin                    
                self.action = False# запрет на перемещение
                grid[ b // (height + margin)][ a // (width + margin)] =0
        if e.key == pygame.K_DOWN:
            if self.y <(height+margin)*(n-1)and self.action == True:
                self.y += height+margin         
                self.action = False# запрет на перемещение
                grid[ b // (height + margin)][ a // (width + margin)] =0
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        if grid[self.row][self.column] ==1:
            self.x = a
            self.y = b
           
              
    def mesto(self):              
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)            
        grid[self.row][self.column] = 1
        print(grid)
    def render (self ):# отображение обьекта на игровом поле(экране)
        screen.blit(self.image,(self.x,self.y))

    
hero1 = Sprite(margin,margin,('abcd.png'))
hero2 = Sprite(margin+(width +margin),margin,('abcd1.png'))
hero3 = Sprite((width +margin)*2+margin,margin,('abcd2.png'))


done = True# некая переменная
grid = []
for row in range(n):
    # заполняем пустую матрицу
    # 10 х 10  grid[row,column]
    grid.append([])
    for column in range(n):
        grid[row].append(0)
while done:# условие существования игрового цикла
    
    #pygame.mixer.music.stop()
   
    screen.fill((0,0,90))
    for e in pygame.event.get():# для любого события
        
        if e.type == pygame.QUIT:# если было закрытие окна
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN : # если событие мышь                                      
            if pygame.mouse.get_pressed()[0]:#если  была нажата лкм
                mp = pygame.mouse.get_pos()
                for i in all_s :#
                    i.bum() # выбор объекта
                
        # Перемещение объекта с помощью курсора
        if e.type == pygame.KEYDOWN: # если была нажата клавиша
             for i in all_s:
                i.mouv()
    
    
    for row in range(n):# рисуем игровое поле
            for column in range(n):
                color = WHITE
                pygame.draw.rect(screen,
                             color,
                             [(margin+width)*column+margin,
                              (margin+height)*row+margin,
                              width,
                              height])    
   
    for i in all_s:# запись положения объекта в список grid
        i.mesto()
    
    for i in all_s:
        i.render()
   
    window.blit(screen,(0,0))# на окне прорисовываем поле игры
   
    pygame.display.flip()# отображаем полностью дисплей(окно)