number = int(input('Введите число: '))
last_digit = number % 10

count_threes = 0
count_last_digit = 0
count_evens = 0
sum_greater_than_5 = 0
prod_greater_than_7 = 1
count_0_and_5 = 0
has_digit_greater_than_7 = False

while number > 0:
    digit = number % 10
    
    if digit == 3:
        count_threes += 1
    if digit == last_digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_evens += 1
    if digit > 5:
        sum_greater_than_5 += digit
    if digit > 7:
        prod_greater_than_7 *= digit
        has_digit_greater_than_7 = True
    if digit == 0 or digit == 5:
        count_0_and_5 += 1
        
    number //= 10

if not has_digit_greater_than_7:
    prod_greater_than_7 = 1

print(f'Количество цифр 3 в числе: {count_threes}')
print(f'Сколько раз в числе встречается его последняя цифра: {count_last_digit}')
print(f'Количество четных цифр: {count_evens}')
print(f'Сумма цифр числа, больших пяти: {sum_greater_than_5}')
print(f'Произведение цифр числа, больших семи: {prod_greater_than_7}')
print(f'Количество цифр 0 и 5 в числе(суммарно): {count_0_and_5}')
