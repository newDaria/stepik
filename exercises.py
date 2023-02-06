# EXERCISE 1
s = 0
k = 30
d = k - 5
k = 2 * d
s = k - 100
print(s)
x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print(x)

# EXERCISE 2
first_number = input()
print(first_number)
second_number = 1
third_number = int(first_number) + second_number
print(third_number)
print(third_number + second_number)

# EXERCISE 3
input1 = input()
input2 = input()
input3 = input()
sum = int(input1) + int(input2) + int(input3)
print(sum)

# EXERCISE 4
cube = int(input())
volume = (cube*cube*cube)
summ = 6*(cube*cube)
print('Объем =',volume)
print('Площадь полной поверхности =', summ)

a = int(input())
b = int(input())

# EXERCISE 5
def f(a, b):
    return 3*(a + b)**3 + 275 * b**2 - 127 * a - 41

print ( f(a, b))

# EXERCISE 6
number = int(input())
print(f'Следующее за числом {number} число: {(number+1)}')
print(f'Для числа {number} предыдущее число: {(number-1)}')

# EXERCISE  7
screen = int(input())
block = int(input())
keyboard = int(input())
mouse = int(input())
computers = 3*(screen + block + keyboard + mouse)
print(computers)

# EXERCISE 8
first_input = int(input())
second_input = int(input())
print(f'{first_input} + {second_input} = {first_input+second_input}')
print(f'{first_input} - {second_input} = {first_input-second_input}')
print(f'{first_input} * {second_input} = {first_input*second_input}')

# EXERCISE 9
a1 = int(input())
d = int(input())
n = int(input())
an = a1+d*(n-1)
print(an)

# EXERCISE 10
double_num = int(input())
print(double_num, double_num*2, double_num*3, double_num*4, double_num*5, sep="---")
a = 82 // 3 ** 2 % 7
print(a)

# EXERCISE 11
b1 = int(input())
q = int(input())
n = int(input())
bn = b1 * q**(n - 1)
print(bn)

# EXERCISE 12
sm = int(input())
m = sm // 100
print(m)

# EXERCISE 12
students = int(input())
mandarin = int(input())
mandarin_per_student = mandarin // students
print(mandarin_per_student)
mandarin_left = mandarin % students
print(mandarin_left)

# EXERCISE 13
people = int(input())
people_left = people *(-1)// 2 * (-1)
print(people_left)


# EXERCISE 14
place = int(input())
room = place *(-1) // 4 *(-1)
print(room)

# EXERCISE 15
minutes_input = int(input())
hours = minutes_input // 60
minutes_left = minutes_input % 60
print(f'{minutes_input} мин - это {hours} час {minutes_left} минут.')

#EXERCISE 16
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
sum = a + b + c
print(f'Сумма цифр = {sum}')
mult = a * b * c
print(f'Произведение цифр = {mult}')

# EXERCISE 17
#457
num = int(input())
c = num % 10 #7
b = (num % 100) // 10 #5
a = num // 100 #4
print(a,b,c, sep ='')
print(a,c,b, sep ='')
print(b,a,c, sep ='')
print(b,c,a, sep ='')
print(c,a,b, sep ='')
print(c,b,a, sep ='')

# EXERCISE 18
#754
num = int(input())
a = num // 1000
b = (num % 1000) // 100 #4
c = (num % 100) // 10 #5
d = num % 10 #7

print(f'''
Цифра в позиции тысяч равна {a}
Цифра в позиции сотен равна {b}
Цифра в позиции десятков равна {c}
Цифра в позиции единиц равна {d}
''')


