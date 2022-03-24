"""cryptography module to encrypt and decrypt text"""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt(key, iv, message):
    """Encrypts message using key and initializing vector"""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    result = b''
    for mes in split_message_by16(message):
        result += encryptor.update(bytes(mes, 'utf8'))
    encryptor.finalize()
    return result


def decrypt(key, iv, message):
    """Decrypts message using key and initializing vector"""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    result_str = decryptor.update(message) + decryptor.finalize()
    return result_str


def split_message_by16(mes):
    """Splits string by parts 16 symbols length each"""
    arr = []
    for i in range(len(mes) // 16 + 1):
        cur_message = mes[i*16:(i+1)*16]
        if len(cur_message) < 16:
            cur_message += " "*(16 - len(cur_message))
        arr.append(cur_message)
    return arr
