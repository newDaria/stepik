# # EXERCISE 1
#
# for i in range(10):
#     print('Python is awesome!')
#
#
# # EXERCISE 2
# text_input = input()
# a = int(input())
#
# for i in range(a):
#     print(text_input)
#
# # EXERCISE 3
# a = "AAA"
# b = "BBBB"
# t = "TTTTT"
# e = "E"
# g = "G"
# for i in range(6):
#     print(a)
#
# for i in range(5):
#     print(b)
#
# print(e)
#
# for i in range(9):
#     print(t)
#
# print(g)
#
# # EXERCISE 4
#
# n = int(input())
#
# for i in range(n):
#     print('*******************')
#
#
# # EXERCISE 5
#
# name = input()
# for num in range(10):
#     print(num,name)
#
# # EXERCISE 6
# num = int(input())
# for new_num in range(num +1):
#     print(f'Квадрат числа {new_num} равен {new_num**2}')
#
# # EXERCISE 7
# num = int(input())
# for star in range(num):
#     print('*'* (num-star))
#
# # EXERCISE 8
#
# #m: стартовое количество организмов;
# m = float(input())
# #p: среднесуточное увеличение в %;
# p = float(input())
# #n: количество дней для размножения.
# n =int(input())
#
# for body in range(n):
#     new_m =m + ( p * m )/ 100
#     print(f'{body +1 } {m}')
#     m = new_m
#
# # EXERCISE 8
# num1 =  int(input())
# num2 = int(input())
# for n in range(num1, num2+1):
#     print(n)
#
# # EXERCISE 9
# m = int(input())
# n = int(input())
# if n > m:
#  for num in range(m, n+1):
#      print(num)
# elif n < m :
#     for num in range(n, m + 1):
#         print(m)
#         m = m -1
# elif n == m:
#     print(m)
#
# # EXERCISE 10
# m = int(input())
# n = int(input())
# if m - n == 1 and m % 2 == 0:
#     print(n)
# elif  m - n == 1 and m % 2 != 0:
#     print(m)
# else:
#     for num in reversed(range(n, m, 2)):
#         print(num + 1)
#
# # EXERCISE 11
# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
#         print(i)
#
# # EXERCISE 12
# n = int(input())
# for num in range(1,11):
#     print(f'{n} x {num} = {n*num}')
#
# # EXERCISE 13
#
# num1 = 4
# num2 = 6
# num1 += num2
# num1 *= num1
# print(num1)
#
# # EXERCISE 14
# total = 0
# for i in range(1, 6):
#     total += i
# print(total)
#
# # EXERCISE 15
# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')
#
# # EXERCISE 16
# a, b = int(input()), int(input())
# total = 0
# for num in range(a,b +1 ):
#     if (num ** 3) % 10 == 4  or (num ** 3) % 10 == 9:
#         total = total +1
# print(total)
import math

# # EXERCISE 17
# n = int(input())
# total = 0
# for num in range(n):
#     new_num = int(input())
#     total += new_num
# print(total)

# EXERCISE 18
#
# n = int(input())
# total  = 1
# for num in range(2, n + 1 ):
#     total +=  1/num
# total -=  math.log(n)
# print(total)

# # EXERCISE 19
#
# n = int(input())
# count = 0
# for num in range(1, n +1 ):
#     if (num ** 2) % 10 == 5 :
#                 count +=num
# print(count)
#
# # EXERCISE 20
# n = int(input())
# total = 1
# for i in range(1,n +1  ):
#     total *= i
# print(total)

# # EXERCISE 21
# total = 1
# for num in range(1, 11):
#         n = int(input())
#         if n > 0:
#             total *= n
# print(total)


# # EXERCISE 22
# n = int(input())
# total = 0
# for num in range(1,n + 1):
#     if  n % num == 0:
#         total += num
# print(total)

# # EXERCISE 23
#
# n = int(input())
# total = 0
# for num in range(1, n +1):
#     if num % 2 == 0:
#         num = num *(-1)
#     else:
#         num = num
#     total += num
# print(total)

# # EXERCISE 24
# n = int(input())
# numbers  = []
# for num in range(n):
#     new_num = int(input())
#     numbers.append(new_num)
# max1 = max(numbers)
# numbers.remove(max1)
# max2 = max(numbers)
# print(max1)
# print(max2)
#
# # EXERCISE 25
# # n = int(input())
# numbers = []
# for num in range(10):
#     n = int(input())
#     numbers.append(n)
#
# no_count = 0
# for number in numbers:
#     if number % 2 != 0:
#         no_count += 1
# if no_count != 0:
#     print('NO')
# else:
#     print('YES')

# # EXERCISE 26
# fib1 = fib2 = 1
# n = int(input())
# if n == 1:
#     print(n)
# else:
#     print(fib1, fib2, end = ' ')
#     for i in range(2,n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end= ' ')

# # EXERCISE 27
# count = 10
# while count < 1:
#     print('Python awesome!')
#
# count = 1
# while count < 10:
#     print('Python awesome!')
#     count += 1
#
# count = 1
# while count < 10:
#     print('Python awesome!')

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1
#
# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# word = input()
# while word != 'КОНЕЦ' and word != 'конец':
#         print(word, end = '\n')
#         word = input()

