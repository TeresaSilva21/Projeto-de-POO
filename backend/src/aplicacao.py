from flask import jsonify

from dados import DadosCaixinha, DadosCartao, DadosConta, DadosContaInfantil, DadosDivida, DadosInicial, DadosUsuario, DadosUsuarioInfantil
from mixin import AuditoriaMixin
from sessao import Sessao

sessao = Sessao()

def procurar_por(objects, key, value):
    for obj in objects:
        if obj.get(key) == value:
            return obj

class Aplicacao(AuditoriaMixin):
    def carregar_dados_inicial(self, jwt: str, num_conta: int) -> DadosInicial:
        usuario = sessao.obter_usuario(jwt)
        d = {
            'nome': usuario.nome,
            'cpf': usuario.cpf
        }

        return jsonify({
            "usuario": d,
            'saldo': procurar_por(usuario.conta, "numero_da_conta", num_conta)
        })

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

    def obter_dados_caixinhas(self, cpf: str) -> list[DadosCaixinha]:
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