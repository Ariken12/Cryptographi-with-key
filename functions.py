def encrypt_line(line, key=None):
    b = bytearray(len(line))
    for i in range(len(line)):
        b[i] = encrypt_char(line[i], int(key[i % len(key)]))
    return b


def decrypt_line(line, key=None):
    b = bytearray(len(line))
    for i in range(len(line)):
        b[i] = decrypt_char(line[i], int(key[i % len(key)]))
    return b


def encrypt_char(a, b=0):
    x = (((a << b) | (a >> (8 - b))) % 256) if a != 0 else 0
    return x


def decrypt_char(a, b=0):
    x = (((a >> b) | (a << (8 - b))) % 256) if a != 0 else 0
    return x
