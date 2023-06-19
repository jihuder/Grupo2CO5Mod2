import random

import pygame
from game.components.power_ups.shield import Shield

from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager: # Manejamos los poderes y los instanciamos
    def __init__(self):
        self.power_ups = [] # creamos una lista  de los poderes que se van a utilizar
        self.duration = random.randint(3, 5) # le damos una duracion  de cuanto van a durar alerotoriamente
        self.when_appears = random.randint(5000, 10000) # cuando aparrece por lo cual le damos un espacio entre 5000 y 10000 milesegundo que aparezca aleatoriamente

    def update(self, game):
        current_time = pygame.time.get_ticks() # tomamos el tiempo actual
        # cuando hacemos que aparesca un poder
        if len(self.power_ups) == 0 and current_time >= self.when_appears: # SI mi lista esta vacia es decir no hay poderes y cuando mi
            # tempo actual sea superior del ultimo momento que aparecio
            self.generate_power_up(game) # creao el poder y le paso el juego

        for power_up in self.power_ups: # Listo los poderes
            power_up.update(game.game_speed, self.power_ups) # si el poder que tome le doy sus acciones en pantalla para que la recorra

            # gestionamos el choque con el poder para adquirirlo
            if game.player.rect.colliderect(power_up.rect): # si colicionamos con el poder
                power_up.start_time = pygame.time.get_ticks() # Le damos un tiempo de duracion de cuando comenzo
            
                game.player.power_up_type = power_up.type # definimos que tipo de poder tiene en la clase  game
                game.player.has_power_up = True # si tiene el poder
                game.player.power_time_up = power_up.start_time + (self.duration * 1000) # cuando el inicio de que se estrello supere la duracion de 100 milesegundo se tiene que apagar
                game.player.set_image((65, 75), SPACESHIP_SHIELD) # cambiar de imagen para cuando tenga el poder
                self.power_ups.remove(power_up) # removemos el poder de la lista de power up

    def draw(self, screen): # dibujamos en pantalla
        for power_up in self.power_ups:# tomamos el elementos de la lista
            power_up.draw(screen) # dibujamos en la pantalla el poder

    def generate_power_up(self, game): # creamos el poder
        power_up = Shield() #instanciamos el poder de curacion 
        self.when_appears += random.randint(5000, 10000) # # le decimos que aparezca cada tiempo
        self.power_ups.append(power_up) # agreamos el poder a la lista para que pueda ser gestionado