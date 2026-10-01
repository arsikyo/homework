BANKNOTES = (5000, 2000, 1000, 500, 200, 100)

def main():
    amount = int(input("Введите сумму для снятия (кратную 100): "))
    
    if amount % 100 != 0:
        print("Ошибка: Сумма должна быть кратна 100!")
        return

    print(f"\nОтчет о выдаче наличных для суммы {amount} руб.:")
    
    remaining_amount = amount
    for note in BANKNOTES:
        count = remaining_amount // note
        if count > 0:
            print(f"Купюры номиналом {note} руб.: {count} шт.")
            remaining_amount %= note
            
if __name__ == "__main__":
    main()