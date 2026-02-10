import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rotation = 0
        self.health = 100  # Здоровье игрока
        self.shotgun_ammo = 6  # Патроны дробовика
        self.pistol_ammo = 12  # Патроны пистолета
        self.reloading = False
        self.current_weapon = 'shotgun'  # Изначально дробовик

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

    def shoot(self):
        if self.current_weapon == 'shotgun':
            if self.shotgun_ammo > 0 and not self.reloading:
                self.shotgun_ammo -= 1
                shotgun_sound.play()  # Звук выстрела
                # Логика стрельбы (попадание по монстру)
                return True
        elif self.current_weapon == 'pistol':
            if self.pistol_ammo > 0 and not self.reloading:
                self.pistol_ammo -= 1
                pistol_sound.play()  # Звук выстрела пистолета
                # Логика стрельбы (попадание по монстру)
                return True
        return False

    def reload(self):
        if not self.reloading:
            self.reloading = True
            pygame.time.set_timer(pygame.USEREVENT, 3000)  # Перезарядка длится 3 секунды

    def update(self):
        if self.reloading:
            if self.current_weapon == 'shotgun':
                self.shotgun_ammo = 6
            elif self.current_weapon == 'pistol':
                self.pistol_ammo = 12
            self.reloading = False
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Останавливаем таймер

    def check_collisions(self, monsters):
        """Проверка столкновений с монстрами"""
        for monster in monsters:
            if math.hypot(monster.x - self.x, monster.y - self.y) < 32:  # Радиус столкновения
                self.health -= 1  # Уменьшаем здоровье игрока
                if self.health <= 0:
                    print("Game Over!")  # Конец игры
                    pygame.quit()
