import random
import os
import pygame

from tupy import *
from src.classes.screen import Screen
from ..global_var import *
from src.classes.score import Score
from src.classes.personagemassets import PersonagemAssets
from src.classes.notes import Notes


class GuitarHeroForro:
    def __init__(self):
        pygame.init()
        self._status = ""
        self._inputs = []
        self._screen = Screen()
        self.personagem = PersonagemAssets('../assets/character/Personagem1.png')
        self.scorePlayer = Score()
        self._end = False

    def start(self):
        run(globals())

    def destroyNotes(self):

        for i in NotasEsquerda:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasEsquerda.remove(i)
                i.destroy()
                self.scorePlayer.decrement(5)
            if i.update():
                NotasEsquerda.remove(i)
                i.destroy()
        for i in NotasDireita:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasDireita.remove(i)
                i.destroy()
                self.scorePlayer.decrement(5)
            if i.update():
                NotasDireita.remove(i)
                i.destroy()

        if self._status != "medium" and self._status != "hard":
            return

        for i in NotasBaixo:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasBaixo.remove(i)
                i.destroy()
                self.scorePlayer.decrement(5)
            if i.update():
                NotasBaixo.remove(i)
                i.destroy()

        if not self._status == "hard":
            return

        for i in NotasCima:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasCima.remove(i)
                i.destroy()
                self.scorePlayer.decrement(5)
            if i.update():
                NotasCima.remove(i)
                i.destroy()

    def createNotes(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)

        if a < 24:
            NotasEsquerda.append(Notes(self._inputs[-2], 0, os.path.join(path_file, 'Notes.png'), 0, 4))
        if b < 24:
            NotasDireita.append(Notes(self._inputs[-1], 0, os.path.join(path_file, 'Notes.png'), 180, 4))

        if not self._status == "medium" and not self._status == "hard":
            return

        if a > 79:
            NotasBaixo.append(Notes(self._inputs[-3], 0, os.path.join(path_file, 'Notes2.png'), 90, 4))

        if not self._status == "hard":
            return

        if b > 79:
            NotasCima.append(Notes(self._inputs[-4], 0, os.path.join(path_file, 'Notes2.png'), 270, 4))

    def updateNotes(self):
        # Partitura para mais à esquerda
        if keyboard.is_key_just_down("Left") and len(NotasEsquerda) != 0:
            if h[0].y / NotasEsquerda[0].y >= 0.95 and h[0].y / NotasEsquerda[0].y <= 1.18:
                NotasEsquerda[0].y += 501
                self.scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                self.personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasEsquerda[0].y += 501
                self.scorePlayer.decrement(5)

        # Partitura para mais à direita
        if keyboard.is_key_just_down("Right") and len(NotasDireita) != 0:
            if h[1].y / NotasDireita[0].y >= 0.95 and h[1].y / NotasDireita[0].y <= 1.18:
                NotasDireita[0].y += 501
                self.scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                self.personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasDireita[0].y += 501
                self.scorePlayer.decrement(5)

        if self._status == "easy":
            return 

        # Partitura para baixo
        if keyboard.is_key_just_down("Down") and len(NotasBaixo) != 0:
            if h[1].y / NotasBaixo[0].y >= 0.95 and h[1].y / NotasBaixo[0].y <= 1.18:
                NotasBaixo[0].y += 501
                self.scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                self.personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasBaixo[0].y += 501
                self.scorePlayer.decrement(5)

        if self._status != "hard":
            return

        # Partitura para cima
        if keyboard.is_key_just_down("Up") and len(NotasCima) != 0:
            print(self._status)
            if h[1].y / NotasCima[0].y >= 0.95 and h[1].y / NotasCima[0].y <= 1.18:
                NotasCima[0].y += 501
                self.scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                self.personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasCima[0].y += 501
                self.scorePlayer.decrement(5)

    def play(self, music):
        pygame.mixer.music.load(f"{os.path.join(path_file, 'assets/sounds', music)}")
        pygame.mixer.music.play()

    # Getter methods
    def get_status(self):
        return self._status

    def get_screen(self):
        return self.__screen

    # Setter methods
    def set_status(self, value):
        self._status = value

    def set_screen(self, screen):
        self.__screen = screen
