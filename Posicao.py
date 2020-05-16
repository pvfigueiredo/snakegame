

class Posicao:
    def __init__(self, x: int, y: int):
        self.pos = {'x': x, 'y': y}

    def get_direcao(self, key: str)->tuple:
        direcao = {
            'a': (-1, 0),
            's': (0, 1),
            'd': (1, 0),
            'w': (0, -1)
        }
        return direcao.get(key, 0)

    def move(self, mov: tuple):
        self.pos['x'] += mov[0]
        self.pos['y'] += mov[1]
    
    def muda_direcao(self, key: str):
        mov = self.get_direcao(key)
        self.move(mov)
        