import random # se exporta ramdon para mover aletoriamente en x y y
import pygame # se importa la libreria para importar sprite
from pygame.sprite import Sprite #se importar sprete para darle una entidad fisica al enemigo dentro del juego
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH # importo las imagenes del enemigo y las constantes de ancho y largo

class Enemy(Sprite):# heredo de sprite para darle entidad al enemigo
    SHIP_WIDTH = 40 # anchura del enemigo
    SHIP_HEIGHT = 60 # altura del enemigo
    Y_POS = 20 # comienza a existir en el y a 20 grados de y
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550] # diferentes posiciones para que aparezca el enemigo
    SPEED_Y = 1  # velocidad como constante en el eje y
    SPEED_X = 5 # Avanza como constante en velocidad de 5 valores con respecto a x 
    MOV_X = {0: 'left', 1: 'right'} #creamos un movimiento aleatorio de izquierda a

    def __init__(self):
        self.image = ENEMY_1 # le damos la imagen al enemigo
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT)) # lo adaptamos segun las dimensiones de nuestra pantalla
        self.rect = self.image.get_rect()# le damos la estructura de un rectacgulo para manipularlo tanto en pocion como en tamaño
        self.rect.y = self.Y_POS # le doy su posicion en y
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)] # le digo que escoga una posicon aleatoria para que comience a existir
        self.speed_x = self.SPEED_X # le doy su velocidad en x
        self.speed_y = self.SPEED_Y # le doy su velocidad en y
        self.movement_x = self.MOV_X[random.randint(0,1)] # le doy un movimiento aleatorio cuando comience a existir
        self.move_x_for = random.randint(30, 100) # Es el rango de la cantidad de posiciones que se va mover con la constante en x para escoger nuevamente si es derecha o izquierda cada cuanto termine esa cantidadn de posiciones
        self.index = 0 # contador de ciclos para contar en numero de pasos  delejej x

    def update(self, ships): # actualizo la nave en cuanto su posicion y atributos por cada iteracion de ciclo del juego
        self.rect.y += self.speed_y # le sumo la velocidad al eje de y para que pueda ir bajando constantemente

        if self.movement_x == 'left': # pregunto si el movimeinto en rando esgogio izquierda
            self.rect.x -= self.speed_x # entonces le doy velocidad para que disminuya en su eje x y se valla a la izquierda
        else: # si no escogio derecha
            self.rect.x += self.speed_x # entonces le doy la velocidad  para que aumente a la derecha
        
        self.change_movement_x() # invoco el metodo de  cambio de movimiento en cuanto a su cantidad de pasos

        if self.rect.y >= SCREEN_HEIGHT: # agrego la validacion para deicirle se sobrepaso la pantallla en su eje y
            ships.remove(self) # remuevo la nave en caso de que haya sobrepasado

    def draw(self, screen): # dibujo la nave por cada iteracion del ciclo del juego dentro de la pantalla
        screen.blit(self.image, (self.rect.x, self.rect.y)) # dibujo la nave segun su posicion actual de x e y

    def change_movement_x(self): # saber cuantos pasos va moverse  por cada lado
        self.index += 1 # ponemos el contador en uno como primera iteracion 
        if (self.index >= self.move_x_for and self.movement_x == 'right')or(self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            # si el contador es mayor o y gual a la cantidad de pasos a recorrer en x y su movimiento es a la derecha
            # ó si la nave en su eje x supero el ancho de la pantalla reinicio el movimiento 
            self.movement_x = 'left' # quiere decir que ya supero el numero de pasos asignado de manera aleatoria por lo cual le decimos que escoga el lado izquierdo
            self.index = 0 # ponemos el contador en 0 para inicia de nuevo el conteo de pasos aleatoria mente
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <=10):
             # si el contador es mayor o y gual a la cantidad de pasos a recorrer en x y su movimiento es a la izquierda
            # ó si la nave en su eje x supero el ancho de la pantalla  en lado izquierdo ya que 10 es lo minimo puede ir hacia la izquierda
            
            self.movement_x = 'right'# quiere decir que ya supero el numero de pasos asignado de manera aleatoria por lo cual le decimos que escoga el lado derecho
            self.index = 0 # ponemos el contador en 0 para inicia de nuevo el conteo de pasos aleatoria mente