# # EXERCISE 28
# word = input()
# count = 0
# while word != 'стоп' and word != 'хватит' and word != 'достаточно':
#         count += 1
#         word = input()
# print(count)

# # EXERCISE 30
#
# num = int(input())
# while num % 7 == 0:
#         print(num)
#         num = int(input())

# # EXERCISE 31
#
# num = int(input())
# sum = 0
# while num >= 0:
#     sum  += num
#     num = int(input())
# print(sum)

# # EXERCISE 33
#
# num = int(input())
# count = 0
# while num >= 0 and num <=5:
#     if num == 5:
#         count +=1
#     num = int(input())
# print(count)

# # EXERCISE 34
#
# num = int(input())
# count = 0
#
#
# if num > 0:
#     count25 = int(num / 25)
#     left_after25 = num % 25
#     count10 = int(left_after25 /10)
#     left_after10 = left_after25 % 10
#     count5 = int(left_after10 /5)
#     left_after5 = left_after10 % 5
#     count = count25 + count10 +count5 +left_after5
# print(count)
#
# # EXERCISE 35
#
# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# # EXERCISE 36
#
# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# # EXERCISE 37
#
# num = int(input())
# number_back = []
# while num > 0:
#     new_num = num // 10
#     number_to_print = num % 10
#     num = new_num
#     number_back.append(number_to_print)
#
# for num in number_back:
#     print(num, end = "")

# # EXERCISE 38
#
# num = int(input())
#
#
# number_back = []
# while num > 0:
#     new_num = num // 10
#     number_to_print = num % 10
#     num = new_num
#     number_back.append(number_to_print)
# max_num = max(number_back)
# min_num = min(number_back)
# print(f'Максимальная цифра равна {max_num}')
# print(f'Минимальная цифра равна {min_num}')

#
# # EXERCISE 39
#
# num = int(input())
# # сумму его цифр;
# all_num = []
# while num > 0:
#     new_num = num // 10
#     number_to_print = num % 10
#     num = new_num
#     all_num.append(number_to_print)
# print(all_num)
#
# sum_num = 0
# quantity_of_num = 0
# multi_num = 1
# average = 0
# for i in all_num:
#     sum_num +=i
#     quantity_of_num +=1
#     multi_num  *=i
#     average = sum_num/quantity_of_num
#     last_digit = all_num[-1]
#     sum_first_last = all_num[-1] + all_num[0]
#
#
# print(sum_num)
# print(quantity_of_num)
# print(multi_num)
# print(average)
# print(last_digit)
# print(sum_first_last)

# # EXERCISE 40
#
#
# num = int(input())
# # сумму его цифр;
# all_num = []
# while num > 0:
#     new_num = num // 10
#     number_to_print = num % 10
#     num = new_num
#     all_num.append(number_to_print)
# print(all_num[-2])

# # EXERCISE 41
#
# num = int(input())
#
# all_num = []
# while num > 0:
#     new_num = num // 10
#     number_to_print = num % 10
#     num = new_num
#     all_num.append(number_to_print)
#
#
# def checkList(lst):
#     ele = lst[0]
#     chk = True
#
#     # Comparing each element with first item
#     for item in lst:
#         if ele != item:
#             chk = False
#             break
#
#     if (chk == True):
#         print("YES")
#     else:
#         print("NO")
#
#
# checkList(all_num)
# решить задачку сегодян
# # EXERCISE 42
#
# n = int(input())
#
# flag = 'YES'
# #  остаток от делания
# s = n % 10
# while n != 0:
#     n1 = n % 10
#     if s > n1:
#         flag = 'NO'
#     s = n1
#     n = n // 10
# print(flag)

# # break, continue, else
# # EXERCISE 42
#
# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
# # EXERCISE 43
# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# # EXERCISE 44
# n = int(input())
# for i in range (2, n + 1):
#     if n % i == 0:
#         print(i)
#
#         break
#     else:
#         continue

# # EXERCISE 45
# n = int(input())
# for i in range (1, n +1):
#     if  i < 5 or i > 9 and i < 17 or i > 37 and i < 78 or i > 87:
#             print(i)

# # EXERCISE 46
# n = 0
# while n < 10:
#     n += 2
#     print(n)
# else:
#     print('Цикл завершен.')

# # EXERCISE 47
# n = 0
# while n < 10:
#     n += 2
#     if n == 8:
#         break
#     print(n)
# else:
#     print('Цикл завершен.')

# # EXERCISE 48
# n = 0
# while n < 10:
#     n += 2
#     if n == 7:
#         break
#     print(n)
# else:
#     print('Цикл завершен.')

# EXERCISE 49
count = 0
# p = 0
# первая ощибка что принимает только 9
for i in range(1, 11):
    x = int(input())
    if x > 0:
        # p = p * x
        count += 1


if count > 0:
    print(count)
    # print(p)
else:
    print('NO')


