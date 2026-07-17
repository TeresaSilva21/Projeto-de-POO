from caixinha import *
from cartao import *
from cartao_infantil import *
from conta import *
from conta_infantil import *
from divida import *
from investimento import *
from mixin import *
from seguranca_parental import *
from usuario_infantil import *
from usuario import *
from sessao import Sessao
import csv

with open("dados/usuarios.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

def main():
    verificacao_usuario = False
    verificacao_usuario_infantil = False
    verificacao_conta = False
    verificacao_conta_infantil = False
    while True:
        
        
        print("SELECIONE:")
        print("01 -> Criar usuário.")
        print("02 -> Criar usuário infantil.")
        print("03 -> Criar conta.")
        print("04 -> Criar conta infantil.")

        option = input("-> ")
        
        if option == "01":
            
            print("Informe:")

            print("ID:")
            id = int(input("-> "))

            print("NOME:")
            nome = input("-> ")

            print("CPF:")
            cpf = input("-> ")

            print("RENDA:")
            renda = float(input("-> "))

            print("SENHA:")
            senha = input("-> ")

            usuario_atual = Sessao.criar_usuario(id, nome, cpf, renda, senha)
            usuario_atual.salvar_no_csv()
            
            verificacao_usuario = True
            
        elif option == "02":
            print("Informe:")    

            print("ID:")
            id = int(input("-> "))   

            print("NOME:")
            nome = input("-> ")

            print("SENHA:")
            senha = input("-> ")

            usuario_infantil_atual = Sessao.criar_usuario_infantil(id, nome, senha)
            usuario_infantil_atual.salvar_no_csv()
            usuario_atual.contas = numero_conta
            verificacao_usuario_infantil = True

        elif option == "03":
            if verificacao_usuario == False:
                print("Crie usuário primeiro para poder criar uma conta!")
            else:
                print("Informe:")    

                print("NÚMERO DA CONTA:")
                numero_conta = int(input("-> "))   

                print("SALDO:")
                saldo = float(input("-> "))

                print("TIPO DA CONTA:")
                tipo_da_conta = int(input("-> "))

                conta_infantil_atual = Sessao.criar_conta(numero_conta, saldo, tipo_da_conta)
                conta_infantil_atual.salvar_no_csv()
                usuario_infantil_atual.contas = numero_conta
                verificacao_conta = True
                
        elif option == '04':
            if verificacao_usuario_infantil == False:
                print("Crie usuário infantil primeiro para poder criar uma conta infantil!")
            else:
                print("Informe:")    

                print("NÚMERO DA CONTA:")
                numero_conta = int(input("-> "))   

                print("SALDO:")
                saldo = float(input("-> "))

                print("TIPO DA CONTA:")
                tipo_da_conta = int(input("-> "))

                Sessao.criar_conta_infantil(numero_conta, saldo, tipo_da_conta)
                verificacao_conta_infantil = True

        else:
            print('Opção inválida. Tente novamente.')

        if verificacao_conta == True:
            print("SELECIONE:")
            print("01 -> Transfêrencia.")
            print("02 -> Saldo.")
            print("03 -> Cartões.")
            print("04 -> Excluir cartão.")

            if option == '01':

                

        elif verificacao_conta_infantil == True:
            print("SELECIONE:")
            print("01 -> Transferência")
            print("02 -> Saldo.")
            print("03 -> Cartões.")
            print("04 -> Excluir cartão.")

            option = input("-> ")

if __name__ == '__main__':    
    main()