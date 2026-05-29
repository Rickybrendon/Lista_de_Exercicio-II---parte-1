from notificador import Notificador

class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        print(f"[App] Enviando notificação no app: {mensagem}")
