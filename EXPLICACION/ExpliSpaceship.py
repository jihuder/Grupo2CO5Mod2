import pygame
from pygame.sprite import Sprite # Sprite lo utilizamos para hacer nuestros propios elementos del juego
from game.utils.constants import SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    SHIP_WIDTH = 40 # ancho de la nave
    SHIP_HEIGHT = 60 # alto de la nave
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH # Posicion inicial de la nave en x segun la pantalla
    Y_POS = 500 # posicion inicial de la nave en y
    SHIP_SPEED = 10 # velocidad de la nave

    def __init__(self):
        self.image = SPACESHIP # para visualizar la nave la traemos definida en constantes
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT)) #Adaptamos la imagen en la pantalla
        self.rect = self.image.get_rect() # utilizo este metodo para poder manipular la nave segun sus codernadas
        self.rect.x = self.X_POS # cordena en x
        self.rect.y = self.Y_POS # cordena en y

    def update(self, user_input): # le pasamos como parametro la entrada de teclado creada en game update
        if user_input[pygame.K_LEFT]: # si el jugador oprime a la izquierda
            self.move_left() # llamar al metodo mover izquierda
        elif user_input[pygame.K_RIGHT]: # si el jugador oprime derecha
            self.move_right() # llamar al metodo mover derecha
        elif user_input[pygame.K_UP]: # si el jugador oprime izquierda
            self.move_up() # llamamos al metodo mover arriba
        elif user_input[pygame.K_DOWN]: # si el jugador oprime abajo
            self.move_down() # llamamos al metodo mover abajo

    def move_left(self):
        self.rect.x -=  self.SHIP_SPEED # le restamos a la izquierda en x segun la constatne de velocidad

    def move_right(self):
        self.rect.x +=  self.SHIP_SPEED  # le sumamos a la derecha en x segun la constante

    def move_up(self):
        self.rect.y -=  self.SHIP_SPEED  # le restamos en y para que suba 

    def move_down(self):
        self.rect.y +=  self.SHIP_SPEED   # le sumamos en y para que baje

    def draw(self, screen): # le pasamos el lienzo
        screen.blit(self.image, (self.rect.x, self.rect.y)) # actualizamos la el lienzo segun la nueva posicon de la nave