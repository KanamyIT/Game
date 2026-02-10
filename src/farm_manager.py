import pygame
import math

class FarmManager:
    def __init__(self):
        self.time_of_day = 0  # 0 = день, 1 = ночь
        self.night_duration = 10 * 60  # ночь длится 10 минут реального времени
        self.day_duration = 18 * 60  # день длится 18 минут
        self.timer = 0  # Таймер для смены дня и ночи

    def update(self, delta_time):
        self.timer += delta_time
        if self.time_of_day == 0:  # день
            if self.timer >= self.day_duration:
                self.time_of_day = 1  # Меняем на ночь
                self.timer = 0
        else:  # ночь
            if self.timer >= self.night_duration:
                self.time_of_day = 0  # Меняем на день
                self.timer = 0

    def get_overlay_color(self):
        """Возвращаем цвет оверлея в зависимости от времени суток"""
        if self.time_of_day == 0:
            # День: голубое небо (без оверлея)
            return (0, 0, 255, 100)  # Light blue
        else:
            # Ночь: тёмный оверлей с красным оттенком
            return (0, 0, 0, 200)  # Dark with red

    def draw_ui(self, screen):
        """Отображаем время суток и прогресс ночей"""
        font = pygame.font.SysFont('Arial', 24)
        time_text = "Night Progress: {}/{}".format(self.timer // 60, self.night_duration // 60)
        text_surface = font.render(time_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))  # Отображение текста на экране
