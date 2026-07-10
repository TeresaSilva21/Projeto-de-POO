import psycopg

from conta import Conta
from sessao import Sessao
from cartao import Cartao
from divida import Divida
from usuario import Usuario
from caixinha import Caixinha
from dados import DadosInicial
from containfantil import ContaInfantil
from usuario_infantil import UsuarioInfantil

class BancoDeDados:
    def __init__(self):
        self.__conn = psycopg.connect("dbname=CardBank user=postgres")
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()

    def criar_usuario(self, usuario: Usuario) -> bool:
        try:
            self.__cursor.execute(""" 
                INSERT INTO usuarios(id,nome,cpf,renda,senha,criancas,contas_criancas,contas) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (   
                    usuario.id,
                    usuario.nome,
                    usuario.cpf,
                    usuario.renda,
                    usuario.senha,
                    usuario.criancas,
                    usuario.contas_criancas,
                    usuario.contas,
                ),
            )
            
        except Exception:
            self.__conn.rollback()
            return False
        
        finally:
            self.__conn.commit          
            return True

    def excluir_usuario(self, usuario: Usuario) -> bool:
        try:
            self.__cursor.execute("""
                DELETE FROM Usuarios WHERE id = %s
            """, (usuario.id)
            )

        except Exception:
            self.__conn.rollback()
            return False

        finally:
            self.__conn.commit()
            return True      

    def criar_usuario_infantil(
        self, usuario_responsavel: Usuario, senha_crianca: str
        ) -> bool:
        try:    
            self.__cursor.execute(""" 
                INSERT INTO UsuariosInfantil (id,nome,senha,contas) VALUES(%s,%s,%s,%s)""",
                    (   
                    UsuarioInfantil.id,
                    UsuarioInfantil.nome,
                    UsuarioInfantil.senha,
                    UsuarioInfantil.contas,
                )
            )
        except Exception:
            self.__conn.rollback()
            return False
        
        finally:
            self.__conn.commit()
            return True
            

    def excluir_usuario_infantil(
        self, usuario_responsavel: Usuario, usuario_infantil: UsuarioInfantil
    ) -> bool:
        try:
            self.__cursor.execute(
                """
                DELETE FROM UsuariosInfantil WHERE id = %s
                """,
                (usuario_infantil.id,),
            )

        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True

    def obter_usuario(self, id: int):
        try:
            self.__cursor.execute(
            """
            SELECT * FROM Usuarios WHERE id = %s
                """,
                (id)
            )

            usuario_dados = self.__cursor.fetchone()

            if usuario_dados is None:
                return None

            return Usuario(
                usuario_dados[1],
                usuario_dados[2],
                usuario_dados[3],
                usuario_dados[4],
            )
            
        except Exception:
            self.__conn.rollback()
            return False

        finally:
            self.__conn.commit()
            return True
            

    def criar_conta(self, usuario: Usuario, tipo: int) -> bool:
        try:
            self.__cursor.execute(""" 
                INSERT INTO UsuariosInfantil (numero,saldo,tipo,cartoes,caixinhas,dividas) VALUES(%s,%s,%s,%s,%s,%s)""",
                    (
                    Conta.numero,
                    Conta.saldo,
                    Conta.tipo,
                    Conta.cartoes,
                    Conta.caixinhas, 
                    Conta.dividas,
                    )
            )

        except Exception:
            self.__conn.rollback()
            return False

        finally:
            self.__conn.commit()
            return True 

    def excluir_conta(self, usuario: Usuario, conta: Conta) -> bool:
        try:
            self.__cursor.execute(
                """
                DELETE FROM conta WHERE numero = %s
                """,
                (usuario.contas.numero)
            )

        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True

    def alterar_saldo(self, usuario: Usuario, conta: Conta) -> bool:
        try:
            self.__cursor.execute(
                """
                UPDATE conta SET saldo = %s WHERE numero = %s
                """,
                (val,usuario.contas.numero)
            )

        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True

    def criar_divida(
        self, divida: Divida, usuario_remetente: Usuario, usuario_destinatario: Usuario
    ) -> bool:
        with psycopg.connect("dbname=CardBank user=postgres") as conn:
            with conn.cursor() as cur:
                self.__cursor.execute(""" 
                    INSERT INTO (id,nome,senha,contas) VALUES(%s,%s,%s,%s)""",
                        (   
                        UsuarioInfantil.id,
                        UsuarioInfantil.nome,
                        UsuarioInfantil.senha,
                        UsuarioInfantil.contas,
                    ),
                )
        return True

    def pagar_divida(self, divida: Divida) -> bool:
        pass

    def obter_dividas(self, usuario_destinatario: Usuario) -> list[Divida]:
        pass

    def criar_cartao(self, usuario: Usuario, cartao: Cartao) -> bool:
        try:
            self.__cursor.execute(""" 
                INSERT INTO UsuariosInfantil (tipo, nome, numero, cvv, vencimento, limite_usado) VALUES(%s,%s,%s,%s,%s,%s)""",
                    (
                        Cartao.tipo,
                        Cartao.nome,
                        Cartao.numero,
                        Cartao.cvv,
                        Cartao.vencimento,
                        Cartao.limite_usado
            )    

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

    def obter_cartoes(self, usuario: Usuario) -> list[Cartao]:
        pass

    def contas_infantis_responsavel(
        self, usuario_responsavel: Usuario
    ) -> list[ContaInfantil]:
        pass