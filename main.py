import random
import os

from tupy import *
from src.classes.guitar_hero_forro import GuitarHeroForro
from src.global_var import *

path_file = os.path.dirname(__file__)
game = GuitarHeroForro()

"""
    Tentativa de implementação por qwer (por hora) no update, sendo;
    q -> mais à esquerda
    r -> mais à direita
"""

print("tome")

def update():
    global h
    global counter

    if keyboard.is_key_just_down('space'):
        game.__screen._file= './assets/music.png'
    
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
        game.createNotes()
        counter = 0
    counter += 1
    
    # modo facil
    if game.menu._easy:
        """ o _show() é para mostrar as 2 hitboxs do modo fácil """
        h[0]._show()
        h[1]._show()
        global NotasEsquerda
        global NotasDireita
        game.destroyNotes()
        game.updateNotes()

    # modo medio
    if game.menu._medium:
        """ o _show() é para mostrar as 3 hitboxs do modo fácil """
        h[0]._show()
        h[1].x = 300
        h[1]._show()
        h[2]._show()
        global NotasBaixo
        game.destroyNotes()
        game.updateNotes()

    # modo dificil
    if game.menu._hard:
        """ o _show() é para mostrar as 4 hitboxs do modo fácil """
        h[0]._show()
        h[1].x = 400
        h[1]._show()
        h[2]._show()
        h[3]._show()
        global NotasCima
        game.destroyNotes()
        game.updateNotes()

"""
    É possível fazer notas aleatórias usando randomint e definindo um intervalo de x à y pra cada Nota.
    Lembrando que o código funciona por ordem, então a nota de posição 1 no array NÃO PODE estar em uma
    Posição maior que a nota de posição 0.
"""

game.start()
