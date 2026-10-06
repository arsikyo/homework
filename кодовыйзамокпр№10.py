while True:
    a=int(input(f'\nВведите пин-код: '))

    if a==4590:
        print(f'Доступ разрешен')
        break
    
    else:
        print(f'Ошибка. Попробуйте еще раз')