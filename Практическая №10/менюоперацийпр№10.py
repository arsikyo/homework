balance=1000

while True:
    try:
        a=int(input(f'1. Узнать баланс\n2. Снять 100 руб.\n3. Положить 100 руб\n4. Выход\n\n'))
    except ValueError:
        print('\nНеверная команда\n')
        continue
    match a:
            
        case 1:
            print(f'\nВаш текущий баланс: {balance}\n')
            
        case 2:
                
            if balance>=100:
                balance-=100
                print(f'\nВы успешно сняли 100 руб.\n')
                
            else:
                print(f'\nНедостаточно средств на балансе\n')
            
        case 3:
            balance+=100
            
        case 4:
            print(f'\nДо свидания, ваш любимый банк!')
            break
            
        case _:
            print(f'\nНеверная команда\n')