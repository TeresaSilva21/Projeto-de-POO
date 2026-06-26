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
        self.__tipo = val

    @property
    @abstractmethod
    def cdi(self) -> NotImplementedType:
        raise NotImplementedError

    @cdi.setter
    @abstractmethod
    def cdi(self, val: int):
        self.__cdi = val

    @abstractmethod
    def depositar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def calcular_rendimento(self, valor: float, tempo: float) -> float:
        pass

class DadosInicial:
    nome: str
    saldo: float

class Sessao:
    def __init__(self):
        self.__usuarios_cadastrados: list[Usuario] = []
        
    def Autenticar(self, cpf: str, senha: str) -> str:
        pass
    
    def obter_usuario(self, jwt: str) -> Usuario:
        pass
    
    def excluir_usuario(self, usuario: Usuario) -> bool:
        pass
    
    def criar_usuario(self, nome: str, cpf: str, renda: float, senha: str) -> Usuario:
        pass
    

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
    def nome(self) -> NotImplementedType:
        raise NotImplementedError

    @nome.setter
    def nome(self, val: str):
        self.__nome = val

    @property
    def numero(self) -> NotImplementedType:
        raise NotImplementedError

    @numero.setter
    def numero(self, val: int):
        self.__numero = val

    @property
    def cvv(self) -> NotImplementedType:
        raise NotImplementedError

    @cvv.setter
    def cvv(self, val: int):
        self.__cvv = val

    @property
    def data_vencimento(self) -> NotImplementedType:
        raise NotImplementedError

    @data_vencimento.setter
    def data_vencimento(self, val: str):
        self.__data_vencimento = val

    @property
    def limite_usado(self) -> NotImplementedType:
        raise NotImplementedError

    @limite_usado.setter
    def limite_usado(self, val: float):
        self.__limite_usado = val

    @property
    def limite_total(self) -> NotImplementedType:
        raise NotImplementedError

    @limite_total.setter
    def limite_total(self, val: float):
        self.__limite_total = val

    @property
    def bloqueado(self) -> NotImplementedType:
        raise NotImplementedError

    @bloqueado.setter
    def bloqueado(self, val: bool):
        self.__bloqueado = val

class DadosCartaoInfantil:
        tipo: int
        nome: str
        numero: int
        cvv: int
        data_vencimento: str
        bloqueado: bool

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
    def nome(self) -> NotImplementedType:
        raise NotImplementedError

    @nome.setter
    def nome(self, val: str):
        self.__nome = val

    @property
    def numero(self) -> NotImplementedType:
        raise NotImplementedError

    @numero.setter
    def numero(self, val: int):
        self.__numero = val

    @property
    def cvv(self) -> NotImplementedType:
        raise NotImplementedError

    @cvv.setter
    def cvv(self, val: int):
        self.__cvv = val

    @property
    def bloqueado(self) -> NotImplementedType:
        raise NotImplementedError

    @bloqueado.setter
    def bloqueado(self, val: bool):
        self.__bloqueado = val


class Divida:
    def __init__(self, id: int, valor: float, data_vencimento: str):
        self.id = id
        self.__valor = valor
        self.__data_vencimento = data_vencimento

    @property
    def valor(self) -> NotImplementedType:
        raise NotImplementedError

    @valor.setter
    def valor(self, val: float):
        self.__valor = val


class Conta:
    def __init__(self, numero_da_conta: int, saldo: float, tipo_da_conta: str):
        self.numero_da_conta = numero_da_conta
        self.__saldo = saldo
        self.__tipo_da_conta = tipo_da_conta
        self.__cartoes: list[Cartao] = []
        self.__caixinhas: list[Caixinha] = []
        self.__dividas: list[Divida] = []

    @property
    def saldo(self) -> NotImplementedType:
        raise NotImplementedError

    @saldo.setter
    def saldo(self, val: float):
        self.__saldo = val

    @saldo.getter
    def saldo(self) -> float:
        return self.__saldo

    def transferencia(self, conta_destinatario: Conta) -> bool:
        pass

    def excluir_cartao(self, numero_do_cartao: int):
        pass


class ContaInfantil(Conta):
    def __init__(self, limite_diario: float, saldo: float, tipo: int):
        self.limite_diario = limite_diario
        self.__saldo = saldo
        self.__tipo = tipo
        self.cartoes: list[CartaoInfantil] = []

    def transferencia(self, conta_destinatario: Conta) -> bool:
        pass


