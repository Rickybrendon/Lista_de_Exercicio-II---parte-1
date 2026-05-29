from central_notificacoes import CentralNotificacoes
from notificador_email import NotificadorEmail
from notificador_sms import NotificadorSMS
from notificador_app import NotificadorApp

# criar a central
central = CentralNotificacoes()

# criar notificadores
email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

# adicionar notificadores à central
central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

# enviar mensagem para todos
central.enviar_para_todos("Sistema em manutenção às 22h.")
