import pygame
import math
import random
from src.raycaster import Raycaster
from src.player import Player

# Настройка
WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 64
FOV = 60

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Horror Game")
clock = pygame.time.Clock()

player = Player()
raycaster = Raycaster(player, MAP)

# Главный цикл игры
def main():
    running = True
    while running:
        screen.fill((0, 0, 0))  # Очистка экрана
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление движением игрока
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.rotate(pygame.mouse.get_pos())

        # Отображение raycasting
        raycaster.cast()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
