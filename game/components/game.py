import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE
from game.components.spaceship import Spaceship

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False # se le agrega el segundo estado al juego
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.death_count = 0 # se le agrega al juego el contador de muertes
        self.score = 0  # se le agrega el contador de puntaje

        # la primer que se ejecute se crea el menu
        self.menu = Menu ('Press Any Key to start...', self.screen)

    # este es el primier metodo que se va ejecutar en vez de run y lo cambiamos en main    
    def execute (self):
        # cuando se ejecute significa que su estado corriendo esta activo
        self.running = True
        while self.running: # mientras que este corriendo
            if not self.playing: # pero si no estoy jugando
                self.show_menu() # muestreme menu
                #implementar
        pygame.display.quit() # si no estoy corriendo salgo de la pantalla
        pygame.quit()   # salgo del juego

    def run(self): #run cambia a estado de que se esta jugando por lo cual tengo que actulizar los estados
        self.score = 0   
        self.bullet_manager.reset()  #reseteamos los manager ya que limpiamos las diferentes listas que tienen
        self.enemy_manager.reset() #implementar
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
# En caso de que se deje de jugar no se sale del juego ya que esa logica la transpasamo a execute 

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.menu.draw_score(self) # necesitamos dijujar ahora el score
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed


    def show_menu(self):# se ejecuta cuando el juego estaen estado corriendo pero no jugando
        # mostramos el menu en el centro de la pantalla
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT //2

        self.menu.reset_screen_color(self.screen) # ponemos la pantalla en blanco


        # necesitamos diferenciar si es la primera vez que juego o si ya estuve en el juego es decir si ya mori una vez
        # ya que  mostramos diferentes menus 
        if self.death_count > 0: # si no he muerto  es decir que es  la primer vez que inice el juego
            self.menu.update_message("keep playing")
            self.menu.draw_score(self, (0, 0, 0))
            self.menu.draw_deaths(self)
        icon = pygame.transform.scale (ICON, (80,120)) # traigo un ICON y lo pongo a escala segun  mis medidas
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height -120)) # dibujo el icono y le doy ubicacion 

        self.menu.draw(self.screen)
        self.menu.update(self)

    def update_score(self): # aumentamos el puntaje 
        self.score += 1

