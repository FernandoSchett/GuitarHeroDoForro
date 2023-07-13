from src.classes.hitbox import HitBox
import os

path_file = ""

# Valores que variam de acordo com a dificuldade
easy_inputs = ['Left', 'Right', 100, 200]
medium_inputs = ['Left', 'Down', 'Right', 200, 100, 300]
hard_inputs = ['Left', 'Rigth', 'Up', 'Right', 300, 200, 100, 400]

counter = 0

all_status = {
    1: "easy",
    2: "medium",
    3: "hard",
    4: "end"
}

catalogo = {
    'A': 'tarecoemariola.ogg',
    'B': 'deixaeutesuperar.ogg',
    'C': 'ocheirodecarolina.ogg',
    'D': 'oxotedasmeninas.ogg',
    'E': 'luaminha.ogg'
}

NotasEsquerda = []
NotasDireita = []
NotasBaixo = []
NotasCima = []

h = [HitBox(100, 400, 'HitBoxArrow.png', 0),  # Hitboxes
     HitBox(200, 400, 'HitBoxArrow.png', 180),
     HitBox(200, 400, 'HitBoxArrow.png', 90),
     HitBox(300, 400, 'HitBoxArrow.png', 270),
     ]