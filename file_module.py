"""module for file operations"""


def get_message_from_file(path):
    """Gets string from file by filepath"""
    f = open(path, 'r')
    message = f.read()
    f.close()
    return message


def get_bytes_message_from_file(path):
    """Gets bytes sequence from file by filepath"""
    f = open(path, 'rb')
    message = f.read()
    f.close()
    return message


def write_bytes_message_to_file(path, message):
    """Writes bytes sequence to file by filepath"""
    f = open(path, 'wb')
    f.write(message)
    f.close()
    return True


def write_message_to_file(path, message):
    """Writes string to file by filepath"""
    f = open(path, 'w')
    f.write(message)
    f.close()
    return True
