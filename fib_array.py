def fib(n):

    fib_array = [0, 1]  #-Массив с значением для F(0) и F(1)

    if n < 2: #-Массив с значением для F(0) и F(1)
        print(fib_array[:n + 1])
        return fib_array[:n + 1]

    #-Вычисление чисел Фибоначчи через цикл >-
    #-< for и последующей записью их в массив.
    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    print(fib_array) #-Выводим массив
    return fib_array #-Возвращаем массив

fib(9)