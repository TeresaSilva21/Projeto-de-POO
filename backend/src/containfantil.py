from conta import Conta
from cartaoinfantil import CartaoInfantil

class ContaInfantil(Conta):
    def __init__(self, limite_diario: float, saldo: float, tipo: int):
        self.limite_diario = limite_diario
        self.__saldo = saldo
        self.__tipo = tipo
        self.cartoes: list[CartaoInfantil] = []

    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, val: float):
        self.__saldo = val
        
    @property
    def tipo(self) -> str:
        return self.__tipo
    @tipo.setter
    def tipo(self, val: str):
        self.__tipo = val

    @property
    def cartoes(self) -> list[CartaoInfantil]:
        return self.__cartoes
    @cartoes.setter
    def cartoes(self, val: list[CartaoInfantil]):
        self.__cartoes = val

    def transferencia(self, val: float, conta_destinatario: Conta) -> bool:
        conta_destinatario.saldo += val
        self.saldo -= val