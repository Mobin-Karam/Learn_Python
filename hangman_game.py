import random
words = ["teacher", 'entertainment', 'death', 'person', 'ad', 'baseball', 'argument', 'atmosphere', 'charity',
         'payment', 'member', 'two', 'device', 'distribution', 'procedure']
random_word = random.choice(words)
characters = list(random_word)
word_length = len(characters)
print(' ---> Welcome to Hangman Game!. <---')
input('  ..::Press ENTER to continue...')
user_name = input('Enter your name:\n >>> ')

word_name_underscore = []
word_string = ''
hangman_lives = 6

for i in range(word_length):
    word_name_underscore.append('_')
    word_string += word_name_underscore[i]

# print(characters)
if hangman_lives != 0:
    while word_string != random_word:
        gl = input(f'Enter the game letter: >>> {word_string}\n ')
        if all(characters[index] != gl for index in range(word_length)) and hangman_lives > 0:
            hangman_lives -= 1
            print(f'Hangman Lives: ----------: {hangman_lives} :-----------\n ')
            print('It\'s not a game letter, try again.⛔')

        else:
            for index in range(word_length):
                if characters[index] == gl:
                    word_string = word_string[:index] + gl + word_string[index + 1:]
                    print('Got it let\'s go ...✅')
                    print(f'Hangman Lives: ----------: {hangman_lives} :-----------\n ')
        if word_string == random_word:
            print(f'You won! {user_name} :-)')
            break
        elif hangman_lives <= 0:
            print(f'You lost! {user_name} :-)')
            break
else:
    print(f'Game Over')
