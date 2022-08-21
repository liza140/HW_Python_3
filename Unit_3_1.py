# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

from dataclasses import dataclass


N = int(input("Введите необходимое число первых элементов последовательности Фибоначчи: "))
fib_list = [0, 1]
fib_string = '0, 1'

for i in range(2,N):
    fib = fib_list[i-2] + fib_list[i-1]
    fib_list.append(fib)
    fib_string = fib_string + ', ' + str(fib)
print(fib_list)
print(fib_string)

data = open('fibonachi.txt', 'w', encoding='utf-8')
data.writelines(fib_string)
data.close()
