def get_message_from_file(path):
    f = open(path, 'r')
    message = f.read()
    f.close()
    return message


def get_bytes_message_from_file(path):
    f = open(path, 'rb')
    message = f.read()
    f.close()
    return message


def write_bytes_message_to_file(path, message):
    f = open(path, 'wb')
    f.write(message)
    f.close()
    return True


def write_message_to_file(path, message):
    f = open(path, 'w')
    f.write(message)
    f.close()
    return True
