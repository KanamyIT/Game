import math
import pygame

class Raycaster:
    def __init__(self, player, map_data):
        self.player = player
        self.map_data = map_data
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        self.projection_plane_dist = WIDTH // 2 / math.tan(math.radians(FOV / 2))

    def cast(self):
        for x in range(WIDTH):
            # Расчёт угла и шага
            ray_angle = (self.player.rotation - FOV / 2) + (x / WIDTH) * FOV
            ray_angle = ray_angle % 360
            # Простейший алгоритм для raycasting
            dx = math.cos(math.radians(ray_angle))
            dy = math.sin(math.radians(ray_angle))
            for depth in range(MAX_DEPTH):
                player_x, player_y = self.player.x, self.player.y
                ray_x = player_x + dx * depth
                ray_y = player_y + dy * depth
                map_x, map_y = int(ray_x // TILE_SIZE), int(ray_y // TILE_SIZE)
                if self.map_data[map_y][map_x] == 1:
                    # Рисуем стену
                    color = (139, 69, 19)
                    pygame.draw.line(self.screen, color, (x, HEIGHT // 2), (x, HEIGHT // 2 + 100))
                    break
                elif self.map_data[map_y][map_x] == 2:
                    # Рисуем дверь
                    color = (255, 255, 255)
                    pygame.draw.line(self.screen, color, (x, HEIGHT // 2), (x, HEIGHT // 2 + 50))
                    break
