import math

num = int(input())
thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
units = num % 10

print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции десятков равна {tens}")
print(f"Цифра в позиции единиц равна {units}")