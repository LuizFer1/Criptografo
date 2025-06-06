import tkinter as tk
from tkinter import scrolledtext, messagebox
from email_client import EmailClient

def enviar_email():
    destinatario = entry_destinatario.get()
    assunto = entry_assunto.get()
    corpo = text_corpo.get("1.0", tk.END)
    try:
        email_client.send_email(destinatario, assunto, corpo)
        messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao enviar e-mail: {e}")

def receber_emails():
    emails = email_client.receive_email()
    text_recebidos.delete("1.0", tk.END)
    for email in emails:
        text_recebidos.insert(tk.END, f"De: {email['from']}\nAssunto: {email['subject']}\nMensagem: {email['body']}\n{'-'*40}\n")

email_client = EmailClient()

root = tk.Tk()
root.title("Sistema de E-mail Criptografado")

# Campos de envio
tk.Label(root, text="Destinatário:").grid(row=0, column=0, sticky="e")
entry_destinatario = tk.Entry(root, width=40)
entry_destinatario.grid(row=0, column=1)

tk.Label(root, text="Assunto:").grid(row=1, column=0, sticky="e")
entry_assunto = tk.Entry(root, width=40)
entry_assunto.grid(row=1, column=1)

tk.Label(root, text="Mensagem:").grid(row=2, column=0, sticky="ne")
text_corpo = scrolledtext.ScrolledText(root, width=40, height=5)
text_corpo.grid(row=2, column=1)

btn_enviar = tk.Button(root, text="Enviar E-mail", command=enviar_email)
btn_enviar.grid(row=3, column=1, sticky="e", pady=5)

# Área de recebimento
tk.Label(root, text="E-mails Recebidos:").grid(row=4, column=0, sticky="ne")
text_recebidos = scrolledtext.ScrolledText(root, width=60, height=15)
text_recebidos.grid(row=4, column=1)

btn_receber = tk.Button(root, text="Receber E-mails", command=receber_emails)
btn_receber.grid(row=5, column=1, sticky="e", pady=5)

root.mainloop()