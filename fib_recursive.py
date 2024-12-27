import time

#-Функция для вычисляет n-е го числа Fib.
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#-Функция для измерения времени выполнения.
def measure_time(n):
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"fib({n}) = {result}, Время выполнения: {execution_time:.2f} мс")

#-Измеряем время для пяти произвольных значений n.
values_of_n = [5, 9, 14, 19, 24]
for n in values_of_n:
    measure_time(n)