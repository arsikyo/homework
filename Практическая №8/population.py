initial_organisms_count = float(input("Введите стартовое количество организмов: "))
daily_growth_percentage = float(input("Введите среднесуточное увеличение (в %): "))
total_simulation_days = int(input("Введите количество дней для размножения: "))

current_population_size = initial_organisms_count

print("\n--- Прогноз популяции по дням ---")
for current_day in range(1, total_simulation_days + 1):
    if current_day > 1:
        current_population_size += current_population_size * (daily_growth_percentage / 100)
    
    print(f"День {current_day}: размер популяции составляет {current_population_size:.2f}")
