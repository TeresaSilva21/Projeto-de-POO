import csv

class Usuario:
    def __init__(self, id: int, nome: str, cpf: str, renda: float, senha: str):
        self.id = id
        self.nome = nome
        self.__cpf = cpf
        self.__renda = renda
        self.__senha = senha
        self.__criancas = []
        self.__contas = []
        
    def salvar_no_csv(self):
        with open("usuarios.csv", "a", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            
            escritor.writerow([
                self.id, 
                self.nome, 
                self.cpf, 
                self.renda, 
                self.senha
            ])

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
        return self.__criancas
    @property
    def contas(self):
        return self.__contas
    
    @senha.setter
    def senha(self, nova_senha: str):
        if nova_senha == "":
            raise ValueError(f'Senha inválida.')
        else:
            self.__senha = nova_senha
            
    @criancas.setter
    def criancas(self, id):
        self.__criancas.append(id)

    @contas.setter                
    def contas(self, numero_da_conta):
        self.__contas.append(numero_da_conta)