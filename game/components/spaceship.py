import pygame
from pygame.sprite import Sprite
from game.utils.constants import DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP, DELAY
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.shooting_time = DELAY
        self.power_up_type = DEFAULT_TYPE # 1 DE QUE TIPO DE PODER son los tres atributos que se crearon cuando el player colicione con el poder
        self.has_power_up = False # 2 SI EL PLAYER TIENO O NO EL PODER
        self.power_time_up = 0 # 3 EL TIEMPO DE DURACION DEL PODER



    def update(self, user_input, game):
        
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()

        if current_time >= self.shooting_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += DELAY

    def move_left(self): 
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y +=  self.SHIP_SPEED   

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Se creo el metodo de cambio de imagen para saber cuando tenga el poder el usuario
    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)