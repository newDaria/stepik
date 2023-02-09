

# EXERCISE 1
num = int(input())
if num > -1 and num <17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# EXERCISE 2
num = int(input())
if num <= -3 or num >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# EXERCISE 3
num = int(input())
if num > - 30 and num <= -2 or num > 7 and num <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# EXERCISE 4
num = int(input())
num_str = str(num)
if len(num_str) == 4 and num % 7 == 0:
    print('YES')
elif len(num_str) == 4 and num % 17 == 0:
    print('YES')
else:
    print('NO')

# EXERCISE 5
# Напишите программу, которая принимает три положительных
# числа и определяет, существует ли невырожденный
# треугольник с такими сторонами.
a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')


# EXERCISE 6
# Напишите программу, которая определяет, является ли
# год с данным номером високосным.
# Если год является високосным,
# то выведите «YES», иначе выведите «NO».
# Год является високосным,
# если его номер кратен 4,
# но не кратен 100, или если он кратен 400.
year = int(input())
if year % 4 == 0 and year%100 != 0 or year% 400 == 0:
    print('YES')
else:
    print('NO')

# EXERCISE 7
#
# Даны две различные клетки шахматной доски.
# Напишите программу, которая определяет,
# может ли ладья попасть с первой клетки на вторую
# одним ходом. Программа получает на вход четыре
# числа от 1 до 8 каждое, задающие номер столбца
# и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести «YES»,
# если из первой клетки ходом ладьи можно попасть во вторую,
# или «NO» в противном случае.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 and y1 != y2:
    print('YES')
elif y1 == y2 and x1 != x2:
    print('YES')
else:
    print('NO')

# EXERCISE 7
# ход короля
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 and  y2 == y1 + 1:
    print('YES')
elif x1 == x2 and y2 == y1 - 1:
    print('YES')
elif y1 == y2 and x2 == x1 + 1:
    print('YES')
elif y1 == y2 and  x2 == x1 -1:
    print('YES')
elif x2 == x1 + 1 and y2 == y1 + 1:
    print('YES')
elif x2 == x1 - 1 and y2 == y1 - 1:
    print('YES')
elif x2 == x1 - 1 and y2 == y1 + 1:
    print('YES')
elif x2 == x1 + 1 and y2 == y1 - 1:
    print('YES')
else:
    print('NO')