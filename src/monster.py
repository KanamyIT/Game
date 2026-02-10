class Monster:
    def __init__(self, x, y, monster_type='shadow'):
        self.x = x
        self.y = y
        self.hp = 1 if monster_type == 'shadow' else 2
        self.speed = 0.05
        self.monster_type = monster_type
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))  # Красный цвет для всех монстров по умолчанию

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
