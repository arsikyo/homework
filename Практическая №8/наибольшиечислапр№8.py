n = int(input(f'Введите количество чисел используемое в программе: '))

num1 = int(input(f'Введите число: '))
num2 = int(input(f'Введите число: '))

if num1 > num2:
    max_num = num1
    second_max = num2
else:
    max_num = num2
    second_max = num1

for _ in range(n - 2):
    current_num = int(input(f'Введите число: '))
    if current_num > max_num:
        second_max = max_num
        max_num = current_num
    elif current_num > second_max:
        second_max = current_num

print(f'Наибольшее число: {max_num}')
print(f'Второе по величине число: {second_max}')
