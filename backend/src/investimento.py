''# 2026 CardBank, all rights reserved
#
from abc import ABC, abstractmethod
from types import NotImplementedType


class Investimento(ABC):
    @property
    @abstractmethod
    def tipo(self) -> NotImplementedType:
        raise NotImplementedError

    @tipo.setter
    @abstractmethod
    def tipo(self, val: int):
        raise NotImplementedError

    @property
    @abstractmethod
    def cdi(self) -> NotImplementedType:
        raise NotImplementedError

    @cdi.setter
    @abstractmethod
    def cdi(self, val: int):
        raise NotImplementedError

    @abstractmethod
    def depositar(self, valor: float) -> bool:
        raise NotImplementedError

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        raise NotImplementedError

    @abstractmethod
    def calcular_rendimento(self, valor: float, tempo: float) -> float:
        raise NotImplementedError