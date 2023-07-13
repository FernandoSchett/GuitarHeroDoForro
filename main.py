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

def update():
    print("entrou update")
    key = keyboard.get_pressed()
    pressed_key = None

    if keyboard.is_key_just_down('space'):
        game.__screen._file= './assets/music.png'
    
    if key['a'] or key['A']:
        pressed_key = 'A'
    elif key['b'] or key['B']:
        pressed_key = 'B'
    elif key['c'] or key['C']:
        pressed_key = 'C'
    elif key['d'] or key['D']:
        pressed_key = 'D'
    elif key['e'] or key['E']:
        pressed_key = 'E'

    if pressed_key:
        game.__screen._file = 'dificult.png'
        sound = catalogo.get(pressed_key, None)
        if sound:
            game.play(sound)

    """ if para o menu de dificuldades """

    if game.menu._file == "dificult.png":
        if keyboard.is_key_just_down('1'):
            game.menu._easy = True
            game.screen._inputs = easy_inputs
            game.screen._file = '../assets/bg.png'
            game.screen._end = True
        elif keyboard.is_key_just_down('2'):
            game.screen._medium = True
            game.screen._inputs = medium_inputs
            game.screen._file = '../assets/bg.png'
            game.screen._end = True
        elif keyboard.is_key_just_down('3'):
            game.screen._hard = True
            game.screen._inputs = hard_inputs
            game.screen._file = '../assets/bg.png'
            game.screen._end = True

    if not game._status == "end":
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
