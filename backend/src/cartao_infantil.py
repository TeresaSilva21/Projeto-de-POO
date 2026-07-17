from cartao import Cartao

class CartaoInfantil(Cartao):
    def __init__(
        self,
        tipo: int,
        nome: str,
        numero: int,
        cvv: int,
        data_vencimento: str,
        bloqueado: bool,
    ):
        self.__tipo = tipo
        self.__nome = nome
        self.__numero = numero
        self.__cvv = cvv
        self.__data_vencimento = data_vencimento
        self.__bloqueado = bloqueado

    @property
    def nome(self) -> str:
        return self.__nome
        
    @property
    def tipo(self) -> int:
        return self.__tipo

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cvv(self) -> int:
        return self.__cvv

    @cvv.setter
    def cvv(self, val: int):
        self.__cvv = val
        
    @property
    def data_vencimento(self) -> str:
        return self.__data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, val: str):
        self.__data_vencimento = val

    @property
    def bloqueado(self) -> bool:
        return self.__bloqueado

    @bloqueado.setter
    def bloqueado(self, val: bool):
        self.__bloqueado = val