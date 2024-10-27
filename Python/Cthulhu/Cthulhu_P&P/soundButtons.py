from pygame import *
import pygame
class SoundButton:
    def __init__(self, name, fileName, colour, x, y, loop):
        small_font = pygame.font.Font('fonts/Designer.otf', 25)
        r,g,b = colour
        self.colour = colour
        self.darkerColour = (max(0, r - 80),max(0, g - 80),max(0, b - 80))
        self.sound = mixer.Sound(fileName)
        self.rect = Rect(x,y,100,100)
        self.playing = False
        self.loop = loop
        self.name = small_font.render(name, False, (255,255,255))
        self.name_rect = self.name.get_rect(center=(x + 50, y + 50))
        self.name_dark = small_font.render(name, False, (205,205,205))
        self.name_dark_rect = self.name.get_rect(center=(x + 50, y + 50))
    def ButtonDrawn(self, screen):
        if self.playing == False:
            draw.rect(screen,self.colour,self.rect)
            screen.blit(self.name, self.name_rect)
        else:
            draw.rect(screen,self.darkerColour,self.rect)
            screen.blit(self.name_dark, self.name_dark_rect)
    def CheckClick(self,pos):
        if self.rect.collidepoint(pos):
          if self.playing == False:
              self.sound.play(-1)
              self.playing = True
          else:
              self.sound.fadeout(1000)
              #self.sound.stop()
              self.playing = False