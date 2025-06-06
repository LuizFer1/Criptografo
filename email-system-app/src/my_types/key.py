from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())  # Salve esse valor e use sempre o mesmo!