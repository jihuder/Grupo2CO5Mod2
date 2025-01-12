import time, random
from game.components.enemies.enemy import Enemy,SCREEN_HEIGHT,SCREEN_WIDTH

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3 and time.time() - self.last_enemy_time >= 2:
            enemy_type = random.randint(1, 2)
            enemy = Enemy(enemy_type)
            enemy.x = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)  
            enemy.y = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)  
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()

    def reset(self):
        self.enemies = []