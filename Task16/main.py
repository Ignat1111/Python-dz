import random
from re import L


def More5():
   # Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
   #  Используйте для решения лямбда-функцию.
   # 2, 3, 4, 6, 7, 8 -> 6, 7, 8
   numbers = [random.randint(1, 10) for i in range(10)]
   print(numbers)
   def result(x): return x > 5
   numbers = list(filter(result, numbers))
   print(numbers)
