# EXERCISE 1

zoom = int(input())
flash  = int(input())

if zoom > flash:
    print('NO')
elif zoom == flash:
    print("Don't know")
else:
    print('YES')

# EXERCISE 2

a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
elif a != b and b != c:
    print('Разносторонний')

# EXERCISE 2

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 < num3:
    print(num1)
elif num1 > num3 and num1 < num2:
    print(num1)
elif num2 > num1 and num2 < num3:
    print(num2)
elif num2 > num3 and num2 < num1:
    print(num2)
else:
    print(num3)

# EXERCISE 3

month = int(input())
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)

# EXERCISE 4
weight = int(input())
if weight < 60:
    print('Легкий вес')
elif weight < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')

# EXERCISE 4
a = int(input())
b = int(input())
operation = input()
if b == 0 and operation == '/':
    print('На ноль делить нельзя!')
elif operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    print(a/b)
else:
    print('Неверная операция')

# EXERCISE 5

color1 = input()
color2 = input()

if color1 == 'красный' and color2 == 'синий'  or color1 == 'синий' and color2 == 'красный':
    print('фиолетовый')
elif color1 == 'красный' and color2 == 'желтый'  or color1 == 'желтый' and color2 == 'красный':
    print('оранжевый')
elif  color1 == 'синий' and color2 == 'желтый'  or color1 == 'желтый' and color2 == 'синий':
    print('зеленый')
elif color1 == 'красный' and color2 == 'красный':
    print('красный')
elif color1 == 'синий' and color2 == 'синий':
    print('синий')
elif color1 == 'желтый' and color2 == 'желтый':
    print('желтый')
else:
    print('ошибка цвета')

# EXERCISE 5

num = int(input())
if num >= 0  and num <=36:
    if num == 0:
        print('зеленый')
    elif num >= 1 and num <= 10:
        if num % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif num >= 11 and num <= 18:
        if num % 2 == 0:
            print('красный')
        else:
            print('черный')
    elif num >= 19 and num <= 28:
        if num % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif num >= 29 and num <= 36:
        if num % 2 == 0:
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')

# EXERCISE 5
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < b1 < a2 < b2 or a2 < b2 < a1 < b1:
    print('пустое множество')

elif a1 < a2 < b1 < b2:
    print(a2,b1)

elif a2 < a1 < b2 < b1:
    print(a1,b2)
elif a1 < b1 == a2 < b2:
    print(b1)
elif a1 == a2 < b1 < b2:
    print(a1,b1)
elif a1 == a2 < b1 < b2 :
    print(a1)
elif a2< a1 < b1 == b2:
    print(a1, b1)
elif a1 == a2 < b2 < b1:
    print(a2,b2)
elif a1 < a2 < b1 == b2:
    print(a2,b2)
elif a1 < a2 < b2 < b1:
    print(a2,b2)
elif a2 < a1 < b1 < b2:
    print(a1,b1)
elif a1 == a2 < b1 == b2:
    print(a1,b1)
elif a2 < b2 == a1 < b1:
    print(a1)


