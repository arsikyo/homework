pirce_cofee=120
price_tea=80
price_juice=100
price_water=50
price_lemonade=90


print("┌──────────────────────────────────────────┐")
print("│          ☕ МЕНЮ НАШЕГО КАФЕ ☕          │")
print("├──────────────────────────────────────────┤")
print(f"│ 1. Кофе  ☕  - {pirce_cofee} руб.                  │")
print(f"│ 2. Чай   🍵  - {price_tea} руб.                   │")
print(f"│ 3. Сок   🧃  - {price_juice} руб.                  │")
print(f"│ 4. Вода  💧  - {price_water} руб.                   │")
print(f"│ 5. Лимонад🥤 - {price_lemonade} руб.                   │")
print("└──────────────────────────────────────────┘")

user_input = input('Выберите напиток(номер), количество порций и введите промокод(при наличии) через пробел: ')
parts = list(map(str.strip, user_input.split()))

match parts:
    case [choise_str, count_str, promocode]:
        promocode = promocode.upper()
    case [choise_str, count_str]:
        promocode = ""
    case _:
        print("\n❌ Ошибка: Неверный формат ввода! Введите данные через пробел.")
        exit()
choice=int(choise_str)
count=int(count_str)

if count<=0:
    print('\n❌ Количество порций не может быть равно нулю')
    exit()
match choice:
    case 1:
        item_name = 'Кофе'
        emoji = '☕'
        price = pirce_cofee
    case 2:
        item_name = 'Чай'
        emoji = '🍵'
        price = price_tea
    case 3:
        item_name = 'Сок'
        emoji = '🧃'
        price = price_juice
    case 4:
        item_name = 'Вода'
        emoji = '💧'
        price = price_water
    case 5:
        item_name = 'Лимонад'
        emoji = '🥤'
        price = price_lemonade
    case _:
        print('\n❌ Ошибка: Такого напитка нет в меню!')

total=price*count
discount=0

if promocode == 'STUDENT':
    discount=total*0.2

final_total=total-discount

if count % 10 == 1 and count % 100 != 11:
    portion = "порция"
elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
    portion = "порции"
else:
    portion = "порций"

print("\n╔══════════════════════════════════════════╗")
print(f"║             {emoji} КВИТАНЦИЯ КАФЕ {emoji}          ║")
print("╚══════════════════════════════════════════╝")
print(f" Товар: {item_name} {emoji}")
print(f" Цена за порцию: {price} руб")
print(f" Количество: {count} {portion}")
print(f" Сумма: {total} руб")

if discount > 0:
    print(f'\n Скидка "STUDENT" (20%): -{discount} руб')

print("════════════════════════════════════════════")
print(f" 💰 К ОПЛАТЕ: {final_total} руб")
print("════════════════════════════════════════════\n") 