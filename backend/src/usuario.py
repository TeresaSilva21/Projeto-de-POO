from conta import Conta
from usuario_infantil import UsuarioInfantil
from mixin import AuditoriaMixin

class Usuario(AuditoriaMixin):
    def __init__(self, id: int, nome: str, cpf: str, renda: float, senha: str):
        self.id = id
        self.nome = nome
        self.__cpf = cpf
        self.__renda = renda
        self.__senha = senha
        self.__criancas: list[UsuarioInfantil] = []
        self.__contas: list[Conta] = []

    def validar(self, senha: str) -> bool:
        if self.__senha == senha:
            return True
        else:
            return False

    def excluir_conta(self, id: int) -> bool:
        if len(self.__contas[id].dividas) == 0:
            del self.__contas[id]
        else:
            raise Exception("O usuário contém dividas.")

    @property
    def cpf(self):
        return self.__cpf
    @property
    def renda(self):
        return self.__renda
    @property
    def senha(self):
        return self.__senha
    @property
    def criancas(self):
        return list[UsuarioInfantil]
    @property
    def contas(self):
        return list[Conta]
    
    @cpf.setter
    def cpf(self, novo_cpf: str):
        if novo_cpf == "000000000-00":
            raise ValueError(f'CPF inválido.')
        else:
            self.__cpf = novo_cpf
    @renda.setter
    def renda(self, nova_renda: float):
        if nova_renda <= 0:
            raise ValueError(f'Renda inválida')
        else:
            self.__renda = nova_renda
    @senha.setter
    def senha(self, nova_senha: str):
        if nova_senha == "":
            raise ValueError(f'Senha inválida.')
        else:
            self.__senha = nova_senha
    @criancas.setter
    def criancas(self, other: UsuarioInfantil):
        self.__criancas = other


    def adicionar_crianca(self, crianca: UsuarioInfantil):
        self.__criancas.append(crianca)

    @contas.setter                
    def contas(self, other: list[Conta]):
        self.__contas = other