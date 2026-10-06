summ=0
discount=10

while True:
    a=int(input(f'Введите цену товара: \n'))
    
    if a<0:
        print(f'Ошибка цены. Некорректное значение')
        continue
    
    elif a==0:
        
        if summ>1000:
            totalsumm=summ-(1-discount/100)
            print(f'Сумма чека со скидкой 10%: {totalsumm}')
            break
        
        else:
            print(f'Сумма чека: {summ}')
            break
    
    else:
        summ+=a