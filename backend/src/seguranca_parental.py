class SegurancaParental:
    def _init_(self, limite_saque_diario):
        self.limite_saque = limite_saque_diario

    def validar_transacao(self, valor):
        if valor > self.limite_saque:
            print(f"ALERTA: Transação bloqueada!")
            return False
        return True