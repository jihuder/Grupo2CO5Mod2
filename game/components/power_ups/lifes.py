from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  HEARTS, HEART_TYPE


class Lifes(PowerUp):
    def __init__(self):
        super().__init__(HEARTS, HEART_TYPE)