class Caixinha(Investimento):
    def __init__(self, nome: str):
        self.nome = nome

    def trancar(self, tempo: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        pass

    def sacar(self, valor: float) -> bool:
        pass

    def calcular_rendimento(self, valor: float, tempo: float) -> float:
        pass

class DadosCartao:
    tipo: int
    nome: str
    numero: int
    cvv: int
    data_vencimento: str
    limite_usado: float
    limite_total: float
    bloqueado: bool

class DadosContaInfantil:
    limite_diario: float
    saldo: float
    tipo: int
    cartoes: list[DadosCartao] = []


class DadosCaixinha:
    nome: str


class DadosDivida:
    id: int
    valor: float
    vencimento: str


class DadosConta:
    numero_da_conta: int
    saldo: float
    tipo: int
    cartoes: list[DadosCartao] = []
    caixinhas: list[DadosCaixinha] = []
    dividas: list[DadosDivida] = []

class DadosUsuario:
    def __init__(self, nome: str, cpf: str, renda: float):
        self.nome = nome
        self.__cpf = cpf
        self.__renda = renda
        self.__criancas: list[DadosUsuarioInfantil] = []
        self.__contas: list[DadosConta] = []

class DadosUsuarioInfantil:
    id: int
    nome: str
    contas: list[ContaInfantil]


class UsuarioInfantil:
    def __init__(self, id: int, nome: str, senha: str):
        self.id = id
        self.nome = nome
        self.__senha = senha
        self.__contas = list[ContaInfantil]

    def validar(self, senha: str) -> bool:
        pass


class Usuario:
    def __init__(self, nome: str, cpf: str, renda: float, senha: str):
        self.nome = nome
        self.__cpf = cpf
        self.__renda = renda
        self.__senha = senha
        self.__criancas: list[UsuarioInfantil] = []
        self.__contas: list[Conta] = []

    def validar(self, senha: str) -> bool:
        pass

    def excluir_conta(self, conta: Conta, divida: Divida) -> bool:
        pass

class BancoDeDados:
    def __init__(self, endereco: str, senha: str):
        self.__endereco = endereco
        self.__senha = senha

    def criar_usuario(self, usuario: Usuario) -> bool:
        pass

    def excluir_usuario(self, usuario: Usuario) -> bool:
        pass

    def criar_usuario_infantil(
        self, usuario_responsavel: Usuario, senha_crianca: str
    ) -> UsuarioInfantil:
        pass

    def excluir_usuario_infantil(
        self, usuario_responsavel: Usuario, usuario_infantil: UsuarioInfantil
    ) -> bool:
        pass

    def obter_usuarios(self) -> list[Usuario]:
        pass

    def criar_conta(self, usuario: Usuario, tipo: int) -> Conta:
        pass

    def excluir_conta(self, usuario: Usuario, conta: Conta) -> bool:
        pass

    def alterar_saldo(self, usuario: Usuario, conta: Conta) -> bool:
        pass

    def criar_divida(
        self, divida: Divida, usuario_remetente: Usuario, usuario_destinatario: Usuario
    ) -> bool:
        pass

    def pagar_divida(self, divida: Divida) -> bool:
        pass

    def obter_dividas(self, usuario_destinatario: Usuario) -> list[Divida]:
        pass

    def criar_cartao(self, usuario: Usuario, cartao: Cartao) -> bool:
        pass

    def bloquear_cartao(self, cartao: Cartao) -> bool:
        pass

    def alterar_limite_cartao(self, cartao: Cartao) -> bool:
        pass

    def criar_caixinha(self, conta: Conta, caixinha: Caixinha) -> bool:
        pass

    def exclur_caixinha(self, conta: Conta, caixinha: Caixinha) -> bool:
        pass

    def trancar_caixinha(self, conta: Conta, caixinha: Caixinha) -> bool:
        pass

    def obter_caixinhas(self, usuario: Usuario) -> list[Caixinha]:
        pass

    def carregar_dados_inicial(self, usuario: Usuario) -> DadosInicial:
        pass

    def obter_cartoes(self, usuario: Usuario) -> list[Cartao]:
        pass

    def contas_infantis_responsavel(
        self, usuario_responsavel: Usuario
    ) -> list[ContaInfantil]:
        pass


class AuditoriaMixin:
    def log(self, mensagem: str) -> str:
        pass


class ApiMixin:
    def iniciar_app(self) -> App:
        pass


class Aplicacao(AuditoriaMixin, ApiMixin):
    def carregar_dados_inicial(self, jwt: str) -> DadosInicial:
        pass

    def logar(self, cpf: str, senha: str) -> str:
        pass

    def logar_infantil(self, cpf_responsavel: str, senha: str) -> str:
        pass

    def obter_cartoes(self, cpf: str) -> list[DadosCartao]:
        pass

    def criar_usuario(
        self, nome: str, cpf: str, renda: float, senha: str
    ) -> DadosUsuario:
        pass

    def excluir_usuario(self, cpf: str, senha: str) -> bool:
        pass

    def criar_conta(self, cpf: str, tipo: int) -> DadosConta:
        pass

    def excluir_conta(self, cpf: str, numero_da_conta: int) -> bool:
        pass

    def obter_dados_caixinhas(self, cpf: str) -> list[Caixinha]:
        pass

    def criar_divida(
        self, cpf_rementente: str, cpf_destinatario: str, valor: float
    ) -> DadosDivida:
        pass

    def pagar_divida(self, cpf_destinatario: str, id: int) -> bool:
        pass

    def obter_dividas(self, cpf: str) -> list[DadosDivida]:
        pass

    def criar_usuario_infantil(
        self, cpf_responsavel: str, nome_crianca: str, senha_crianca: str
    ) -> DadosUsuarioInfantil:
        pass

    def excluir_usuario_infantil(self, cpf_responsavel: str, id: int) -> bool:
        pass

    def usuarios_infantis_responsavel(
        self, cpf_responsavel: str
    ) -> list[DadosUsuarioInfantil]:
        pass

    def criar_conta_infantil(self, cpf_responsavel: str, id: int) -> DadosContaInfantil:
        pass

    def deletar_conta_infantil(self, cpf_responsavel: str, id: int) -> bool:
        pass

    def contas_infantis_responsavel(
        self, cpf_responsavel: str
    ) -> list[DadosContaInfantil]:
        pass

