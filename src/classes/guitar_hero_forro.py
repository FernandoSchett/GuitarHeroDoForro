import random
import os
import pygame

from tupy import *
from .menu import Menu
from ..global_var import *

class GuitarHeroForro:
    
    def __init__(self):
        pygame.init()
        self.menu = Menu()

    
    def start(self):
        run(globals())

    def play(self, music):
        self.mixer.music.load(f"{os.path.join(path_file, 'assets/sounds', music)}")
        self.mixer.music.play()