import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship # importamos nave

class Game:
    def __init__(self):#OBJETO JUEGO ENTRA COMO PARAMETRO
        pygame.init() # INICIALIZA Y PREPARA ENTORNO
        pygame.display.set_caption(TITLE) # TITULO DE LA PANTALLA
        pygame.display.set_icon(ICON) # ICONO DE LA PANTALLA
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # ALTO Y ANCHO DE LA PANTALLA
        self.clock = pygame.time.Clock() # CONTROLA LOS TIEMPOS EN EL JUEGO
        self.playing = False # ESTADO DEL JUEGO CUANDO SE INICIA EL JUEGO
        self.game_speed = 10 # vELOCIDAD DE JUEGO
        self.x_pos_bg = 0 # POSICION DE X
        self.y_pos_bg = 0 # POSICION DE Y
        self.player = Spaceship() # creamos jugador como nave

    def run(self): # Me ejecuta en main, inicializa el juego
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events() # define los eventos del juego 
            self.update() # actualiza los eventos y elementos del juego
            self.draw() # dibuja dentro la pantalla 
        pygame.display.quit() # Cierro la ventana
        pygame.quit()# apago pygame libreria

    def events(self):
        for event in pygame.event.get(): # lista de eventos, reviso cada evento
            if event.type == pygame.QUIT: # si el evento actual es de salida
                self.playing = False # cambio a playing para que en run salga del juego

    def update(self):
        user_input = pygame.key.get_pressed() # Creamos la entrada de teclado la cual vamos a exportar a spaceship para hacer la logica de movimiento
        self.player.update(user_input) # pasamos el input y lo actualizamos en jugador para mover la nave
    
    def draw(self):
        self.clock.tick(FPS) # Actulizo 30 frame por cada segundo del juego 
        self.screen.fill((255, 255, 255)) # inicializo la pantalla en blanco
        self.draw_background() # metodo personalizado abajo que permite que pueda dibujar en al pantalla
        self.player.draw(self.screen) # depues de dibujar el fondo dibujamos la nave le pasamos como parametro la pantalla para que se dibuje
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT)) # le pasamos el fondo con las medidas
        image_height = image.get_height() # tomamos el alto de la imagen de como punto de referencia de donde comienza
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # Dibujamos la imagen en la posicion de x é y 0 0
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height)) #Dibujamos la segunda imagen  menos el alto de la primera para que aparezca en negativo
        if self.y_pos_bg >= SCREEN_HEIGHT: # SI la posicion del fondo de imagen es superior o = que el largo de la pantalla
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height)) # entro y  dibujo la nueva imagen a medida que la nueva imagen valla corriendo es decir encima de la que sigue
            self.y_pos_bg = 0 # pongo en cero el eje y para que cada vez que se super y se peque la siguiente imagen por encima
        self.y_pos_bg += self.game_speed
