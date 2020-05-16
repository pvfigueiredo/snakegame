from tkinter import Canvas
from tkinter import mainloop
from tkinter import Tk
import random


def get_movimento(key):
    mov = {
        'a': (-10, 0),
        'd': (10, 0),
        's': (0, 10),
        'w': (0, -10)
    }
    return mov.get(key, 0)

def move_rec(event):
    global x, y, cobra, xc, yc, tam
    coord = get_movimento(event.char)
    if limites(x + coord[0]) and limites(y + coord[1]):
        if x == xc and y == yc:
            drop_comida()
            tam += 1
        else:
            x += coord[0] 
            y += coord[1]
            canvas.delete(cobra[tam - 1])
            cobra.insert(0, canvas.create_rectangle(x, y, x + 10, y + 10, fill='blue'))         

def limites(val):
    return 10 <= val <= 580

def drop_comida():
    global comida, xc, yc
    canvas.delete(comida)
    gera_coord_comida()
    comida = canvas.create_rectangle(xc, yc, xc + 10, yc + 10, fill='red')

def gera_coord_comida():
    global xc, yc
    xc = (random.randint(10, 590)//10) * 10
    yc = (random.randint(10, 590)//10) * 10

    

root = Tk()

WIDTH = HEIGHT = 600
x = y = 300

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

tam = 0
cobra = []
cobra.append(canvas.create_rectangle(x, y, x + 10, y + 10, fill='blue'))
tam += 1

gera_coord_comida()
comida = canvas.create_rectangle(xc, yc, xc + 10, yc + 10, fill='red')

limite_sup = canvas.create_line(10, 10, 590, 10)
limite_dir = canvas.create_line(590, 10, 590, 590)
limite_inf = canvas.create_line(10, 590, 590, 590)
limite_esq = canvas.create_line(10, 10, 10, 590)

root.bind('<Key>', move_rec)
mainloop()
