try:
    pocket = int(input("Введите номер кармана (0-36): "))
    
    if not (0 <= pocket <= 36):
        print("ошибка ввода")
    elif pocket == 0:
        print("зеленый")
    else:
        if 1 <= pocket <= 10:
            color = "красный" if pocket % 2 != 0 else "черный"
        elif 11 <= pocket <= 18:
            color = "черный" if pocket % 2 != 0 else "красный"
        elif 19 <= pocket <= 28:
            color = "красный" if pocket % 2 != 0 else "черный"
        elif 29 <= pocket <= 36:
            color = "черный" if pocket % 2 != 0 else "красный"
            
        print(f"{color}")

except ValueError:
    print("ошибка ввода")