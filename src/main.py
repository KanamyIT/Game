import pygame
import math
import random
import time
from pygame.locals import *
from src.raycaster import Raycaster
from src.player import Player
from src.monster import Monster
from src.farm_manager import FarmManager
from src.painting import Painting

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

# Основной игровой цикл
def main():
    run_game = True
    while run_game:
        screen.fill((0, 0, 0))  # Очистка экрана
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Управление движением игрока
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.rotate(pygame.mouse.get_pos())

        # Обновление времени (день/ночь)
        farm_manager.update(clock.get_time() / 1000)

        # Получение оверлея для дня/ночи
        overlay_color = farm_manager.get_overlay_color()
        overlay_surface = pygame.Surface((WIDTH, HEIGHT))
        overlay_surface.fill(overlay_color)
        screen.blit(overlay_surface, (0, 0))

        # Обновление картин
        for painting in paintings:
            painting.update(farm_manager.time_of_day)
            painting.draw(screen)

        # Отображение raycasting
        raycaster.cast()

        # Выводим часы и прогресс ночей
        farm_manager.draw_ui(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
