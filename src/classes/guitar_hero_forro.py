import random
import os
import pygame

from tupy import *
from .screen import Screen
from ..global_var import *

class GuitarHeroForro:
    
    def __init__(self):
        pygame.init()
        self._end = False
        self._easy = False
        self._medium = False
        self._hard = False
        self.__screen = Screen()

    def start(self):
        run(globals())

    def play(self, music):
        self.mixer.music.load(f"{os.path.join(path_file, 'assets/sounds', music)}")
        self.mixer.music.play()
    
    # Getter methods
    
    def get_end(self):
        return self._end
    
    def get_easy(self):
        return self._easy
    
    def get_medium(self):
        return self._medium
    
    def get_hard(self):
        return self._hard
    
    def get_screen(self):
        return self.__screen
    
    # Setter methods
    
    def set_end(self, value):
        self._end = value
    
    def set_easy(self, value):
        self._easy = value
    
    def set_medium(self, value):
        self._medium = value
    
    def set_hard(self, value):
        self._hard = value
    
    def set_screen(self, screen):
        self.__screen = screen
