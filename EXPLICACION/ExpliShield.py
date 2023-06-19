from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE

# hacemos la clase shiel escudo para que podamos dar versiones diferentes de power up
class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)# la clase padre me esta pidiendo la imgen y el tipo por lo cual le tengo que dar esos parametros de constantes 