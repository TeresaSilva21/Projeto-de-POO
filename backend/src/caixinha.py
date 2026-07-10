from investimento import Investimento


class Caixinha(Investimento):
    def __init__(self, nome: str):
        self.nome = nome

    def trancar(self, tempo: float) -> bool:
        if tempo > 0:
            return True
        elif tempo <= 0:
            return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            return True
        elif valor <= 0:
            return False

    def sacar(self, valor: float) -> bool:
        if valor > 0:
            return True
        elif valor <= 0:
            return False
            
    def calcular_rendimento(self, valor: float, tempo: float) -> float:
        pass