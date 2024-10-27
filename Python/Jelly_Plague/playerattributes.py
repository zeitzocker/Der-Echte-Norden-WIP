import pygame.sprite
import os

#####
working_dictionary = os.getcwd()
#####


class PlayerAttributes(pygame.sprite.Sprite):
    def __init__(self, x, y, movement_speed, origin, width_frame, height_frame):
        super().__init__()
        self.__origin = origin
        self.__width_frame = width_frame
        self.__height_frame = height_frame
        self.image = pygame.image.load((os.path.join(working_dictionary, 'Graphics', 'turtle.png'))).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.movement_speed = movement_speed

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.movement_speed
        if keys[pygame.K_d]:
            self.rect.x += self.movement_speed

    def border_control(self):
        if self.rect.left <= self.__origin:
            self.rect.left = self.__origin
        elif self.rect.right >= self.__width_frame:
            self.rect.right = self.__width_frame

    def update(self):
        self.player_input()
        self.border_control()


class Shots(pygame.sprite.Sprite):
    def __init__(self, position, height):
        super().__init__()
        self.image = pygame.image.load((os.path.join(working_dictionary, 'Graphics', 'shell_bullets.png'))).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.height = height

    def border_control(self):
        if self.rect.top >= self.height:
            self.kill()

    def update(self):
        self.rect.y -= 5
        self.border_control()


class PlayerComplete(PlayerAttributes):
    def __init__(self, x, y, movement_speed, origin, width_frame, height_frame, bullet_group):
        super().__init__(x, y, movement_speed, origin, width_frame, height_frame)
        self.__bullet_group = bullet_group
        self.__height_frame = height_frame
        self.bullet_delay = 400
        self.__last_shot = pygame.time.get_ticks()

    def shooting(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE]:
            if current_time - self.__last_shot >= self.bullet_delay:
                shot = Shots(self.rect.midtop, self.__height_frame)
                self.__bullet_group.add(shot)
                self.__last_shot = current_time

    def update(self):
        super().update()
        self.shooting()
