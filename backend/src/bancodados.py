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
            self.__conn.commit()
            return True

    def excluir_usuario(self, usuario: Usuario) -> bool:
        try:
            self.__cursor.execute("""
                DELETE FROM Usuarios WHERE id = %s
            """, (usuario.id,)
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
                (id,)
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

    def criar_conta(self, usuario: Usuario) -> bool:
        try:
            self.__cursor.execute(""" 
                INSERT INTO conta (numero,saldo,tipo,cartoes,caixinhas,dividas) VALUES(%s,%s,%s,%s,%s,%s)""",
                    (
                    usuario.contas.numero,
                    usuario.contas.saldo,
                    usuario.contas.tipo,
                    usuario.contas.cartoes,
                    usuario.contas.caixinhas, 
                    usuario.contas.dividas,
                    ),
                    
                """
                UPDATE Usuarios SET contas = ARRAY_APPEND(contas, %s) WHERE numero = %s""",
                (

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
                (conta.saldo, conta.numero)
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
        try:    
            self.__cursor.execute(""" 
                INSERT INTO divida (id,valor,vencimento) VALUES(%s,%s,%s)""",
                    (   
                    divida.id,
                    divida.valor,
                    divida.data_vencimento
                ),
            )
            
            self.__cursor.execute(""" 
                INSERT INTO (id, numero_da_conta, divida) VALUES(%s,%s,%s)""",
                    (   
                    usuario_destinatario.id,
                    divida.valor,
                    divida.data_vencimento
                ),
            )
        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True
    def pagar_divida(self, divida: Divida) -> bool:
        try:
            self.__cursor.execute(
                """
                DELETE FROM conta WHERE id = %s
                """,
                (divida.id,)
            )

        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True

    def obter_dividas(self, usuario_destinatario: Usuario) -> list[Divida]:
        try:
            self.__cursor.execute(
            """
            SELECT * FROM Usuarios WHERE id = %s
                """,
                (id,)
            )

            dividas_dados = self.__cursor.fetchone()

            if dividas_dados is None:
                return None

            return Usuario(
                dividas_dados[1],
                dividas_dados[2],
                dividas_dados[3],
            )
            
        except Exception:
            self.__conn.rollback()
            return False

        finally:
            self.__conn.commit()
            return True

    def criar_cartao(self, usuario: Usuario, cartao: Cartao) -> bool:
        try:
            self.__cursor.execute(""" 
                INSERT INTO cartao (tipo, nome, numero, cvv, vencimento, limite_usado, limite_total, bloqueado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (
                        cartao.tipo,
                        cartao.nome,
                        cartao.numero,
                        cartao.cvv,
                        cartao.vencimento,
                        cartao.limite_usado,
                        cartao.limite_total,
                        cartao.bloqueado
                    )    
                )

        except Exception:
            self.__conn.rollback()
            return False
        finally:
            self.__conn.commit()
            return True

    def bloquear_cartao(self, cartao: Cartao) -> bool:
        try:
            self.__cursor.execute(
                """
                UPDATE cartao SET bloqueado = %s WHERE numero = %s
                """,
                (cartao.limite_total, cartao.numero)
            )

        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True

    def alterar_limite_cartao(self, cartao: Cartao) -> bool:
        try:
            self.__cursor.execute(
                """
                UPDATE cartao SET limite_total = %s WHERE numero = %s
                """,
                (True, cartao.numero)
            )

        except Exception:
            self.__conn.rollback()
            return False
            
        finally:
            self.__conn.commit()
            return True

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