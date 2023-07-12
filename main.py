import random
import os

from tupy import *
from src.classes.score import Score
from src.classes.notes import Notes
from src.classes.personagemassets import PersonagemAssets
from src.classes.guitar_hero_forro import GuitarHeroForro
from src.global_var import *
import pygame

path_file = os.path.dirname(__file__)
game = GuitarHeroForro()

"""
    Tentativa de implementação por qwer (por hora) no update, sendo;
    q -> mais à esquerda
    r -> mais à direita
"""
if game.get_end() == False:
    
    print("tome")

    def destroyNotes():
        global NotasEsquerda
        global NotasDireita
        global NotasBaixo
        global NotasCima
        for i in NotasEsquerda:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasEsquerda.remove(i)
                i.destroy()
                scorePlayer.decrement(5)
            if i.update():
                NotasEsquerda.remove(i)
                i.destroy()
        for i in NotasDireita:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasDireita.remove(i)
                i.destroy()
                scorePlayer.decrement(5)
            if i.update():
                NotasDireita.remove(i)
                i.destroy()
        if not game.menu._medium and not game.menu._hard:
            return

        for i in NotasBaixo:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasBaixo.remove(i)
                i.destroy()
                scorePlayer.decrement(5)
            if i.update():
                NotasBaixo.remove(i)
                i.destroy()

        if not game.menu._hard:
            return

        for i in NotasCima:
            """ Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
            if i.y > 450:
                NotasCima.remove(i)
                i.destroy()
                scorePlayer.decrement(5)
            if i.update():
                NotasCima.remove(i)
                i.destroy()

    def createNotes():
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        if a < 24:
            NotasEsquerda.append(Notes(game.menu._inputs[-2], 0, os.path.join(path_file, 'assets/image.png'), 0, 4))
        if b < 24:
            NotasDireita.append(Notes(game.menu._inputs[-1], 0, os.path.join(path_file, 'assets/image.png'), 180, 4))

        if not game.menu._medium and not game.menu._hard:
            return

        if a > 79:
            NotasBaixo.append(Notes(game.menu._inputs[-3], 0, os.path.join(path_file, 'assets/image.png'), 90, 4))

        if not game.menu._hard:
            return

        if b > 79:
            NotasCima.append(Notes(game.menu._inputs[-4], 0, os.path.join(path_file, 'assets/image.png'), 270, 4))

    def updateNotes():
        global NotasEsquerda
        global NotasDireita
        global NotasBaixo
        global NotasCima

        # Partitura para mais à esquerda
        if keyboard.is_key_just_down("Left") and len(NotasEsquerda) != 0:
            if h[0].y / NotasEsquerda[0].y >= 0.95 and h[0].y / NotasEsquerda[0].y <= 1.18:
                NotasEsquerda[0].y += 501
                scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasEsquerda[0].y += 501
                scorePlayer.decrement(5)

        # Partitura para mais à direita
        if keyboard.is_key_just_down("Right") and len(NotasDireita) != 0:
            if h[1].y / NotasDireita[0].y >= 0.95 and h[1].y / NotasDireita[0].y <= 1.18:
                NotasDireita[0].y += 501
                scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasDireita[0].y += 501
                scorePlayer.decrement(5)

        if not game.menu._medium and not game.menu._hard:
            return

        # Partitura para baixo
        if keyboard.is_key_just_down("Down") and len(NotasBaixo) != 0:
            if h[1].y / NotasBaixo[0].y >= 0.95 and h[1].y / NotasBaixo[0].y <= 1.18:
                NotasBaixo[0].y += 501
                scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasBaixo[0].y += 501
                scorePlayer.decrement(5)

        if not game.menu._hard:
            return

        # Partitura para cima
        if keyboard.is_key_just_down("Up") and len(NotasCima) != 0:
            if h[1].y / NotasCima[0].y >= 0.95 and h[1].y / NotasCima[0].y <= 1.18:
                NotasCima[0].y += 501
                scorePlayer.increment(10)
                randomNumero = random.randint(1, 38)
                personagem.file = f'../assets/character/Personagem{randomNumero}.png'
            else:
                NotasCima[0].y += 501
                scorePlayer.decrement(5)

    def update():
        global h
        global counter

        if keyboard.is_key_just_down('space'):
            game.__screen._file= 'music.png'

        """ if para o game.menu de seleção de músicas """

        if keyboard.is_key_just_down('A'):
            game.__screen._file = 'dificult.png'
            game.play('tarecoemariola.ogg')
        if keyboard.is_key_just_down('B'):
            game.__screen._file = 'dificult.png'
            game.play('deixaeutesuperar.ogg')
        if keyboard.is_key_just_down('C'):
            game.__screen._file = 'dificult.png'
            game.play('ocheirodecarolina.ogg')
        if keyboard.is_key_just_down('D'):
            game.__screen._file = 'dificult.png'
            game.play('oxotedasmeninas.ogg')
        if keyboard.is_key_just_down('E'):
            game.__screen._file = 'dificult.png'
            game.play('luaminha.ogg')

        """ if para o menu de dificuldades """

        if game.menu._file == "dificult.png":
            if keyboard.is_key_just_down('1'):
                print("dacil carai")
                game.menu._easy = True
                game.menu._inputs = easy_inputs
                game.menu._file = '../assets/bg.png'
                game.menu._end = True
            elif keyboard.is_key_just_down('2'):
                game.menu._medium = True
                game.menu._inputs = medium_inputs
                game.menu._file = '../assets/bg.png'
                game.menu._end = True
            elif keyboard.is_key_just_down('3'):
                game.menu._hard = True
                game.menu._inputs = hard_inputs
                game.menu._file = '../assets/bg.png'
                game.menu._end = True

        if not game.menu._end:
            return
        if counter == 10:
            createNotes()
            counter = 0
        counter += 1
        
        # modo facil
        if game.menu._easy:
            """ o _show() é para mostrar as 2 hitboxs do modo fácil """
            h[0]._show()
            h[1]._show()
            global NotasEsquerda
            global NotasDireita
            destroyNotes()
            updateNotes()

        # modo medio
        if game.menu._medium:
            """ o _show() é para mostrar as 3 hitboxs do modo fácil """
            h[0]._show()
            h[1].x = 300
            h[1]._show()
            h[2]._show()
            global NotasBaixo
            destroyNotes()
            updateNotes()

        # modo dificil
        if game.menu._hard:
            """ o _show() é para mostrar as 4 hitboxs do modo fácil """
            h[0]._show()
            h[1].x = 400
            h[1]._show()
            h[2]._show()
            h[3]._show()
            global NotasCima
            destroyNotes()
            updateNotes()

    """
        É possível fazer notas aleatórias usando randomint e definindo um intervalo de x à y pra cada Nota.
        Lembrando que o código funciona por ordem, então a nota de posição 1 no array NÃO PODE estar em uma
        Posição maior que a nota de posição 0.
    """

    NotasEsquerda = []
    NotasDireita = []
    NotasBaixo = []
    NotasCima = []

    personagem = PersonagemAssets('../assets/character/Personagem1.png')
    scorePlayer = Score()

game.start()
