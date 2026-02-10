import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rotation = 0

    def move(self, keys):
        speed = PLAYER_SPEED
        if keys[pygame.K_w]:  # Вперёд
            self.x += math.cos(math.radians(self.rotation)) * speed
            self.y += math.sin(math.radians(self.rotation)) * speed
        if keys[pygame.K_s]:  # Назад
            self.x -= math.cos(math.radians(self.rotation)) * speed
            self.y -= math.sin(math.radians(self.rotation)) * speed
        if keys[pygame.K_a]:  # Влево
            self.x += math.cos(math.radians(self.rotation + 90)) * speed
            self.y += math.sin(math.radians(self.rotation + 90)) * speed
        if keys[pygame.K_d]:  # Вправо
            self.x -= math.cos(math.radians(self.rotation + 90)) * speed
            self.y -= math.sin(math.radians(self.rotation + 90)) * speed

    def rotate(self, mouse_pos):
        self.rotation = math.degrees(math.atan2(mouse_pos[1] - self.y, mouse_pos[0] - self.x))
