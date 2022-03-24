"""cryptography module to encrypt and decrypt text"""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
from os import urandom
import os


def encrypt(key, iv, message):
    """returns encrypted message"""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    result = b''
    for mes in split_message_by16(message):
        result += encryptor.update(bytes(mes, 'utf8'))
    encryptor.finalize()

    return result


def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8], 2)) for i in range(len(s)//8))


def decrypt(key, iv, message):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    result_str = decryptor.update(message) + decryptor.finalize()
    return result_str


def split_message_by16(mes):
    arr = []
    for i in range(len(mes) // 16 + 1):
        curMessage = mes[i*16:(i+1)*16]
        if(len(curMessage) < 16):
            curMessage += " "*(16 - len(curMessage))
        arr.append(curMessage)
    return arr