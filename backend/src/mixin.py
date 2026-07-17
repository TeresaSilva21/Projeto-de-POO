from datetime import datetime

class AuditoriaMixin:
    def log(self, mensagem: str):
        print(f"[{datetime.now()}] {self.__class__.__name__}: {mensagem}")