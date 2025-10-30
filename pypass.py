import random
import subprocess, sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to PyPassword Generator!')
input('   Press ENTER to continue...')
num_letters = int(input('::.How many letters do you want to be in your password?:\n>> '))
num_symbols = int(input('::.How many symbols do you want?:\n>> '))
num_numbers = int(input('::.How many numbers do you want?:\n>> '))
p = subprocess.Popen(['clip'], stdin=subprocess.PIPE, text=True)
if (num_letters + num_symbols + num_numbers) < 8:
    print('⛔Sorry, you have to add at least 8 Characters.')
else:

    first_password = []
    for i in range(num_letters):
        first_password.append(random.choice(letters))
    for i in range(num_symbols):
        first_password.append(random.choice(symbols))
    for i in range(num_numbers):
        first_password.append(random.choice(numbers))
    primary_password = ''
    random.shuffle(first_password)

    for i in range(first_password.__len__()):
        primary_password += first_password[i]
    p.communicate(primary_password)
    print(
        f'Your password is been generated...✅\n primary password: {primary_password}\n >>> Is been copy to ClipBoard!...')

    input('if you want, you can save you username & password here Press Enter...')
    username = input('>>> Your Username: ')
    websiteUrl = input('>>> Enter WebsiteUrl with dot[]: ')
    with open("demofile.txt", "a") as f:
        f.write(f'website: https://www.{websiteUrl}/\n Username: {username}\n Password: {primary_password}\n')

    print('Your username & password have been saved...')
    input('Press Enter...')
