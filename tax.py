TAX_RATE = 0.13

income = float(input("Введите ваш годовой доход (руб.): "))
calculated_tax = income * TAX_RATE
after_tax_income = income - calculated_tax

print(f"\nОбщая сумма дохода: {income:,.2f} руб.".replace(",", " "))
print(f"Сумма рассчитанного налога: {calculated_tax:,.2f} руб.".replace(",", " "))
print(f"Сумма «на руки» после вычета налога: {after_tax_income:,.2f} руб.".replace(",", " "))
