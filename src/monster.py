import pygame
import random
import math

class Monster:
    def __init__(self, x, y, monster_type='shadow'):
        self.x = x
        self.y = y
        self.type = monster_type

        # Определяем характеристики монстра в зависимости от типа
        if self.type == 'shadow':
            self.hp = 1
            self.speed = 0.1
            self.image = pygame.Surface((32, 32))
            self.image.fill((0, 0, 0))  # Тень — черный
        elif self.type == 'cultist':
            self.hp = 3
            self.speed = 0.05
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 255, 255))  # Белый для культистов
        elif self.type == 'boss':
            self.hp = 5
            self.speed = 0.02
            self.image = pygame.Surface((64, 64))  # Босс — большой
            self.image.fill((255, 0, 0))  # Красный для босса

    def move_towards_player(self, player_x, player_y):
        dx = player_x - self.x
        dy = player_y - self.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            dx, dy = dx / dist, dy / dist
            self.x += dx * self.speed
            self.y += dy * self.speed

    def update(self, player_x, player_y):
        self.move_towards_player(player_x, player_y)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def kill(self):
        """Монстр убит"""
        monster_sound.play()  # Звук уничтожения монстра
        monsters.remove(self)  # Удаляем монстра из списка

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
