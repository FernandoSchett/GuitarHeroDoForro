from tupy import *

class PersonagemAssets(Image):
    def __init__(self, file) -> None:
        self._x = 770
        self._y = 310
        self._file = file
    
    # Getter methods
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_file(self):
        return self._file
    
    # Setter methods
    
    def set_x(self, value):
        self._x = value
    
    def set_y(self, value):
        self._y = value
    
    def set_file(self, value):
        self._file = value
