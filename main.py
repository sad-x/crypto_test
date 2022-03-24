"""main module"""
import db_module
import crypto_module
import file_module
import ui_module
from os import urandom


if __name__ == '__main__':
    mode = ui_module.get_mode()
    input_file_path = ui_module.get_input_file_path()
    output_file_path = ui_module.get_output_file_path(mode)

    if mode == "encrypt":
        # input_file_path = 'C:/Users/alex/Desktop/input_file_for_crypto.txt'
        # output_file_path = 'C:/Users/alex/Desktop/encrypted_file_for_crypto.txt'
        original_message = file_module.get_message_from_file(input_file_path)
        con = db_module.connect_to_db("CryptoTest", "postgres")
        keyVectorPair = db_module.get_vector_key_pair(con)
        key = keyVectorPair['CryptoKey']
        iv = keyVectorPair['InitVector']
        encrypted_message = crypto_module.encrypt(bytes(key, 'utf8'), bytes(iv, 'utf8'), original_message)
        file_module.write_bytes_message_to_file(output_file_path, encrypted_message)
        print("Your encrypted message:")
        print(encrypted_message)
    else:
        # input_file_path = 'C:/Users/alex/Desktop/encrypted_file_for_crypto.txt'
        # output_file_path = 'C:/Users/alex/Desktop/output_file_for_crypto.txt'
        encrypted_message = file_module.get_bytes_message_from_file(input_file_path)
        con = db_module.connect_to_db("CryptoTest", "postgres")
        keyVectorPair = db_module.get_vector_key_pair(con)
        key = keyVectorPair['CryptoKey']
        iv = keyVectorPair['InitVector']
        bytes_decrypted_message = crypto_module.decrypt(bytes(key, 'utf8'), bytes(iv, 'utf8'), encrypted_message)
        decrypted_message = bytes_decrypted_message.decode('utf8')
        file_module.write_message_to_file(output_file_path, decrypted_message)
        print("Your decrypted message:\n" + decrypted_message)

    # myKey = str(urandom(32))[2:-2]
    # myV = str(urandom(16))[2:-2]
    # db_module.insert_record_to_crypto_table(con, myKey, myV)
