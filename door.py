class Door:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.hp = 100  # Здоровье двери

    def repair(self, amount):
        """Ремонт двери"""
        self.hp = min(100, self.hp + amount)

    def draw(self, screen):
        door_color = (255, 255, 255) if self.hp > 0 else (255, 0, 0)
        pygame.draw.rect(screen, door_color, (self.x, self.y, 64, 128))  # Рисуем дверь
