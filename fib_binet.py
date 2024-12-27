import math

def fib(n):
    pln = (1 + math.sqrt(5)) / 2 #-Золотое сечение.
    min = (1 - math.sqrt(5)) / 2 #-Сопряжённое значение.
    
    #-Итерпретация формулы Бине для чисел Фибоначи.
    fib_binet_n = (pln**n - min**n) / math.sqrt(5)
    return round(fib_binet_n) #-Функция округления.

print(fib(34)) #-Работает только для значений 1 ≤ n ≤ 64.