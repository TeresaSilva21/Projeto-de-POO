from mixin import AuditoriaMixin
from usuario import Usuario
from usuario_infantil import UsuarioInfantil
from conta import Conta
from conta_infantil import ContaInfantil

class Sessao(AuditoriaMixin):
    def criar_usuario(self, id: int, nome: str, cpf: str, renda: float, senha: str):
        usuario = Usuario(id, nome, cpf, renda, senha)
        self.log('Usuário foi criado com sucesso!')
        return usuario
    
    def criar_usuario_infantil(self, id, nome, senha):
        usuarioInfantil = UsuarioInfantil(id, nome, senha)
        self.log('Usuário infantil foi criado com sucesso!')
        return usuarioInfantil

    
    def criar_conta(self, numero_da_conta, saldo, tipo_da_conta):
        conta = Conta(numero_da_conta, saldo, tipo_da_conta)
        self.log('Conta foi criada com sucesso!')
        return conta

    
    def criar_conta_infantil(self, numero_da_conta, saldo, tipo_da_conta):
        contaInfantil = ContaInfantil(numero_da_conta, saldo, tipo_da_conta)
        self.log('Conta infantil foi criada com sucesso!')
        return contaInfantil
