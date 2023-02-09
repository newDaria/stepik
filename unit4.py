# EXERCISE 1
num = int(input())
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# EXERCISE 2
num = int(input())
a = num // 1000
b = (num % 1000) // 100 #4
c = (num % 100) // 10 #5
d = num % 10 #7
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')

# EXERCISE 3
age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# EXERCISE 4
a = int(input())
b = int(input())
c = int(input())

if c == (b - a) + b:
    print('YES')
else:
    print('NO')

# EXERCISE 5

a = int(input())
b = int(input())
c = int(input())
d = int(input())
num_list = [a,b,c,d]
min_num = min(num_list)
print(min_num)

# EXERCISE 6

age = int(input())
if age <= 13:
    print('детство')
elif age < 25:
    print('молодость')
elif age < 60:
    print('зрелость')
else:
    print('старость')

# EXERCISE 7

a = int(input())
b = int(input())
c = int(input())

if a > 0:
    a = a
else:
    a = 0

if  b > 0:
    b = b
else:
    b = 0

if  c > 0:
    c = c
else:
    c = 0
print(a+b+c)