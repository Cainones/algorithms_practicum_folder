#-Решение методом KMP.
def fib_eo(n):
    #-Генерация чисел Фибоначчи
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    #-Проверка чётности
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

fib_eo(0)  #-Вывод: even (0)
fib_eo(1)  #-Вывод: odd (1)
fib_eo(2)  #-Вывод: odd (1)