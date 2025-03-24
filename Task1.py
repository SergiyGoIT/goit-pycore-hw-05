def caching_fibonacci():
    # порожній словник для зберігання кешованих значень
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевіряємо, чи є значення в кеші
        if n in cache:
            return cache[n]
        
        # Обчислюємо значення і зберігаємо його в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
