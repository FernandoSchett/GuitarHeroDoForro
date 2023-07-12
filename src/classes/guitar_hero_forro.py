import random
import os
import pygame

from tupy import *
from score import Score
from notes import Notes
from menu import Menu
from hitbox import HitBox
from personagemassets import PersonagemAssets

from tupy import *

class GuitarHeroForro(pygame):
    
    def __init__(self):
        self.init()
        self.menu = Menu()
    
    def start(self):
        run(globals())

    def play(self, music):
        self.mixer.music.load(f"{os.path.join(os.path.dirname(__file__), './assets/sounds', music)}")
        self.mixer.music.play()