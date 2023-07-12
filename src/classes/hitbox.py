from tupy import *

class HitBox(Image):
    def __init__(self, x: float, y: float, file: str, angle: int) -> None:
        self._x = x
        self._y = y
        self._file = file
        self._angle = angle
        self._hide()
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_file(self):
        return self._file
    
    def get_angle(self):
        return self._angle
        
    def set_x(self, value):
        self._x = value
    
    def set_y(self, value):
        self._y = value
    
    def set_file(self, value):
        self._file = value
    
    def set_angle(self, value):
        self._angle = value
