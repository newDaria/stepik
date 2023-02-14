# EXERCISE 1

a = float(input())
b = float(input())
s = 1/2*a*b
print(s)

# EXERCISE 2

s = float(input())
v1 = float(input())
v2 = float(input())

v = v1+v2
t = s/v
print(t)

# EXERCISE 3


a = float(input())

if a == 0:
    print('Обратного числа не существует')
else:
    print(a**(-1))

# EXERCISE 4

f = float(input())

c = 5/9*(f-32)
print(c)

# EXERCISE 5

dog_age = float(input())
human_age = 0
if dog_age < 3:
    human_age = dog_age * 10.5
else:
    human_age = dog_age * 4 +13
print(human_age)

# EXERCISE 6

num = float(input())
new_num = (num - int(num))*10
print(int(new_num))


# EXERCISE 7

num = float(input())
new_num = (num - int(num))
print(new_num)

# EXERCISE 7

a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
numbers = [a,b,c,d,e]
max_num = max(numbers)
min_num = min(numbers)
print(f'Наименьшее число = {min_num}')
print(f'Наибольшее число = {max_num}')

# EXERCISE 7

a,b,c = int(input()),int(input()), int(input())
numbers = [a,b,c]
max_num = max(numbers)
min_num = min(numbers)
print(max_num)
print((a+b+c)-(max_num+min_num))
print(min_num)


# EXERCISE 8

num = int(input())
hundreds = num // 100
tens = (num - (hundreds * 100)) // 10
ones = num % 10
# print(hundreds, tens, ones)

num_list = [hundreds, tens, ones]
max_num = max(num_list)
min_num = min(num_list)
middle_num = (hundreds + tens + ones)-(max_num+min_num)
if max_num - min_num == middle_num:
    print('Число интересное')
else:
    print('Число неинтересное')

# EXERCISE 9

a1,a2,a3,a4,a5  = float(input()),float(input()),float(input()),float(input()),float(input())
a1 = abs(a1)
a2 = abs(a2)
a3 = abs(a3)
a4 = abs(a4)
a5 = abs(a5)
sum_num = a1 +a2 +a3 +a4 +a5
print(sum_num)

# EXERCISE 10
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
distance = abs(p1 -q1) + abs(p2 - q2)
print(distance)