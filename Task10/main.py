# Задача 2. В списке находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

fruits = ["айва", "авокадо", "абрикос", "апельсин", "мандарин", "яблоко", "вишня", "гранат"]
for fruit in fruits:
   if fruit.startswith("а"):
      print(fruit)