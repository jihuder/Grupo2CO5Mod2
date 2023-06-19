import random
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
class PowerUp(Sprite):# Heredo de sprite para darle entidad de forma de ubicacion y tamñano a mis objetos
    def __init__(self, image, type): # cuando instancie le paso como parametro la imagen para verlo visualmetne y darle un tipo para poder diferenciar entre ellos
        self.image = image # imagen importado de el manejardor de power up
        self.type = type # typo de poder que le vamos a dar
        self.rect = self.image.get_rect() # le doy entidad de rectagulo
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120) # para que sea simetrico???
        self.rect.y = 0# el poder va se estatico en su eje y
        self.start_time = 0 # para saber cuanto va durar necesitamos controlar su tiempo de duracion con un tiempo de inicio

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed # vamos hacer que recorra en un y porque en x no se va a mover, de donde viene el game speed viene de game 
        if self.rect.y > SCREEN_HEIGHT:# si el poder supera el alto de la pantalla
            power_ups.remove(self) # removemos el poder

    def draw(self, screen):# dibujamos en pantalla y le pasamos la pantalla para dibujar
        screen.blit(self.image, self.rect)# que dibujamos? el poder y le damos la imagen y la posicion
    