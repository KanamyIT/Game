import pygame

class Painting:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.day_painting = pygame.Surface((64, 64))  # Текстура картины днем
        self.night_painting = pygame.Surface((64, 64))  # Текстура картины ночью
        
        # Заполнение картин
        self.day_painting.fill((255, 255, 255))  # Белая картина (день)
        self.night_painting.fill((255, 0, 0))  # Кровавая картина (ночь)

        self.current_painting = self.day_painting  # Изначально дневная картина

    def update(self, time_of_day):
        """Обновляем картину в зависимости от времени суток"""
        if time_of_day == 1:  # Ночь
            self.current_painting = self.night_painting
        else:  # День
            self.current_painting = self.day_painting

    def draw(self, screen):
        """Отображаем картину на экране"""
        screen.blit(self.current_painting, (self.x, self.y))
