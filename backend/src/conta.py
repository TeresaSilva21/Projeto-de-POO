from cartao import Cartao
from caixinha import Caixinha
from divida import Divida

class Conta:
    def __init__(self, numero_da_conta: int, saldo: float, tipo_da_conta: str):
        self.numero_da_conta = numero_da_conta
        self.__saldo = saldo
        self.__tipo_da_conta = tipo_da_conta
        self.__cartoes: list[Cartao] = []
        self.__caixinhas: list[Caixinha] = []
        self.__dividas: list[Divida] = []

    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, val: float):
        self.__saldo = val
        
    @property
    def tipo_da_conta(self) -> str:
        return self.__tipo_da_conta
    @tipo_da_conta.setter
    def tipo_da_conta(self, val: str):
        self.__tipo_da_conta = val
        
    @property
    def cartoes(self) -> list[Cartao]:
        return self.__cartoes
    @cartoes.setter
    def cartoes(self, val: list[Cartao]):
        self.__cartoes = val
        
    @property
    def caixinhas(self) -> list[Caixinha]:
        return self.__caixinhas
    @caixinhas.setter
    def caixinhas(self, val: list[Caixinha]):
        self.__caixinhas = val
        
    @property
    def dividas(self) -> list[Divida]:
        return self.__dividas
    @dividas.setter
    def dividas(self, val: list[Divida]):
        self.__dividas = val

    def transferencia(self, val: float, conta_destinatario) -> bool:
        conta_destinatario.saldo += val
        self.saldo -= val
        return True

    def excluir_cartao(self, numero_do_cartao: int):
        for cartao in self.cartoes:
            if numero_do_cartao == cartao.numero_do_cartao:
                self.cartoes.remove(cartao)