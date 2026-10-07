import random

secret_number = random.randint(1, 10)
is_guessed = False

for attempt in range(3):
    user_guess = int(input('Введите число: '))
    
    if user_guess == secret_number:
        print('Угадали!')
        is_guessed = True
        break
    else:
        print('Неверно')
        if user_guess < secret_number:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')

if not is_guessed:
    print(f'Попытки закончились. Было загадано число: {secret_number}')
