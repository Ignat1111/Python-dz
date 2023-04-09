# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def print_even_numbers(start, stop):
   for i in range(0,9):
      if i % 2 == 0:
            print (i)

print(print_even_numbers(10,20))