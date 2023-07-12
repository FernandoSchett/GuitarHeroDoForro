from tupy import *

class Notes(Image):
    """
    Classe responsável por armazenar os dados de uma nota.

    Atributos privados:
    - _file: imagem da nota
    - _x: posição horizontal da nota
    - _y: posição vertical da nota
    - _angle: ângulo da nota
    - _speed: velocidade da nota

    Métodos públicos:
    - fall(): atualiza a posição da nota e verifica se ela foi acertada pelo jogador
    """
    def __init__(self, x: float, y: float, file: str, angle: int, speed: float) -> None:
        self._file = file
        self._x = x
        self._y = y
        self._angle = angle
        self._speed = speed

    # Getter methods
    
    def get_file(self):
        return self._file
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_angle(self):
        return self._angle
    
    def get_speed(self):
        return self._speed
    
    # Setter methods
    
    def set_file(self, value):
        self._file = value
    
    def set_x(self, value):
        self._x = value
    
    def set_y(self, value):
        self._y = value
    
    def set_angle(self, value):
        self._angle = value
    
    def set_speed(self, value):
        self._speed = value

    def update(self):
        if self._y > 450:
            return False
        self._y += self._speed
