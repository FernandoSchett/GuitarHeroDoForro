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

h = [HitBox(100, 400, 'HitBoxArrow.png', 0),  # Hitboxes
     HitBox(200, 400, 'HitBoxArrow.png', 180),
     HitBox(200, 400, 'HitBoxArrow.png', 90),
     HitBox(300, 400, 'HitBoxArrow.png', 270),
     ]

def update():
    global counter
    global easy_inputs 
    global medium_inputs 
    global hard_inputs 
    global h
    global NotasEsquerda
    global NotasDireita
    global NotasCima
    global NotasBaixo
    
    if keyboard.is_key_just_down('space'):
        game._screen._file = 'music.png'

    """ if para o game.__screen de seleção de músicas """

    if keyboard.is_key_just_down('a'):
        game._screen._file = 'dificult.png'
        game.play('tarecoemariola.ogg')
    if keyboard.is_key_just_down('b'):
        game._screen._file = 'dificult.png'
        game.play('deixaeutesuperar.ogg')
    if keyboard.is_key_just_down('c'):
        game._screen._file = 'dificult.png'
        game.play('ocheirodecarolina.ogg')
    if keyboard.is_key_just_down('d'):
        game._screen._file = 'dificult.png'
        game.play('oxotedasmeninas.ogg')
    if keyboard.is_key_just_down('e'):
        game._screen._file = 'dificult.png'
        game.play('luaminha.ogg')

    """ if para o game.__screen de dificuldades """

    if game._screen._file == "dificult.png":
        if keyboard.is_key_just_down('1'):
            game._status = "easy"
            game._inputs = easy_inputs
            game._screen._file = '../assets/bg.png'
            game._end = True
        elif keyboard.is_key_just_down('2'):
            game._status = "medium"
            game._inputs = medium_inputs
            game._screen._file = '../assets/bg.png'
            game._end = True
        elif keyboard.is_key_just_down('3'):
            game._status = "hard"
            game._inputs = hard_inputs
            game._screen._file = '../assets/bg.png'
            game._end = True

    if not game._end:
        return
    
    if counter == 10:
        game.createNotes()
        counter = 0
    counter += 1
    
    # modo facil
    if game._status == "easy":
        """ o _show() é para mostrar as 2 hitboxs do modo fácil """
        h[0]._show()
        h[1]._show()
        game.destroyNotes()
        game.updateNotes()

    # modo medio
    if game._status == "medium":
        """ o _show() é para mostrar as 3 hitboxs do modo fácil """
        h[0]._show()
        h[1].x = 300
        h[1]._show()
        h[2]._show()
        game.destroyNotes()
        game.updateNotes()

    # modo dificil
    if game._status == "hard":
        """ o _show() é para mostrar as 4 hitboxs do modo fácil """
        h[0]._show()
        h[1].x = 400
        h[1]._show()
        h[2]._show()
        h[3]._show()
        game.destroyNotes()
        game.updateNotes()

"""
    É possível fazer notas aleatórias usando randomint e definindo um intervalo de x à y pra cada Nota.
    Lembrando que o código funciona por ordem, então a nota de posição 1 no array NÃO PODE estar em uma
    Posição maior que a nota de posição 0.
"""

run(globals())
