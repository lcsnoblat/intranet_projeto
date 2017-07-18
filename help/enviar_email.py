from django.core.mail import send_mail


class EnviarEmail:
    
    def __init__(self, assunto, corpo, de_quem, para):
        self.assunto = assunto
        self.corpo = corpo
        self.de_quem = de_quem
        self.para = para
        self.enviar()

    def enviar(self):
        send_mail(self.assunto, self.corpo, self.de_quem, self.para, fail_silently=False)