print("=== Сравнение цвета шахматных клеток ===")

try:
    col1 = int(input("Столбец 1-й клетки: "))
    row1 = int(input("Строка 1-й клетки: "))
    col2 = int(input("Столбец 2-й клетки: "))
    row2 = int(input("Строка 2-й клетки: "))

    if not (1 <= col1 <= 8 and 1 <= row1 <= 8 and 1 <= col2 <= 8 and 1 <= row2 <= 8):
        print("Ошибка: координаты должны быть в диапазоне от 1 до 8.")
    else:
        if (col1 + row1) % 2 == (col2 + row2) % 2:
            print("YES")
        else:
            print("NO")

except ValueError:
    print("Ошибка: вводите только целые числа.")