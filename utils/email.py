import win32com.client as win32
from pathlib import Path


class Email:
    def __init__(self, destinatario, assunto, mensagem, anexo=None):
        self.destinatario = destinatario
        self.assunto = assunto
        self.mensagem = mensagem
        self.anexo = anexo


    def enviar_email(self):
        outlook = win32.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)

        mail.To = self.destinatario
        mail.Subject = self.assunto
        mail.Body = self.mensagem

        # anexar arquivo se existir
        if self.anexo:
            mail.Attachments.Add(str(Path(self.anexo).resolve()))

        mail.Send()  # envia diretamente
        # mail.Display()  # abre o email antes de enviar (opcional)