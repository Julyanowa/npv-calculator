from npv_calculator import NPVCalculator

if __name__ == "__main__":
    # Условия задачи
    initial_investment = 21500
    cash_flows = [13225, 13225, 15000, 18000]  # 4 периода
    discount_rate = 0.15

    # Расчёт
    calculator = NPVCalculator(initial_investment, cash_flows, discount_rate)
    npv = calculator.calculate_npv()

    print(f"NPV проекта: {npv:.2f} ден. ед.")

    if npv > 0:
        print("✅ Проект стоит принять, так как NPV > 0.")
    else:
        print("❌ Проект отклоняется, так как NPV < 0.")