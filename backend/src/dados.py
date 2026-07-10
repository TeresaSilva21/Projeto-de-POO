class DadosUsuario:
    def __init__(self, nome: str, cpf: str, renda: float):
        self.nome = nome
        self.__cpf = cpf
        self.__renda = renda
        self.__criancas: list[DadosUsuarioInfantil] = []
        self.__contas: list[DadosConta] = []
class DadosInicial:
    usuario: DadosUsuario
    saldo: float  
class DadosCartaoInfantil:
        tipo: int
        nome: str
        numero: int
        cvv: int
        data_vencimento: str
        bloqueado: bool
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
class DadosUsuarioInfantil:
    id: int
    nome: str
    contas: list[DadosContaInfantil]