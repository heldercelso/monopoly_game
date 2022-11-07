from project.property import Property

class Board():

    def __init__(self, _num_properties, property_sale_range, property_rent_range):
        self._num_properties = _num_properties
        self._property_sale_range = property_sale_range
        self._property_rent_range = property_rent_range
        self.__new_board()

    def __new_board(self):
        initial_pos = [Property(starter=True)]  # Starter point - position 0
        properties = [Property(self._property_sale_range, self._property_rent_range) for _ in range(self._num_properties)]
        self._all_properties = initial_pos + properties
    
    def _get_board(self):
        return self._all_properties