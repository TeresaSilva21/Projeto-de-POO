import csv
class UsuarioInfantil:
    def __init__(self, id: int, nome: str, senha: str):
        self.id = id
        self.nome = nome
        self.__senha = senha
        self.__contas = []

    def validar(self, senha: str) -> bool:
        if self.__senha == senha:
            return True
        else:
            return False
        
    def salvar_no_csv(self):

        with open("usuarios_infantis.csv", "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            
            escritor.writerow([
                self.id, 
                self.nome, 
                self.senha 
            ])

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
    def contas(self):
        return self.__contas
    
    @contas.setter                
    def contas(self, numero_da_conta):
        self.__contas.append(numero_da_conta)