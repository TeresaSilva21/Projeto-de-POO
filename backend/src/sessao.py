import os
import psycopg
from usuario import Usuario
from flask.cli import load_dotenv
from bancodados import BancoDeDados
from bancodados import BancoDeDados

load_dotenv()

banco = BancoDeDados()

class Sessao:
        
    def autenticar(self, cpf: str, senha: str) -> str:
        pass
    
    def obter_usuario(self, jwt: str) -> Usuario:
        decoded = jwt.decode(jwt, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        
        usuario = banco.obter_usuario(decoded["id"])

        return usuario
    
    def excluir_usuario(self, usuario: Usuario) -> bool:
        BancoDeDados.excluir_usuario(usuario)
            
    def criar_usuario(self, id: int, nome: str, cpf: str, renda: float, senha: str) -> Usuario:
        usuario = Usuario(id, nome, cpf, renda, senha)
        return usuario