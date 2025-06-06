import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email
import os

class EmailClient:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 465


    def send_email(self, recipient, subject, message):
        try:
            encrypted_message = '[ENCRYPTED]' + self.encrypt_message(message)
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(encrypted_message, 'plain'))  # Envia mensagem criptografada

            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient, msg.as_string())
            print(f"E-mail enviado para {recipient} com assunto '{subject}'")
        except Exception as e:
            print(f"Falha ao enviar e-mail: {e}")

    def receive_email(self):
        emails = []
        try:
            imap_server = "imap.gmail.com"
            mail = imaplib.IMAP4_SSL(imap_server)
            mail.login(self.username, self.password)
            mail.select("inbox")

            status, messages = mail.search(None, "ALL")
            if status == "OK":
                for num in messages[0].split()[-5:]:  # Busca os 5 e-mails mais recentes
                    status, data = mail.fetch(num, "(RFC822)")
                    if status == "OK":
                        msg = email.message_from_bytes(data[0][1])
                        subject = msg["subject"]
                        from_ = msg["from"]
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    charset = part.get_content_charset() or "utf-8"
                                    body = part.get_payload(decode=True).decode(charset, errors="replace")
                                    if body.startswith('[ENCRYPTED]'):
                                        try:
                                            decrypted_body = self.decrypt_message(body[len('[ENCRYPTED]'):])
                                        except Exception:
                                            decrypted_body = body
                                    else:
                                        decrypted_body = body
                                    emails.append({
                                        "from": from_,
                                        "subject": subject,
                                        "body": decrypted_body
                                    })
                                    break
                else:
                    charset = msg.get_content_charset() or "utf-8"
                    body = msg.get_payload(decode=True).decode(charset, errors="replace")
                    if body.startswith('[ENCRYPTED]'):
                        try:
                            decrypted_body = self.decrypt_message(body[len('[ENCRYPTED]'):])
                        except Exception:
                            decrypted_body = body
                    else:
                        decrypted_body = body
                    emails.append({
                        "from": from_,
                        "subject": subject,
                        "body": decrypted_body
                    })
            mail.logout()
        except Exception as e:
            print(f"Falha ao receber e-mails: {e}")
        return emails


    def encrypt_message(self, message, key=b'bt9w_TOJD5_bb0DyNt4oNIqsPzFqtDZXwCJRqhbriWI='):
        from encryption import encrypt_message
        return encrypt_message(message, key)

    def decrypt_message(self, encrypted_message, key=b'bt9w_TOJD5_bb0DyNt4oNIqsPzFqtDZXwCJRqhbriWI='):
        from encryption import decrypt_message
        return decrypt_message(encrypted_message, key)