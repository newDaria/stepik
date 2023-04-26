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

# # EXERCISE 49
# count = 0
# # p = 0
# # первая ощибка что принимает только 9
# for i in range(1, 11):
#     x = int(input())
#     if x > 0:
#         # p = p * x
#         count += 1
#
#
# if count > 0:
#     print(count)
#     # print(p)
# else:
#     print('NO')

# # EXERCISE 50
#
# # принимаем последовательность из 10 чисел
# sequence = []
# for i in range(3):
#     sequence.append(int(input()))
#
# # инициализируем переменные для суммы и максимального отрицательного числа
# sum_neg = 0
# max_neg = -1
#
# # проходим по последовательности и ищем отрицательные числа
# for num in sequence:
#     if num < 0:
#         sum_neg += num
#         if num > max_neg:
#             max_neg = num


# # выводим результаты
# if sum_neg == 0:
#     print("NO")
# else:
#     print( sum_neg)
#     print( max_neg)


# # EXERCISE 51
#
# s = 0
# for i in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)

# # EXERCISE 52
#
# n =input()
# # convert input to a list of num
# all_num = [int(x)for x  in str(n)]
# # print(all_num)
# # max_digit = []
# num_devide_three = []
# for num in all_num:
#     if num % 3 == 0:
#         num_devide_three.append(num)
# if num_devide_three == []:
#     print('NO')
# else:
#     print(max(num_devide_three))

#
# # EXERCISE 53
# n = int(input())
# while n > 9:
#     n //= 10
# print(n)


# # EXERCISE 54
# n = int(input())
# product = 1
#
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)
#
# # EXERCISE 55
# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)

# # EXERCISE 56
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# # EXERCISE 57
#
# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# # EXERCISE 58
# n = int(input())
# # print n range2 times
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# # EXERCISE 59
#
# n = int(input())
# # print n range2 times
# for i in range(n):
#     for j in range(5):
#         print(i + 1, end=' ')
#     print()

# # EXERCISE 60
#
# n = int(input())
# number_digit = 1
# # print n range2 times
# for i in range(n):
#     number_digit = 1
#
#     for j in range(9):
#         print(f'{i + 1} + {number_digit} = {number_digit+(i+1)}')
#         number_digit += 1
#
#     print()

# # EXERCISE 61
# #  Если текущий номер строки меньше или равен половине
# #  высоты треугольника (то есть меньше или равен (n + 1) // 2),
# #  выводится i звездочек. В противном случае выводится (n - i + 1)
# #  звездочек, то есть количество звездочек на каждой строке убывает.
# n = int(input())
# for i in range(1, n + 1):
#     if i <= (n + 1) // 2:
#         print("*" * i)
#     else:
#         print("*" * (n - i + 1))
#
# # EXERCISE 62
#
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# # EXERCISE 62
# n = int(input())
# m = 0
#
# for i in range(n):
#     m += 1
#     for j in range(i + 1):
#         print(m, end='')
#
#     print()

# # EXERCISE 63
# # Решите уравнение в натуральных числах
#
# # 28n+30k+31m=365.
# n = 365//28
# k = 365//30
# m = 365//31
# print(n)
# print(k)
# print(m)
# total = 0
# for n in range(1, 13):
#     for k in range(1, 12):
#         for m in range(1, 11):
#                    if 28 * n + 30 * k + 31 * m == 365:
#                         total += 1
#                         print('n =', n, 'k =', k, 'm =', m)
#                         print('Общее количество натуральных решений =', total)

# # EXERCISE 64
# # 10n+5k+0.5m=100
# n = 100//10
# k = 100//5
# m = 100//0.5
# print(n)
# print(k)
# print(m)
# total = 0
# for n in range(1, 100):
#     for k in range(1, 100):
#         for m in range(1, 100):
#                    if  10*n + 5*k + 0.5 * m == 100  and n + k + m == 100:
#                         total += 1
#                         print('n =', n, 'k =', k, 'm =', m)
#                         print('Общее количество натуральных решений =', total)

# # EXERCISE 65
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         print(a, b, c, d, e)

