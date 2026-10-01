print("=== Проверка хода слона ===")

try:
    col1 = int(input("Исходный столбец: "))
    row1 = int(input("Исходная строка: "))
    col2 = int(input("Целевой столбец: "))
    row2 = int(input("Целевая строка: "))

    if not (1 <= col1 <= 8 and 1 <= row1 <= 8 and 1 <= col2 <= 8 and 1 <= row2 <= 8):
        print("Ошибка: координаты вне шахматного поля.")
    elif col1 == col2 and row1 == row2:
        print("Ошибка: клетки должны быть различными.")
    else:
        if abs(col1 - col2) == abs(row1 - row2):
            print("YES")
        else:
            print("NO")

except ValueError:
    print("Ошибка: вводите только целые числа.")
