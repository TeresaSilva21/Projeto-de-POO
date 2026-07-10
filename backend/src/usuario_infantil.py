from containfantil import ContaInfantil

class UsuarioInfantil:
    def __init__(self, id: int, nome: str, senha: str):
        self.id = id
        self.nome = nome
        self.__senha = senha
        self.__contas = list[ContaInfantil]

    def validar(self, senha: str) -> bool:
        if self.__senha == senha:
            return True
        else:
            return False

    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter                
    def senha(self, nova_senha):
        if nova_senha == "":
            raise ValueError(f'Senha inválida.')
        else:
            self.__senha = nova_senha

    @property
    def contas(self) -> list[ContaInfantil]:
        return list[ContaInfantil]
    
    @contas.setter                
    def contas(self, other: list[ContaInfantil]):
        self.__contas = other
        
