from conta import Conta
from seguranca_parental import SegurancaParental
import csv

class ContaInfantil(Conta, SegurancaParental):
    def __init__(self, numero_da_conta, saldo: float, tipo: int):
        self.numero_da_conta = numero_da_conta
        self.__saldo = saldo
        self.__tipo = tipo
        self.cartoes = []
        
    def salvar_no_csv(self):
        with open("contas_infantis.csv", "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            
            escritor.writerow([
                self.numero_da_conta, 
                self.saldo, 
                self.tipo
            ])

    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, val: float):
        self.__saldo = val
        
    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def cartoes(self):
        return self.__cartoes
    @cartoes.setter
    def cartoes(self, val):
        self.__cartoes = val

    def transferencia(self, val: float, conta_destinatario) -> bool:
        conta_destinatario.saldo += val
        self.saldo -= val