# # EXERCISE 63
#
# n = int(input())
# m = 1
#
# for i in range(n):
#
#     for j in range(i + 1):
#         print(m, end=' ')
#         m += 1
#
#     print()
#
# # EXERCISE 64
#
# n = int(input())
# # m = 1
# for i in range(1, n + 1):
#     for j in range(1,i+1):
#         print(j , end='')
#         # m +=1
#         for j in range(i - 1, 0, -1):
#             print(j, end='')
#             # m -=1
#
#
#         print()

# # EXERCISE 65
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for j in range(i - 1, 0, -1):
#         print(j, end='')
#     print()
#
# # EXERCISE 66
#
# a = int(input())
# b = int(input())
# # максимальная сумма делителей
# summ_count = 0
# # максимальному значению у которого
# # сумма делителей будет наибольшей
# max_x = 0
#
#
# for x in range(a, b +1):
#     # обнуление счетчика делителей
#     count = 0
#     for i in range (1, b +1):
#         if x % i == 0:
#             count +=i
#             if count >= summ_count:
#                 summ_count = count
#                 max_x = x
# print(max_x, summ_count)

# # EXERCISE 67
# n = int(input())
# plus = '+'
# # первый цикл выводит кол-во строк
# for i in range(1, n + 1):
#     print(i,end='')
#     #  что выводит в каждой строке
#     for j in range(1, n +1):
#             if i % j == 0:
#                 print('+', end ='')
#     print()
#
# EXERCISE 68

# n = int(input())
# lis_n = []
# new_n = 0
#
# while n  > 9:
#     lis_n.append(n % 10)
#     n = n // 10
# # print(lis_n)
#     for i in lis_n:
#         n += i
#     lis_n = []
# print(n)
#
# # while new_n  > 0:
# #     lis_n.append(new_n % 10)
# #     new_n = new_n // 10
# # # print(lis_n)
# # for i in lis_n:
# #     new_n += i
# # print(new_n)

#
# from math import *
# n = int(input())
# summ = 0
# mult = 1
#
# for x in range(1, n+1 ):
#     summ += factorial(x)
# print(summ)

# # EXERCISE 69
# a = int(input())
# b = int(input())
#
# for x in range (a, b +1 ):
#     count = 0
#     for i in range (1, x + 1):
#         if x % i == 0:
#             count += 1
#     if count == 2:
#        print(x)

# Определение суммы вводимого числа

# number = int(input())
# sum = 0
#
# while number > 0:
#     # остаток от деления на 10
#     digit = number % 10
#     # прибавляем к тотал последнюю цифру
#     sum += digit
#     # оставляем только те цифры, которые деляться на 10
#     number //= 10
#
# print("Сумма цифр числа:", sum)


# # EXERCISE 70
# n = int(input())
#
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         digit = n % 10
#         s += digit
#     n //= 10
# print(s)

#
# # EXERCISE 71
# n = 8
# count = 0
# maximum = -10**6 -1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# # EXERCISE 72
#
# n = 4
# count = 0
# maximum = -10**8
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
#
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# # EXERCISE 73
#
# n = int(input())
# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')

#
# # EXERCISE 74
#
# n = int(input())
# n_list = []
# while n > 0:
#     digit = n % 10
#     n_list.append(digit)
#     n = n //10
# # print(n_list)
# print(n_list[-3])


# # EXERCISE 75
#
# n = int(input())
# count3 = 0
# countLast = 0
# countChet = 0
# sumBig5 = 0
# multyBig7 = 1
# count05 = 0
# last = n % 10
# while n > 0:
#     x = n % 10
#     if x == 3:
#         count3 += 1
#     if x == last:
#         countLast += 1
#     if x % 2 == 0:
#         countChet += 1
#     if x > 5:
#         sumBig5 += x
#     if x > 7:
#         multyBig7 *= x
#     if x == 0 or x == 5:
#         count05 += 1
#     n //= 10
# print(count3)
# print(countLast)
# print(countChet)
# print(sumBig5)
# print(multyBig7)
# print(count05)

