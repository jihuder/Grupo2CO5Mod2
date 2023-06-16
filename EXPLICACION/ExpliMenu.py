"""
    Menu me permite desplegar en pantalla diferentes tipos de mensajes durante el juego
"""
import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 # Cual es la mitad de la pantalla en el alto 
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2 # Cual es la mitas de la pantalla en el ancho

    def __init__(self, message, screen):# crear el menu inicial
        screen.fill((255, 255, 255)) # restablecemos el fondo de pantalla en blanco
        self.font = pygame.font.Font(FONT_STYLE, 50)# Utilizamos la fuente que vamos a usar y el tamaño
        self.text = self.font.render(message, True, (0,0,0)) # renderizamos el texto y la damos color
        self.text_rect = self.text.get_rect() # utilizamos rect para darle propiedades de tamñano y ubicacion
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT) # centramos el texto segun la pantalla

    def update(self, game):# actualiza en el ciclo del juego
        pygame.display.update() #actualiza la pantalla o la resetea
        self.handle_events_on_menu(game) # y llamamos al manejador de eventos y le pasmos la clase game

    def draw (self, screen ):# dibuja en el ciclo del juego
        screen.blit(self.text, self.text_rect) # dibujamos en pantalla el texto  con las cordenadas del centro

    def handle_events_on_menu(self, game): # manejador de eventos en el menu, con dos estados diferentes
        # Estados dentro y fuera de juego en el game manejamos los atributos de si estamos jugando o no
        for event in pygame.event.get(): # escuchamos los eventos y decimos que
            if event.type == pygame.QUIT: # si el evento de t¿ipo tecla es quit o es salir
                game.playing = False # terminamos el juego
                game.running = False # paramas todo el juego
            elif event.type == pygame.KEYDOWN: # si el evento es de tipo tecla es cualquier tecla
                game.run() # correr el juego

    def reset_screen_color(self, screen):# restablecer el color
        screen.fill((255, 255, 255)) #restablecemos el color de blanco de nuevo cuando comenzo el menu

    def update_message(self, message):# Desplegar mensajes
        self.text = self.font.render(message, True, (0,0,0)) # actualizamos el texto  y lo rederizamos de nuevo
        self.text_rect = self.text.get_rect() # del objeto actualizamos  su rect 
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT) # actualizamos su ubicacion por medio de rect