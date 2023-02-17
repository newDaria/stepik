# EXERCISE 1
print(
"""
"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
""")

# EXERCISE 2
name = input()
second_name = input()
print(f'Hello {name} {second_name}! You just delved into Python')

# EXERCISE 3
football_name_team = input()
print(f'Футбольная команда {football_name_team} имеет длину {len(football_name_team)} символов')

# EXERCISE 4
city1 = input()
city2 = input()
city3 = input()

city_leng = {city1: len(city1),city2: len(city2), city3: len(city3), }

max_key = max(city_leng, key=city_leng.get)
min_key = min(city_leng, key=city_leng.get)
print(min_key)
print(max_key)

# for 3 city
sorted_citY= sorted(city_leng, key=city_leng.get, reverse=True)
for city in sorted_citY:
    print(city)
import math
# EXERCISE 5
a,b,c = input(), input(), input()
a,b,c = len(a), len(b),len(c)
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print('YES')
else:
    print('NO')

# EXERCISE 6
a = input()
if 'синий' in a:
    print('YES')
else:
    print('NO')

# EXERCISE 7
b = input()
if 'суббота' in b:
    print('YES')
elif 'воскресенье' in b:
    print('YES')
else:
    print('NO')


# EXERCISE 8
email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')

# EXERCISE 9
from math import *
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
num1 = pow(x1 - x2, 2)
num2 = pow(y1 - y2, 2)
s = num1 + num2
result = sqrt(s)
print(result)

# EXERCISE 10
import math
r = float(input())
p = math.pi
print(p*r**2)
print(2*p*r)

# EXERCISE 11

from math import *
a = float(input())
b = float(input())

print((a + b)/2 )
print(sqrt(a * b))
print((2*a*b)/(a+b))
print(sqrt((pow(a,2) + pow(b,2))/2))


# EXERCISE 12
from math import *
x = float(input())
rad = radians(x)
result = sin(rad) + cos(rad) + tan(rad)**2
print(result)

# EXERCISE 13
from math import *
x = float(input())
print(floor(x)+ceil(x))

# EXERCISE 14
from math import *
a,b,c = float(input()),float(input()),float(input())
d = b**2 -4*a*c
if d < 0:
    print('Нет корней')
elif d == 0:
    print((-1)*(b/(2*a)))
elif d>0:
    x1 = (-b - sqrt(d))/(2*a)
    x2 =(-b + sqrt(d))/(2*a)
    x1x2 = [x1,x2]
    print(min(x1x2))
    print(max(x1x2))

# EXERCISE 15
from math import *
n = float(input())
a = float(input())
p = math.pi
s = (n * a**2)/(4*tan(p/n))
print(s)




