import pygame
import math
import random
import sys
import os

# Добавляем путь к src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.raycaster import Raycaster
from src.player import Player
from src.monster import Monster
from src.farm_manager import FarmManager
from src.painting import Painting
from src.door import Door

# Константы и начальная настройка
WIDTH, HEIGHT = 800, 600
FPS = 60
MAP_SIZE = 10
TILE_SIZE = 64
FOV = 60  # угол обзора
MAX_DEPTH = 800
PLAYER_SPEED = 0.1  # скорость игрока
MONSTER_SPAWN_RATE = 0.1  # шанс появления монстра ночью
NIGHTS_TOTAL = 5  # всего ночей

# Инициализация pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Horror Game")
clock = pygame.time.Clock()

# Игрок
player = Player()

# Менеджер игры (день/ночь, задачи)
farm_manager = FarmManager()

# Картины
paintings = [Painting(100, 100), Painting(300, 100), Painting(500, 100)]

# Raycasting
raycaster = Raycaster(player, MAP)

# Список монстров
monsters = []

# Звуки
footsteps_sound = pygame.mixer.Sound('assets/sounds/footsteps.wav')  # Замените на свой звук шагов
shotgun_sound = pygame.mixer.Sound('assets/sounds/shotgun.wav')  # Замените на свой звук выстрела
pistol_sound = pygame.mixer.Sound('assets/sounds/pistol.wav')  # Звук пистолета
monster_sound = pygame.mixer.Sound('assets/sounds/monster_sound.wav')  # Замените на свой звук монстра
chicken_sound = pygame.mixer.Sound('assets/sounds/chicken_sound.wav')  # Замените на звук курицы

# Дверь
door = Door(400, 300)

def spawn_monsters():
    """Спавн монстров ночью с разными типами"""
    global monsters
    monsters = []
    num_monsters = random.randint(3, 10)  # Число монстров каждую ночь
    for _ in range(num_monsters):
        monster_type = random.choice(['shadow', 'cultist', 'boss'])  # Случайный тип монстра
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT - 100)
        monsters.append(Monster(x, y, monster_type))

def game_over():
    font = pygame.font.SysFont('Arial', 72)
    text = font.render("Game Over!", True, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(3000)  # Ожидаем 3 секунды перед выходом
    pygame.quit()
    exit()

def victory():
    font = pygame.font.SysFont('Arial', 72)
    text = font.render("You Win!", True, (0, 255, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(3000)  # Ожидаем 3 секунды перед выходом
    pygame.quit()
    exit()

# Основной игровой цикл
def main():
    run_game = True
    while run_game:
        screen.fill((0, 0, 0))  # Очистка экрана
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Перезарядка
                    player.reload()
                if event.key == pygame.K_1:  # Выбор дробовика
                    player.current_weapon = 'shotgun'
                if event.key == pygame.K_2:  # Выбор пистолета
                    player.current_weapon = 'pistol'

        # Проверка столкновений с монстрами
        player.check_collisions(monsters)

        # Проверка победы
        if len(monsters) == 0 and farm_manager.time_of_day == 1:
            victory()

        # Проверка здоровья игрока
        if player.health <= 0:
            game_over()

        # Управление движением игрока
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.rotate(pygame.mouse.get_pos())

        # Ремонт двери
        if keys[pygame.K_e]:  # При нажатии E ремонтируем дверь
            door.repair(20)

        # Обновление времени (день/ночь)
        farm_manager.update(clock.get_time() / 1000)

        # Спавним монстров на ночь
        if farm_manager.time_of_day == 1:
            spawn_monsters()

        # Обновление картин
        for painting in paintings:
            painting.update(farm_manager.time_of_day)
            painting.draw(screen)

        # Обновление монстров
        for monster in monsters:
            monster.update(player.x, player.y)
            monster.draw(screen)

        # Стрельба
        if keys[pygame.K_SPACE]:  # Если игрок нажимает пробел, стреляем
            player.shoot()

        # Рисуем дверь
        door.draw(screen)

        # Отображение raycasting
        raycaster.cast()

        # Выводим часы и прогресс ночей
        farm_manager.draw_ui(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
