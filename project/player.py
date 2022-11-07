from dataclasses import dataclass

IMPULSIVE, EXIGENT, CAUTIOUS, RANDOM = 0, 1, 2, 3
PLAYER_TYPE = { IMPULSIVE: 'Impulsivo',
                EXIGENT: 'Exigente',
                CAUTIOUS: 'Cauteloso',
                RANDOM: 'Aleatorio'}


# class just to store data - __init__ included by default
@dataclass
class Player:
    player_id: int
    type: int
    position: int = 0
    available_money: float = 300.0
