from tupy import *

class Menu(BaseImage):
    def __init__(self) -> None:
        super().__init__(file='start.png', x=450, y=250)
        self._end = False
        self._easy = False
        self._medium = False
        self._hard = False
    
    def get_end(self):
        return self._end
    
    def get_easy(self):
        return self._easy
    
    def get_medium(self):
        return self._medium
    
    def get_hard(self):
        return self._hard
        
    def set_end(self, value):
        self._end = value
    
    def set_easy(self, value):
        self._easy = value
    
    def set_medium(self, value):
        self._medium = value
    
    def set_hard(self, value):
        self._hard = value
