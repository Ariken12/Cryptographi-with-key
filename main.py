import functions as func
import os

def encrypt(input_file, key=''):
    output_file = input_file + '.cry'
    input_file = open(input_file, 'rb')
    output_file = open(output_file, 'wb')
    for line in input_file:
        output_file.write(func.encrypt_line(line, key))
    input_file.close()
    output_file.close()


def decrypt(input_file, key=''):
    output_file = input_file[:-4:]
    input_file = open(input_file, 'rb')
    output_file = open(output_file, 'wb')
    for line in input_file:
        output_file.write(func.decrypt_line(line, key))
    input_file.close()
    output_file.close()


def main():
    file = 'try_to_crypto/test.txt'
    key = '84321'
    encrypt(file, key)
    decrypt(file+'.cry', key)


if __name__ == '__main__':
    main()
