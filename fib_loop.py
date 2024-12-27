import time

#-Функция для вычисляет n-е го числа Fib >-
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    # -< с использованием цикла for.
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

#-Функция для измерения времени с возвращением результата.
def measure_fib_time(n):
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    return result, elapsed_time

#-Пример измерения времени для пяти произвольных значений n.
n_values = [5, 10, 20, 30, 32]
for n in n_values:
    result, elapsed_time = measure_fib_time(n)
    print(f"fib({n}) = {result}, время выполнения: {elapsed_time:.6f} мс")