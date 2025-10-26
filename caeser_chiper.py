from itertools import repeat
from typing import Any

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabet))
print('Welcome to Caeser Cipher')
input_value = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n >>>  ')
message = ''
shift_number = 0


def caeser_encrypt(msg, alph, shift_num):
    """

    :param msg:
    :param alph:
    :param shift_num:
    """
    msg_characters = list(msg)

    for i in range(26):
        for j in range(len(msg_characters)):
            if alph[i] == msg_characters[j]:
                s_num = shift_num % len(msg_characters)
                msg_characters[j] = alph[i - s_num]
    # encrypt Message

    msg = ''.join(msg_characters)
    return msg


def caeser_decrypt(msg, alph, shift_num):
    """
import param
    :param msg:
    :param alph:
    :param shift_num:
    """
    msg_characters = list(msg)

    for i in range(26):
        for j in range(len(msg_characters)):
            if alph[i] == msg_characters[j]:
                s_num = shift_num % len(msg_characters)
                if s_num == 0:
                    msg_characters[j] = alph[i + 1]
                else:
                    msg_characters[j] = alph[i - s_num]
    # encrypt Message

    msg = ''.join(msg_characters)
    return msg


while True:
    if input_value.strip() == '' or input_value.lower().strip() != 'encode' or input_value.lower().strip() != 'decode':
        while input_value.strip() != 'encode' or input_value.strip() != 'decode':
            if input_value.strip() == 'encode' or input_value.strip() == 'decode':
                break
            else:
                input_value = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n >>>  ')
    if message.strip() == '':
        while message.strip() == '':
            message = input('Type your message:\n >>> ')
            if message.strip() != '':
                break
    if shift_number == 0:
        try:
            shift_number = int(input('Type the shift number:\n >>> '))
            if shift_number < 0 or shift_number > 26:
                print('Try Again.')
                continue
        except ValueError:
            print('Invalid input. Please try again.')
    if input_value.strip() == 'encode':
        print(f'>>> Your encode message is : {caeser_encrypt(message, alphabet, shift_number)}')
        break
    if input_value.strip() == 'decode':
        print(f'>>> Your decode message is : {caeser_decrypt(message, alphabet, shift_number)}')
        break
    else:
        break
