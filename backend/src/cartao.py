class Cartao:
    def __init__(
        self,
        tipo: int,
        nome: str,
        numero: int,
        cvv: int,
        data_vencimento: str,
        limite_usado: float,
        limite_total: float,
        bloqueado: bool,
    ):
        self.__tipo = tipo
        self.__nome = nome
        self.__numero = numero
        self.__cvv = cvv
        self.__data_vencimento = data_vencimento
        self.__limite_usado = limite_usado
        self.__limite_total = limite_total
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

    @property
    def data_vencimento(self) -> str:
        return self.__data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, val: str):
        self.__data_vencimento = val

    @property
    def limite_usado(self) -> float:
        return self.__limite_usado

    @limite_usado.setter
    def limite_usado(self, val: float):
        self.__limite_usado = val

    @property
    def limite_total(self) -> float:
        return self.__limite_total

    @limite_total.setter
    def limite_total(self, val: float):
        self.__limite_total = val

    @property
    def bloqueado(self) -> bool:
        return self.__bloqueado

    @bloqueado.setter
    def bloqueado(self, val: bool):
        self.__bloqueado = val