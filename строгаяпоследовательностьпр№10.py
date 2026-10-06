a=int(input(f'Введите первое число последовательности: '))
bp=False

while True:
    if bp==False:
        b=int(input(f'\nВведите второе число последовательности: '))

    if a>=b:
        print(f'\nОшибка. Введено некорректное число')
        continue
    
    else:
        bp=True
        c=int(input(f'\nВведите третье число последовательности: '))

        if b>=c:
            print(f'\nОшибка. Введено некорректное число')
            continue
        else:
            print(f'\nПоследовательность принята')
            break