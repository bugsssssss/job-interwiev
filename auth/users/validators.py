import random
import string
import re


# генерирую рандомный код с буквами и цифрами
def generate_random_code(length):
    characters = string.ascii_letters + string.digits  # Combine letters and digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code


def validate_phone_number(phone_number):
    # Нет ли букв
    cleaned_number = re.sub(r'[-\s]', '', phone_number)

    # Check if the cleaned input contains at least one letter
    if any(c.isalpha() for c in cleaned_number):
        return False

    # Я писал проврерку для узб номеров, при желании можно убрать
    if phone_number.startswith('998'):
        return True
    else:
        print('Вы вводите номер другой страны')
        return False

# Тесты
# input_number = "998 90-123-45-67"
# print(validate_phone_number(input_number))

# input_number = "998 90-123-45-6sss"
# print(validate_phone_number(input_number))

# input_number = "7 90-123-45-67"
# print(validate_phone_number(input_number))


# валидатор кода (можно улучшить проверку в зависимости от нужды)
def code_validartor(code):
    if len(code) != 4:
        return False

    return True

# валидатор инвайт (можно также улучшить проверку в зависимости от нужды)
def invite_code_validator(invite_code):
    if len(invite_code) != 6:
        return False

    return True
