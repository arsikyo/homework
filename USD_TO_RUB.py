USD_TO_RUB = 95.50


def convert_usd_to_rub(amount_usd: float) -> float:
    """Конвертирует сумму из долларов США (USD) в российские рубли (RUB).

    Args:
        amount_usd (float): Сумма в долларах.

    Returns:
        float: Рассчитанная сумма в рублях по текущему курсу.
    """
    return amount_usd * USD_TO_RUB


def main():
    usd_amount = float(input("Введите сумму в долларах (USD): "))
    
    rub_amount = convert_usd_to_rub(usd_amount)
    
    print(f"Сумма в рублях: {rub_amount:,.2f} руб.".replace(",", " "))


if __name__ == "__main__":
    main()
