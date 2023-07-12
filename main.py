import random
import os
import pygame

from tupy import *
from src.classes.score import Score
from src.classes.notes import Notes
from src.classes.menu import Menu
from src.classes.hitbox import HitBox
from src.classes.personagemassets import PersonagemAssets
from src import *

pygame.init()

"""
    Tentativa de implementação por qwer (por hora) no update, sendo;
    q -> mais à esquerda
    r -> mais à direita
"""
menu = Menu()

def play(music):
    pygame.mixer.music.load(f"{os.path.join(os.path.dirname(__file__), './assets/sounds', music)}")
    pygame.mixer.music.play()


h = [HitBox(100, 400, '../assets/HitBoxArrow.png', 0),  # Hitboxes
     HitBox(200, 400, '../assets/HitBoxArrow.png', 180),
     HitBox(200, 400, '../assets//HitBoxArrow.png', 90),
     HitBox(300, 400, '../assets/HitBoxArrow.png', 270),
     ]

# Valores que variam de acordo com a dificuldade
easy_inputs = ['Left', 'Right', 100, 200]
medium_inputs = ['Left', 'Down', 'Right', 200, 100, 300]
hard_inputs = ['Left', 'Rigth', 'Up', 'Right', 300, 200, 100, 400]

counter = 0

if menu._end == False:
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
        if not menu._medium and not menu._hard:
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

        if not menu._hard:
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
            NotasEsquerda.append(Notes(menu._inputs[-2], 0, '../assets/image.png', 0, 4))
        if b < 24:
            NotasDireita.append(Notes(menu._inputs[-1], 0, '../assets/image.png', 180, 4))

        if not menu._medium and not menu._hard:
            return

        if a > 79:
            NotasBaixo.append(Notes(menu._inputs[-3], 0, '../assets/image1.png', 90, 4))

        if not menu._hard:
            return

        if b > 79:
            NotasCima.append(Notes(menu._inputs[-4], 0, './assets/image1.png', 270, 4))

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

        if not menu._medium and not menu._hard:
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

        if not menu._hard:
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
            menu._file = '../assets/music.png'

        """ if para o menu de seleção de músicas """

        if keyboard.is_key_just_down('A'):
            menu._file = 'dificult.png'
            play('../assets/sounds/tarecoemariola.ogg')
        if keyboard.is_key_just_down('B'):
            menu._file = 'dificult.png'
            play('../assets/sounds/deixaeutesuperar.ogg')
        if keyboard.is_key_just_down('C'):
            menu._file = 'dificult.png'
            play('../assets/sounds/ocheirodecarolina.ogg')
        if keyboard.is_key_just_down('D'):
            menu._file = 'dificult.png'
            play('../assets/sounds/oxotedasmeninas.ogg')
        if keyboard.is_key_just_down('E'):
            menu._file = 'dificult.png'
            play('../assets/sounds/luaminha.ogg')

        """ if para o menu de dificuldades """

        if menu._file == '../assets/dificult.png':
            if keyboard.is_key_just_down('1'):
                menu._easy = True
                menu._inputs = easy_inputs
                menu._file = '../assets/bg.png'
                menu._end = True
            elif keyboard.is_key_just_down('2'):
                menu._medium = True
                menu._inputs = medium_inputs
                menu._file = '../assets/bg.png'
                menu._end = True
            elif keyboard.is_key_just_down('3'):
                menu._hard = True
                menu._inputs = hard_inputs
                menu._file = '../assets/bg.png'
                menu._end = True

        if not menu._end:
            return
        if counter == 10:
            createNotes()
            counter = 0
        counter += 1
        # modo facil
        if menu._easy:
            """ o _show() é para mostrar as 2 hitboxs do modo fácil """
            h[0]._show()
            h[1]._show()
            global NotasEsquerda
            global NotasDireita
            destroyNotes()
            updateNotes()

        # modo medio
        if menu._medium:
            """ o _show() é para mostrar as 3 hitboxs do modo fácil """
            h[0]._show()
            h[1].x = 300
            h[1]._show()
            h[2]._show()
            global NotasBaixo
            destroyNotes()
            updateNotes()

        # modo dificil
        if menu._hard:
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

    personagem = PersonagemAssets('../assets/Personagem1.png')
    scorePlayer = Score()

run(globals())
