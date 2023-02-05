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

# EXERCISE 7
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