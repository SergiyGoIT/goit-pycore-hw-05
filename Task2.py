import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку всіх дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    matches = re.findall(pattern, text)
    
    # Повертаємо кожне знайдене число як float
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    # Використовуємо генераторну функцію для підсумовування всіх дійсних чисел у тексті
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")