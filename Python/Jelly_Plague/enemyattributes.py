import pygame.sprite
import os
import random
####
working_dictionary = os.getcwd()
####


class EnemyAttributes(pygame.sprite.Sprite):
    def __init__(self, x, y, hitpoints, moving_range, collisiongroup, enemy_png):
        super().__init__()
        self.image = pygame.image.load((os.path.join(working_dictionary,
                                        'Graphics', enemy_png))).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.movementspeed = 5
        self.__range_right = self.rect.right + moving_range
        self.__range_left = self.rect.left - moving_range
        self.hitpoints = hitpoints
        self.__anygroup = collisiongroup
        self.point_per_kill = 0
        self.__active = False

    def enemy_movement(self):
        self.rect.x += self.movementspeed
        if self.rect.right >= self.__range_right:
            self.movementspeed = -self.movementspeed
        elif self.rect.left <= self.__range_left:
            self.movementspeed = -self.movementspeed

    def collision(self):
        self.__active = False
        if pygame.sprite.spritecollide(self, self.__anygroup, True, collided=None):
            self.hitpoints -= 1
            if self.hitpoints == 0:
                self.kill()
                self.__active = True
                if self.__active:
                    self.point_per_kill += 50
                    self.hitpoints -= 1
                    self.__active = False

    def update(self):
        self.enemy_movement()
        self.collision()


class Bullets(pygame.sprite.Sprite):
    def __init__(self, position, height):
        super().__init__()
        self.image = pygame.image.load((os.path.join(working_dictionary, 'Graphics', 'Bullets.png'))).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.height = height

    def border_control(self):
        if self.rect.top >= self.height:
            self.kill()

    def update(self):
        self.rect.y += 5
        self.border_control()


class EnemyComplete(EnemyAttributes):
    list = []

    def __init__(self, x, y, hitpoints, moving_range, bullet_delay, height_frame,
                 bullet_group, colissiongroup, enemy_png):
        super().__init__(x, y, hitpoints, moving_range, colissiongroup, enemy_png)
        self.__bullet_group = bullet_group
        self.bullet_delay = bullet_delay
        self.__last_shot = pygame.time.get_ticks()
        self.__height = height_frame
        EnemyComplete.list.append(self)

    def shooting(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_shot >= self.bullet_delay:
            shooting_variance = random.randint(1, 10)
            if (shooting_variance % 2) == 0:
                bullet = Bullets(self.rect.midbottom, self.__height)
                self.__bullet_group.add(bullet)
            self.__last_shot = current_time

    def update(self):
        super().update()
        self.shooting()
