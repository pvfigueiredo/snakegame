from tkinter import Canvas
from tkinter import mainloop
from tkinter import Tk
import random


WIDTH = 500
HEIGHT = 400
x = 150
y = 200
pontos = 0
coord = (0,0)

def get_movimento(key):
    mov = {
        'a': (-10, 0),
        'd': (10, 0),
        's': (0, 10),
        'w': (0, -10)
    }
    return mov.get(key, 0)

def evento(e):
    global x, y, coord, cancel
    coord = get_movimento(e.char)
    if cancel != None:
        canvas.after_cancel(cancel)
    move()
    

def move():
    global x, y, cobra, xc, yc, tam, cancel
    x += coord[0]
    y += coord[1]    
    if limites(x, y):        
        if x == xc and y == yc:
            drop_comida()
            incrementa_score()
            tam += 1
        else:            
            canvas.delete(cobra[tam - 1])
            cobra.insert(0, canvas.create_rectangle(x, y, x + 10, y + 10, fill='blue'))
    else:
        return
    
    cancel = canvas.after(75, move)
    
def limites(xt, yt):
    return 10 <= xt <= 290 and 10 <= yt <= 390

def drop_comida():
    global comida, xc, yc
    canvas.delete(comida)
    gera_coord_comida()
    comida = canvas.create_rectangle(xc, yc, xc + 10, yc + 10, fill='red')

def gera_coord_comida():
    global xc, yc
    xc = (random.randint(10, 290)//10) * 10
    yc = (random.randint(10, 150)//10) * 10

def incrementa_score():
    global pontos
    pontos += 100
    score = canvas.find_withtag('score')
    canvas.itemconfigure(score, text=f'Pontos: {pontos}', tag='score')
 

root = Tk()

cancel = None
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_text(
    350, 50, text=f'Pontos: {pontos}', tag='score'
)

tam = 0
cobra = []
cobra.append(canvas.create_rectangle(x, y, x + 10, y + 10, fill='blue'))
tam += 1

gera_coord_comida()
comida = canvas.create_rectangle(xc, yc, xc + 10, yc + 10, fill='red')

limite_sup = canvas.create_line(10, 10, 300, 10)
limite_dir = canvas.create_line(300, 10, 300, 400)
limite_inf = canvas.create_line(10, 400, 300, 400)
limite_esq = canvas.create_line(10, 10, 10, 400)

root.bind('<Key>', evento)
mainloop()
