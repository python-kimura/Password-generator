
from random import *

def generate_symbols_list(is_numbers=False, is_letters=False, is_specials=False):
    numbers = [chr(i) for i in range(48, 58)]

    letters = [chr(i) for i in range(65, 91)] + \
              [chr(i) for i in range(97, 123)]

    special = [chr(i) for i in range(33, 48)] + \
              [chr(i) for i in range(58, 65)] + \
              [chr(i) for i in range(91, 97)] + \
              [chr(i) for i in range(123, 127)]

    symbols = []
    if is_numbers:
        symbols.extend(numbers)
    if is_letters:
        symbols.extend(letters)
    if is_specials:
        symbols.extend(special)

    return symbols


def generate_password(length, is_numbers=False, is_letters=False, is_specials=False):
    symbols = generate_symbols_list(is_numbers, is_letters, is_specials)
    return ''.join(choice(symbols) for _ in range(length))


def request_number(message):
    while True:
        result = input(message)

        if result.isdigit():
            result = int(result)
            break
        else:
            print('Вы должны ввести число!')

    return result


print('Приветствую вас в генераторе паролей!')

length = request_number('Введите длину пароля: ')

is_numbers = input('Нужны ли цифры? [да/нет] ').lower() == 'да'
is_letters = input('Нужны ли буквы? [да/нет] ').lower() == 'да'
is_specials = input('Нужны ли специальные символы? [да/нет] ').lower() == 'да'

print('Ваш пароль готов!')
print(generate_password(length, is_numbers, is_letters, is_specials))