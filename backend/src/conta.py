import csv
class Conta:
    def __init__(self, numero_da_conta: int, saldo: float, tipo_da_conta: str):
        self.numero_da_conta = numero_da_conta
        self.__saldo = saldo
        self.__tipo_da_conta = tipo_da_conta
        self.__cartoes = []
        self.__caixinhas = []
        self.__dividas = []
        
    def salvar_no_csv(self):

        with open("contas.csv", "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            
            escritor.writerow([
                self.numero_da_conta, 
                self.saldo, 
                self.tipo_da_conta
            ])

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
    def cartoes(self):
        return self.__cartoes
    @cartoes.setter
    def cartoes(self, val):
        self.__cartoes = val
        
    @property
    def caixinhas(self):
        return self.__caixinhas
    @caixinhas.setter
    def caixinhas(self, val):
        self.__caixinhas = val
        
    @property
    def dividas(self):
        return self.__dividas
    @dividas.setter
    def dividas(self, val):
        self.__dividas = val

    def transferencia(self, val, id_destinatario) -> bool:
        id_destinatario.saldo += val
        self.saldo -= val
        return True

    def excluir_cartao(self, numero_do_cartao: int):
        for cartao in self.cartoes:
            if numero_do_cartao == cartao.numero_do_cartao:
                self.cartoes.remove(cartao)