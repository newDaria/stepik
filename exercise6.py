# # EXERCISE 1
#
# a = float(input())
# b = float(input())
# s = 1/2*a*b
# print(s)

# # EXERCISE 2
#
# s = float(input())
# v1 = float(input())
# v2 = float(input())
#
# v = v1+v2
# t = s/v
# print(t)

# # EXERCISE 3
#
#
# a = float(input())
#
# if a == 0:
#     print('Обратного числа не существует')
# else:
#     print(a**(-1))

# # EXERCISE 4
#
# f = float(input())
#
# c = 5/9*(f-32)
# print(c)

# # EXERCISE 5
#
# dog_age = float(input())
# human_age = 0
# if dog_age < 3:
#     human_age = dog_age * 10.5
# else:
#     human_age = dog_age * 4 +13
# print(human_age)
#
# # EXERCISE 6
#
# num = float(input())
# new_num = (num - int(num))*10
# print(int(new_num))

#
# # EXERCISE 7
#
# num = float(input())
# new_num = (num - int(num))
# print(new_num)
#
# # EXERCISE 7
#
# a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
# numbers = [a,b,c,d,e]
# max_num = max(numbers)
# min_num = min(numbers)
# print(f'Наименьшее число = {min_num}')
# print(f'Наибольшее число = {max_num}')

# EXERCISE 7
# сделать условие для строки где вводные данные равны
a,b,c = int(input()),int(input()), int(input())
numbers = [a,b,c]
max_num = max(numbers)
min_num = min(numbers)
if a != max_num and a != min_num:
    print(max_num)
    print(a)
    print(min_num)
elif b != max_num and b != min_num:
    print(max_num)
    print(b)
    print(min_num)
elif c != max_num and c != min_num:
    print(max_num)
    print(c)
    print(min_num)