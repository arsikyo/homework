# Продвинутый ввод в одну строку через map/split
weight, height = map(float, input("Введите вес (кг) и рост (м) через пробел: ").split())

bmi = weight / (height * height)

print(f"Ваш Индекс Массы Тела (ИМТ) составляет: {bmi:.1f}")
