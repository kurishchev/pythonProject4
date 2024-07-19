from true_math import divide as true_divide
from fake_math import divide as fake_divide

first = float(input('введите делимое: '))
second = float(input('ведите делитель: '))
print('Результат деления "true_divide": ', true_divide(first, second))
print('Результат деления "fake_divide": ', fake_divide(first, second))