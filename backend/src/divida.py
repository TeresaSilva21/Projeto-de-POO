class Divida:
    def __init__(self, id: int, valor: float, data_vencimento: str):
        self.id = id
        self.__valor = valor
        self.__data_vencimento = data_vencimento

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, val: float):
        self.__valor = val

    @property
    def data_vencimento(self) -> str:
        return self.__data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, val: str):
        self.__data_vencimento = val