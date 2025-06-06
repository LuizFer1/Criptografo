import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog, ttk
from email_client import EmailClient
import os
import sys

class EmailApp:
    def __init__(self):
        try:
            self.root = tk.Tk()
            self.root.title("Sistema de E-mail Criptografado")
            self.root.geometry("800x600")
            self.root.configure(bg="#4169E1")
            
            # Configurar protocolo de fechamento
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            self.email_client = None
            self.encryption_key = None
            
            # Inicializar variáveis de entrada
            self.email_entry = None
            self.password_entry = None
            self.key_entry = None
            self.destinatario_entry = None
            self.assunto_entry = None
            self.mensagem_text = None
            self.emails_text = None
            
            # Iniciar com tela de login
            self.show_login_screen()
            
        except Exception as e:
            print(f"Erro na inicialização: {e}")
            sys.exit(1)
    
    def on_closing(self):
        """Função para fechar a aplicação de forma segura"""
        try:
            self.root.quit()
            self.root.destroy()
        except:
            pass
        sys.exit(0)
    
    def clear_screen(self):
        """Limpa a tela de forma segura"""
        try:
            for widget in self.root.winfo_children():
                widget.destroy()
        except Exception as e:
            print(f"Erro ao limpar tela: {e}")
    
    def show_login_screen(self):
        self.clear_screen()
        
        try:
            # Frame principal
            main_frame = tk.Frame(self.root, bg="#4169E1")
            main_frame.pack(expand=True)
            
            # Ícone de cadeado (usando texto simples para evitar problemas)
            icon_frame = tk.Frame(main_frame, bg="#4169E1")
            icon_frame.pack(pady=50)
            
            lock_label = tk.Label(icon_frame, text="LOCK", font=('Arial', 30, 'bold'), 
                                 bg="#4169E1", fg="white")
            lock_label.pack()
            
            # Campos de login
            tk.Label(main_frame, text="EMAIL", font=('Arial', 12, 'bold'), 
                    bg="#4169E1", fg="white").pack(pady=(20, 5))
            self.email_entry = tk.Entry(main_frame, width=30, font=('Arial', 12))
            self.email_entry.pack(pady=5)
            
            tk.Label(main_frame, text="SENHA", font=('Arial', 12, 'bold'), 
                    bg="#4169E1", fg="white").pack(pady=(20, 5))
            self.password_entry = tk.Entry(main_frame, width=30, font=('Arial', 12), show="*")
            self.password_entry.pack(pady=5)
            
            # Botão Login
            login_btn = tk.Button(main_frame, text="LOGAR", font=('Arial', 12, 'bold'), 
                                 bg="white", fg="#4169E1", width=20, command=self.login)
            login_btn.pack(pady=30)
            
        except Exception as e:
            print(f"Erro na tela de login: {e}")
            messagebox.showerror("Erro", f"Erro na interface: {e}")
    
    def login(self):
        try:
            email = self.email_entry.get() if self.email_entry else ""
            password = self.password_entry.get() if self.password_entry else ""
            
            if not email or not password:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
            
            # Inicializar cliente de email
            self.email_client = EmailClient()
            self.email_client.username = email
            self.email_client.password = password
            
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.show_key_screen()
            
        except Exception as e:
            print(f"Erro no login: {e}")
            messagebox.showerror("Erro", f"Falha no login: {e}")
    
    def show_key_screen(self):
        self.clear_screen()
        
        try:
            # Frame principal
            main_frame = tk.Frame(self.root, bg="#4169E1")
            main_frame.pack(expand=True)
            
            # Título
            title_label = tk.Label(main_frame, text="CONFIGURAR CHAVE", 
                                  font=('Arial', 20, 'bold'), bg="#4169E1", fg="white")
            title_label.pack(pady=50)
            
            tk.Label(main_frame, text="CHAVE DE ENCRIPTAÇÃO", font=('Arial', 14, 'bold'), 
                    bg="#4169E1", fg="white").pack(pady=20)
            
            # Campo para chave
            self.key_entry = tk.Entry(main_frame, width=50, font=('Arial', 10))
            self.key_entry.pack(pady=10)
            
            # Botão adicionar chave
            add_key_btn = tk.Button(main_frame, text="ADICIONAR CHAVE", font=('Arial', 12, 'bold'), 
                                   bg="white", fg="#4169E1", width=20, command=self.add_key)
            add_key_btn.pack(pady=20)
            
            # Botão gerar chave
            gen_key_btn = tk.Button(main_frame, text="GERAR NOVA CHAVE", font=('Arial', 12, 'bold'), 
                                   bg="lightgray", fg="#4169E1", width=20, command=self.generate_key)
            gen_key_btn.pack(pady=10)
            
            # Texto informativo
            info_text = "Insira uma chave Fernet válida ou gere uma nova"
            tk.Label(main_frame, text=info_text, font=('Arial', 10), 
                    bg="#4169E1", fg="lightgray", wraplength=400).pack(pady=10)
            
        except Exception as e:
            print(f"Erro na tela de chave: {e}")
            messagebox.showerror("Erro", f"Erro na interface: {e}")
    
    def generate_key(self):
        try:
            from cryptography.fernet import Fernet
            new_key = Fernet.generate_key()
            
            if self.key_entry:
                self.key_entry.delete(0, tk.END)
                self.key_entry.insert(0, new_key.decode())
            
            messagebox.showinfo("Chave Gerada", "Nova chave gerada! Guarde com segurança.")
            
        except Exception as e:
            print(f"Erro ao gerar chave: {e}")
            messagebox.showerror("Erro", f"Erro ao gerar chave: {e}")
    
    def add_key(self):
        try:
            key_input = self.key_entry.get() if self.key_entry else ""
            
            if not key_input:
                messagebox.showerror("Erro", "Insira ou gere uma chave!")
                return
            
            # Validar chave
            from cryptography.fernet import Fernet
            Fernet(key_input.encode())
            self.encryption_key = key_input.encode()
            
            # Atualizar cliente de email
            if self.email_client:
                self.email_client.encryption_key = self.encryption_key
            
            messagebox.showinfo("Sucesso", "Chave configurada com sucesso!")
            self.show_main_screen()
            
        except Exception as e:
            print(f"Erro ao adicionar chave: {e}")
            messagebox.showerror("Erro", "Chave inválida!")
    
    def show_main_screen(self):
        self.clear_screen()
        
        try:
            # Frame principal com scrollbar se necessário
            main_frame = tk.Frame(self.root, bg="white")
            main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Título
            title_label = tk.Label(main_frame, text="Sistema de E-mail Criptografado", 
                                  font=('Arial', 16, 'bold'), bg="white")
            title_label.pack(pady=10)
            
            # Notebook para abas
            notebook = ttk.Notebook(main_frame)
            notebook.pack(fill=tk.BOTH, expand=True)
            
            # Aba Enviar
            send_frame = tk.Frame(notebook, bg="white")
            notebook.add(send_frame, text="Enviar E-mail")
            
            self.create_send_interface(send_frame)
            
            # Aba Receber
            receive_frame = tk.Frame(notebook, bg="white")
            notebook.add(receive_frame, text="E-mails Recebidos")
            
            self.create_receive_interface(receive_frame)
            
            # Botões de navegação
            nav_frame = tk.Frame(main_frame, bg="white")
            nav_frame.pack(fill=tk.X, pady=10)
            
            logout_btn = tk.Button(nav_frame, text="LOGOUT", font=('Arial', 10), 
                                  bg="#ff4444", fg="white", command=self.show_login_screen)
            logout_btn.pack(side=tk.LEFT)
            
            change_key_btn = tk.Button(nav_frame, text="ALTERAR CHAVE", font=('Arial', 10), 
                                      bg="#4169E1", fg="white", command=self.show_key_screen)
            change_key_btn.pack(side=tk.RIGHT)
            
        except Exception as e:
            print(f"Erro na tela principal: {e}")
            messagebox.showerror("Erro", f"Erro na interface: {e}")
    
    def create_send_interface(self, parent):
        tk.Label(parent, text="DESTINATÁRIO", font=('Arial', 10, 'bold')).pack(anchor="w", padx=10, pady=(10,0))
        self.destinatario_entry = tk.Entry(parent, width=50)
        self.destinatario_entry.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(parent, text="ASSUNTO", font=('Arial', 10, 'bold')).pack(anchor="w", padx=10, pady=(10,0))
        self.assunto_entry = tk.Entry(parent, width=50)
        self.assunto_entry.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(parent, text="MENSAGEM", font=('Arial', 10, 'bold')).pack(anchor="w", padx=10, pady=(10,0))
        self.mensagem_text = scrolledtext.ScrolledText(parent, width=50, height=15)
        self.mensagem_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        enviar_btn = tk.Button(parent, text="ENVIAR", font=('Arial', 12, 'bold'), 
                              bg="#4169E1", fg="white", command=self.enviar_email)
        enviar_btn.pack(pady=10)
    
    def create_receive_interface(self, parent):
        self.emails_text = scrolledtext.ScrolledText(parent, width=60, height=20)
        self.emails_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        receber_btn = tk.Button(parent, text="RECEBER EMAILS", font=('Arial', 12, 'bold'), 
                               bg="#4169E1", fg="white", command=self.receber_emails)
        receber_btn.pack(pady=10)
    
    def enviar_email(self):
        try:
            destinatario = self.destinatario_entry.get() if self.destinatario_entry else ""
            assunto = self.assunto_entry.get() if self.assunto_entry else ""
            mensagem = self.mensagem_text.get("1.0", tk.END) if self.mensagem_text else ""
            
            if not destinatario or not assunto or not mensagem.strip():
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
            
            if not self.email_client:
                messagebox.showerror("Erro", "Cliente de e-mail não configurado!")
                return
            
            self.email_client.send_email(destinatario, assunto, mensagem)
            messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
            
            # Limpar campos
            if self.destinatario_entry:
                self.destinatario_entry.delete(0, tk.END)
            if self.assunto_entry:
                self.assunto_entry.delete(0, tk.END)
            if self.mensagem_text:
                self.mensagem_text.delete("1.0", tk.END)
            
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            messagebox.showerror("Erro", f"Falha ao enviar e-mail: {e}")
    
    def receber_emails(self):
        try:
            if not self.email_client:
                messagebox.showerror("Erro", "Cliente de e-mail não configurado!")
                return
            
            emails = self.email_client.receive_email()
            
            if self.emails_text:
                self.emails_text.delete("1.0", tk.END)
                
                if not emails:
                    self.emails_text.insert(tk.END, "Nenhum e-mail encontrado.")
                    return
                
                for email_data in emails:
                    self.emails_text.insert(tk.END, f"De: {email_data.get('from', 'N/A')}\n")
                    self.emails_text.insert(tk.END, f"Assunto: {email_data.get('subject', 'N/A')}\n")
                    self.emails_text.insert(tk.END, f"Mensagem: {email_data.get('body', 'N/A')}\n")
                    self.emails_text.insert(tk.END, "-" * 50 + "\n\n")
                
        except Exception as e:
            print(f"Erro ao receber e-mails: {e}")
            messagebox.showerror("Erro", f"Falha ao receber e-mails: {e}")
    
    def run(self):
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Erro na execução: {e}")
        finally:
            self.on_closing()

def main():
    try:
        app = EmailApp()
        app.run()
    except Exception as e:
        print(f"Erro fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()