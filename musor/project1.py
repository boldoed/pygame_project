import pygame as pg
import sys
import os 

class Game():
    def __init__(self):
        self.running = True
        pg.init()
        size = WIDTH, HEIGHT = 700, 700
        self.screen = pg.display.set_mode(size)

    def run(self):
        while self.running:
            self.render()
            self.events()
            self.update()
    
    def events(self):
        events = pg.event.get()
        for event in events:
           if event.type == pg.QUIT:
            self.running = False

    def render(self):
        self.draw(self.screen)
        pg.display.flip()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (255, 0, 0), (1, 1, self.width - 1, self.height - 1))

if __name__ == '__main__':
    game = Game()
    pg.display.set_caption('Пасьянс')
    game.run()
    pg.quit()

        