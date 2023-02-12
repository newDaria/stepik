# # EXERSISE 1
#
# num = int(input())
# a = num % 100
# if a == 0:
#     print('YES')
# else:
#     print('NO')

# # EXERSISE 2
#
# num_column1 = int(input())
# num_line1 = int(input())
# num_column2 = int(input())
# num_line2 = int(input())
# color1 =''
# color2 =''
# if (num_column1 + num_line1) % 2 == 0:
#     color1 = 'white'
# else:
#     color1 = 'black'
#
# if (num_column2 + num_line2) % 2 == 0:
#     color2 = 'white'
# else:
#     color2 = 'black'
#
# if color1 == color2:
#     print('YES')
# else:
#     print('NO')
#

# # EXERSISE 3
#
# age = int(input())
# m = input()
# if m == 'f':
#     if age >= 10 and age <= 15:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# # EXERSISE 4
#
# num = int(input())
# ones = ["","I","II","III","IV","V","VI","VII","VIII","IX","X"]
# if 1<= num <= 10:
#     print(ones[num])
# else :
#     print('ошибка')
#
# # EXERSISE 5
# num = int(input())
# if num % 2 != 0:
#     print('YES')
# elif num % 2 ==0  and 2<= num <=5:
#     print('NO')
# elif num % 2 ==0 and 6<= num <=20:
#     print('YES')
# elif num % 2 ==0 and 20< num:
#     print('NO')

# EXERSISE 6
# ход слона
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

# EXERCISE 7
# ход коня
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

# EXERCISE 8
# ход ферзя
x1, y1 = int(input()),int(input())
x2,y2 = int(input()),int(input())
if x1 == x2 or y1 == y2:
    print('YES')
elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
    print('YES')
else:
    print('NO')
