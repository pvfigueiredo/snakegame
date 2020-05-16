from Posicao import Posicao


class Cobra:
    def __init__(self, cor):
        self.cor = cor
        self.posicao = Posicao(300, 300)
        self.tail = []    

    def come(self)->bool:
        colisao = True
        return colisao

    def cresce(self):
        pass

    def movimenta(self, key: str):
        self.posicao.move(key)
        
        