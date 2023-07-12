from src.classes.hitbox import HitBox
import os

path_file = ""

# Valores que variam de acordo com a dificuldade
easy_inputs = ['Left', 'Right', 100, 200]
medium_inputs = ['Left', 'Down', 'Right', 200, 100, 300]
hard_inputs = ['Left', 'Rigth', 'Up', 'Right', 300, 200, 100, 400]

h = [HitBox(100, 400, os.path.join(path_file, 'assets/HitBoxArrow.png'), 0),  # Hitboxes
     HitBox(200, 400, os.path.join(path_file, 'assets/HitBoxArrow.png'), 180),
     HitBox(200, 400, os.path.join(path_file, 'assets/HitBoxArrow.png'), 90),
     HitBox(300, 400, os.path.join(path_file, 'assets/HitBoxArrow.png'), 270),
     ]

counter = 0
