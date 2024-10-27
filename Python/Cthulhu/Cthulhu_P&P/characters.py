import pygame
from pygame import *

class Characters:
    def __init__(self,name , x, y, image,icon):
        self.icon = pygame.image.load(icon).convert_alpha()
        self.icon_rect = self.icon.get_rect(center=(x, y))

        self.name = name
        self.tab_x = x
        self.tab_y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image_rect = Rect(5,100,50,50)
        self.showing = False

    def ShowIcon(self,screen):
        screen.blit(self.icon, self.icon_rect)

    def CheckMouse(self,pos):
        if self.icon_rect.collidepoint(pos):
            self.showing = True
        else:
            self.showing = False

    def TableDrawn(self, screen):
        if self.showing == True:
            screen.blit(self.image, self.image_rect)
