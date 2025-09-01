class NPVCalculator:
    def __init__(self, initial_investment, cash_flows, discount_rate):
        """
        Класс для расчёта NPV инвестиционного проекта.

        :param initial_investment: начальные инвестиции (положительное число)
        :param cash_flows: список денежных потоков по годам [CF1, CF2, ...]
        :param discount_rate: ставка дисконтирования (например, 0.15 для 15%)
        """
        self.initial_investment = initial_investment
        self.cash_flows = cash_flows
        self.discount_rate = discount_rate

    def calculate_npv(self):
        """Возвращает значение NPV проекта."""
        npv = -self.initial_investment
        for t, cf in enumerate(self.cash_flows, start=1):
            npv += cf / ((1 + self.discount_rate) ** t)
        return npv

    def decision(self):
        """Рекомендация по проекту."""
        npv = self.calculate_npv()
        if npv > 0:
            return f"NPV = {npv:.2f} → проект выгоден ✅"
        elif npv < 0:
            return f"NPV = {npv:.2f} → проект невыгоден ❌"
        else:
            return f"NPV = {npv:.2f} → проект на грани рентабельности ⚖️"