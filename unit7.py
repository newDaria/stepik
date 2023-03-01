# EXERCISE 1

for i in range(10):
    print('Python is awesome!')


# EXERCISE 2
text_input = input()
a = int(input())

for i in range(a):
    print(text_input)

# EXERCISE 3
a = "AAA"
b = "BBBB"
t = "TTTTT"
e = "E"
g = "G"
for i in range(6):
    print(a)

for i in range(5):
    print(b)

print(e)

for i in range(9):
    print(t)

print(g)

# EXERCISE 4

n = int(input())

for i in range(n):
    print('*******************')


# EXERCISE 5

name = input()
for num in range(10):
    print(num,name)

# EXERCISE 6
num = int(input())
for new_num in range(num +1):
    print(f'Квадрат числа {new_num} равен {new_num**2}')

# EXERCISE 7
num = int(input())
for star in range(num):
    print('*'* (num-star))

# EXERCISE 8

#m: стартовое количество организмов;
m = float(input())
#p: среднесуточное увеличение в %;
p = float(input())
#n: количество дней для размножения.
n =int(input())

for body in range(n):
    new_m =m + ( p * m )/ 100
    print(f'{body +1 } {m}')
    m = new_m

# EXERCISE 8
num1 =  int(input())
num2 = int(input())
for n in range(num1, num2+1):
    print(n)

# EXERCISE 9
m = int(input())
n = int(input())
if n > m:
 for num in range(m, n+1):
     print(num)
elif n < m :
    for num in range(n, m + 1):
        print(m)
        m = m -1
elif n == m:
    print(m)

# EXERCISE 10
m = int(input())
n = int(input())
if m - n == 1 and m % 2 == 0:
    print(n)
elif  m - n == 1 and m % 2 != 0:
    print(m)
else:
    for num in reversed(range(n, m, 2)):
        print(num + 1)

# EXERCISE 11
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)

# EXERCISE 12
n = int(input())
for num in range(1,11):
    print(f'{n} x {num} = {n*num}')

# EXERCISE 13

num1 = 4
num2 = 6
num1 += num2
num1 *= num1
print(num1)

# EXERCISE 14
total = 0
for i in range(1, 6):
    total += i
print(total)

# EXERCISE 15
total = 0
for i in range(1, 6):
    total += i
    print(total, end='')

# EXERCISE 16
a, b = int(input()), int(input())
total = 0
for num in range(a,b +1 ):
    if (num ** 3) % 10 == 4  or (num ** 3) % 10 == 9:
        total = total +1
print(total)


