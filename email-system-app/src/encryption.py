from cryptography.fernet import Fernet

KEY = b'bt9w_TOJD5_bb0DyNt4oNIqsPzFqtDZXwCJRqhbriWI='  # Use a chave gerada pelo Fernet.generate_key()

def encrypt_message(message, key=KEY):
    f = Fernet(key)
    token = f.encrypt(message.encode('utf-8'))
    return token.decode('utf-8')

def decrypt_message(encrypted_message, key=KEY):
    f = Fernet(key)
    token = encrypted_message.encode('utf-8')
    decrypted = f.decrypt(token)
    return decrypted.decode('utf-8')
