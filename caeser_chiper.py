from itertools import repeat
from typing import Any

alphabet: list[str | Any] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
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
    final_msg = ''
    for i in range(26):
        for j in range(len(msg_characters)):
            if alph[i] == msg_characters[j]:
                s_num = shift_num % len(msg_characters)
                final_msg += msg_characters[j - s_num]
    # encrypt Message

    return final_msg


def caeser_decrypt(msg, alph, shift_num):
    """
import param
    :param msg:
    :param alph:
    :param shift_num:
    """
    msg_characters = list(msg)
    final_msg = ''
    for i in range(26):
        for j in range(len(msg_characters)):
            if alph[i] == msg_characters[j]:
                s_num = shift_num % len(msg_characters)
                final_msg += msg_characters[j - s_num]
    # Decrypt Message
    return final_msg


while True:
    if input_value.strip() == '' or input_value.lower().strip() != 'encode' or input_value.lower().strip() == 'decode':
        while input_value.strip() != 'encode' or input_value.strip() != 'decode':
            if input_value.strip() == 'encode' or input_value.strip() == 'decode':
                break
            else:
                input_value = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n >>>  ')
    elif message.strip() == '':
        while message.strip() == '':
            message = input('Type your message:\n >>> ')
            if message.strip() != '':
                break
    elif shift_number == 0:
        while True:
            try:
                shift_number = int(input('Type the shift number:\n >>> '))
                if shift_number < 0 or shift_number > 26:
                    print('Try Again.')
                    continue
                break
            except ValueError:
                print('Invalid input. Please try again.')
    elif input_value.strip() == 'encode':
        caeser_encrypt(input_value, alphabet, shift_number)
    elif input_value.strip() == 'decode':
        caeser_decrypt(input_value, alphabet, shift_number)
    elif caeser_encrypt(message, alphabet, shift_number).strip() == '' or caeser_decrypt(message, alphabet,
                                                                                         shift_number).strip() == '':
        print(caeser_encrypt(message, alphabet, shift_number), caeser_decrypt(message, alphabet, shift_number))
        input_continue_value = input(f'Do you want to continue (y/n): \n >>> ')
        try:
            if input_continue_value.lower().strip() == 'y':
                continue
            elif input_continue_value.lower().strip() == 'n':
                print('Thank you for playing.')
                break
        except ValueError:
            print('Invalid input. Please try again.')
