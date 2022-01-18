import random
import pygame

class Card(object):
    def __init__(self, textures, suit, val):
        self.textures = textures
        self.card_tex      = textures[0]
        self.card_back_tex = textures[1]
        self.suit = suit
        self.value = val
        self.revealed = False


    def draw(self, screen, pos):
        if self.revealed:
            screen.blit(self.card_tex, pos)
        else:
            screen.blit(self.card_back_tex, pos)
