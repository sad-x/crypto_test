"""user interface module"""
import os


def get_mode():
    """Gets mode from user"""
    mode = 'unknown'
    while mode == 'unknown':
        user_mode = input("Choose mode (1 - encryption, 2 - decryption)\n")
        if user_mode == '1':
            mode = 'encrypt'
            print('You have chosen encryption.')
        elif user_mode == '2':
            mode = 'decrypt'
            print('You have chosen decryption.')
    return mode


def get_output_file_path(mode):
    """Gets output filepath from user"""
    while 1 == 1:
        ofp = input("Enter the output directory\n")
        if not os.path.isdir(ofp):
            print("No such directory!")
        else:
            if mode == 'encrypt':
                return os.path.normpath(os.path.join(ofp + "/encrypted_file_for_crypto.txt")).replace('\\', '/')
            else:
                return os.path.normpath(os.path.join(ofp + "/output_file_for_crypto.txt")).replace('\\', '/')


def get_input_file_path():
    """Gets input filepath from user"""
    is_file_ok = False
    while not is_file_ok:
        file_path = input("Enter the input file path\n")
        try:
            open(file_path, 'r')
        except IOError:
            print("Wrong file path!")
            continue
        f = open(file_path, 'r')
        if f.read() == "":
            print("Empty file!")
        else:
            print("File path is correct.")
            return file_path
