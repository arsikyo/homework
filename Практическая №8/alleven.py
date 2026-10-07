print("Введите последовательность из 10 целых чисел (каждое с новой строки):")
are_all_numbers_even = True

for i in range(1, 11):
    current_number = int(input(f"Число №{i}: "))
    if current_number % 2 != 0:
        are_all_numbers_even = False

if are_all_numbers_even:
    print("Результат проверки: YES (все введённые числа чётные)")
else:
    print("Результат проверки: NO (среди чисел есть нечётные)")
