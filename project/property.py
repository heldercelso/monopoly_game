import random
from project.player import Player


class Property:
    owner: Player = None
    sale_price: float = None
    rent_price: float = None

    def __init__(self, property_sale_range=[70.0, 150.0], property_rent_range=[30.0, 70.0], starter=False):
        if not starter:
            self.sale_price = random.uniform(property_sale_range[0], property_sale_range[1])
            self.rent_price = random.uniform(property_rent_range[0], property_rent_range[1])
