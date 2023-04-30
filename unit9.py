# # строки
#
# s = 'abcdefg'
# print(s[0] + s[2] + s[4] + s[6])
#
# s = 'abcdefg'
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)
# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')
#
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[7])
#
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[-10])
#
# s = input()
# index_letter = 0
# for i in range(0, len(s)):
#     if index_letter < len(s):
#         print(s[index_letter])
#         index_letter +=2

# s = input()
# for i in range(1,len(s)+1):
#     print(s[-i])
#
# name = input()
# second_name = input()
# middle_name = input()
#
# print(second_name[0] + name[0] + middle_name[0])

# # exercise 10
#
# n = input()
# s = 0
# for i in n:
#     s += int(i)
# print(s)

# # exercise 11
#
# n = input()
# count_num = 0
# num_contain = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# for i in num_contain:
#     if i in n:
#         count_num +=1
#     else:
#         count_num +=0
# if count_num > 0 :
#     print('Цифра')
# else:
#     print('Цифр нет')

#
# # exercise 12
#
# n = input()
# count_plus = 0
# count_stars = 0
#
# for i in n:
#     if i =='*':
#         count_stars +=1
#     if i == '+':
#         count_plus += 1
# print(f'Символ + встречается {count_plus} раз')
# print(f'Символ * встречается {count_stars} раз')


# # exercise 13
#
# n = input()
# count = 0
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         count += 1
# print(count)

# # exercise 14
#
# n = input()
# # гласные
# vow =  'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
# # согласные
# con  = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
#
# count_vow = 0
# count_con = 0
#
# for i in range(len(n)):
#
#     if n[i] in vow:
#         count_vow +=1
#     if n[i] in con:
#         count_con +=1
# print(f'Количество гласных букв равно {count_vow}')
# print(f'Количество согласных букв равно {count_con}')

# # exercise 15
#
# n = int(input())
# two_bin = bin(n)
# print(two_bin[2:])

# # срезы
# s = 'abcdefg'
# print(s[2:5])
#
# s = 'abcdefg'
# print(s[3:])
#
# s = 'abcdefg'
# print(s[:3])
#
# s = 'abcdefg'
# print(s[:])
#
# s = 'abcdefg'
# print(s[::-3])
#
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[:12])
#
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])
#
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])
#
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# n = input()
# n_rev = n[::-1]
# if n == n_rev:
#     print("YES")
# else:
#     print("NO")
#
# n = input()
#
# # общее количество символов в строке;
# print(len(n))
# # исходную строку, повторенную 3 раза;
# print(n+n+n)
# # первый символ строки;
# print(n[0])
#
# # первые три символа строки;
# print(n[:3])
#
# # последние три символа строки;
# print(n[-3:])
#
# # строку в обратном порядке;
# print(n[::-1])
#
# # exercises 12
# n = input()
# # третий символ этой строки;
# print(n[2])
# # предпоследний символ этой строки;
# print(n[-2])
# # первые пять символов этой строки;
# print(n[:5])
# # всю строку, кроме последних двух символов;
# print(n[:-2])
# # все символы с четными индексами;
# print(n[::2])
# # все символы с нечетными индексами;
# print(n[1::2])
# # все символы в обратном порядке;
# print(n[::-1])
# # все символы строки через один в обратном порядке, начиная с последнего.
# print(n[::-2])
#
# # exercises 13
# s = input()
# # На вход программе подается строка текста.
# # Напишите программу, которая разрежет ее на две равные части,
# # переставит их местами и выведет на экр
# #
# # for i in len(s):
#
# half = len(s)/2
# # if it is odd
# first_part = len(s) - half
# last_part = half
# if len(s) % 2 == 0:
#     print(s[int(half):]+ s[:int(half)])
# else:
#     print(s[int(half+1) :] + s[:int(half+1)])
# # если длина строки не четная то длина
# # первой части должна быть на один символ больше

# #   ФУНКЦИИ РАБОТЫ СО СТРОКАМИ
# #
# # s = 'i Learn Python language'
# # print(s.capitalize())
# #
# # s = 'i LEARN Python LAnguaGE'
# # print(s.lower())
# #
# # s = '$12344%^$#@!'
# # print(s.lower())
# #
# # s1 = 'a'
# # s2 = s1.upper()
# # print(s1, s2)
# #
# # s = 'i LEARN Python LAnguaGE'
# # print(s.upper())
# #
# # s = 'i LEARN Python LAnguaGE'
# # print(s.swapcase())
# #
# # На вход программе подается строка состоящая
# # из имени и фамилии человека, разделенных одним пробелом.
# # Напишите программу, которая проверяет,
# # что имя и фамилия начинаются с заглавной буквы.
#
# s = input()
# name = s.split()[0]
# second_name = s.split()[1]
# capital = 0
# if name[0].isupper() and second_name[0].isupper():
#     print('YES')
# else:
#     print('NO')

# #  EXERCISE
# #
# # На вход программе подается строка.
# # Напишите программу, которая меняет регистр символов,
# # другими словами замените все строчные
# # символы заглавными и наоборот.
#
# s = input()
# print(s.swapcase())


# #  EXERCISE
# #
# # На вход программе подается строка текста.
# # Напишите программу, которая определяет
# # является ли оттенок текста хорошим или нет.
# # Текст имеет хороший оттенок, если содержит
# # подстроку «хорош» во всевозможных регистрах.
#
# s = input()
#
# if 'хорош' in s.lower():
#     print('YES')
# else:
#     print('NO')
#
# #  EXERCISE
#
# # На вход программе подается строка.
# # Напишите программу, которая подсчитывает
# # количество буквенных символов в нижнем регистре.
# #
# # s = input()
# # count = 0
# # for i in s:
# #     if i.islower():
# #         count +=1
# #
# # print(count)
#
# # Поиск и замена
# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))
#
# s = 'www.stepik.org'
# print(s.startswith('www'))
#
# s = 'www.stepik.org'
# print(s.endswith('.ru'))
#
# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))
#
# s = '     I learn Python language               '
# print(s.strip())
#
# s = 'abcdababa'
# print(s.replace('ab', '123'))

# EXERCISE
#
# На вход программе подается строка текста,
# состоящая из слов, разделенных ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.
#
# s = input()
# print(s.count(" ") + 1)

#
# # EXERCISE
# #
# # На вход программе подается строка
# # генетического кода, состоящая из букв А (аденин)
# # , Г (гуанин), Ц (цитозин), Т (тимин).
# # Напишите программу, которая подсчитывает
# # сколько аденина, гуанина, цитозина и тимина
# # входит в данную строку генетического кода.
#
# s = input().lower()
#
# a = 0
# g = 0
# z = 0
# t = 0
#
#
# for i in s:
#     if i == 'а':
#         a +=1
#     if i == 'г':
#         g += 1
#     if i == 'ц':
#         z += 1
#     if i == 'т':
#         t += 1
#
#
# print(f'Аденин: {a}')
# print(f'Гуанин: {g}')
# print(f'Цитозин:  {z}')
# print(f'Тимин: {t}')

# # EXERCISE
#
# number_s = int(input())
# count_eleven = 0
# final_count = 0
#
# for i in range (0, number_s ):
#     s = input()
#     count_eleven = s.count('11')
#     if count_eleven > 2:
#         final_count +=1
# print(final_count)

# # EXERCISE
#
# s = input()
# count = 0
# for i in range(0,10):
#     count += s.count(str(i))
# print(count)
#
# # EXERCISE
#
# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')
#
# # EXERCISE

# s = input()
# a = 0
# b = 0
#
# for i in s:
#     if s.count(i) >= a:
#         a = s.count(i)
#         b = i
# print(b)


# # EXERCISE
#
# s = input()
# indexes = [i for i, c in enumerate(s) if c == 'f']
# if  s.count('f') == 0:
#     print('NO')
# elif s.count('f') == 1:
#     print(indexes[0])
# else:
#     print(f'{indexes[0]} {indexes[-1]}')

# # EXERCISE
#
# s= input()
# min = s.find('h')
# max = s.rfind('h')
# output = s[: min ] + s[max +1 :]
# print(output)

# # EXERCISE
#
# s = 'aabbAA111ccDDaa'
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
#
# s = 'aabb!@#$11cc'
# print(s.islower())
#
#
# s = 'AAb!@#$11CC'
# print(s.isupper())
#
# s = '    abbc    '
# print(s.isspace())
#
#
# s = 'In {0}, someone paid {1} {2} for two pizzas.'
#
# print(s.format(2010,'10k','Bitcoin' ))


# print(ord('foo'))

# # EXERCISE
#
# a = int(input())
# b = int(input())
#
# for i in range(a,b +1 ):
#     print(chr(i), end= ' ')

#
# # EXERCISE
#
# s = input()
# for i in range(len(s)):
#     print(ord(s[i]), end= ' ')


# name = 'джо'
# print(name.lower())
# print(name.upper())
# print(name)
#
# s = 'Python rocks!'
# print(s[1:6])
#
# s = '    Python rocks!     '
# print(s.strip())
# print(s.upper())
# print(s.replace('o', '@' ))

# s = input()
#
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')

# # EXERCISE
#
# s = input()
# print(s.replace('1', 'one'))
#
#
# # EXERCISE
# s = input()
# print(s.replace('@',''))

#
# # EXERCISE
# s = input()
# indexes = [i for i, c in enumerate(s) if c == 'f']
# if  s.count('f') == 0:
#     print(-2)
# elif s.count('f') == 1:
#     print(-1)
# else:
#     print(f'{indexes[1]}')

# EXERCISE

s = input()
indexes = [i for i, c in enumerate(s) if c == 'h']
rev = s[indexes[0] +1 :indexes[-1]]
print(f'{s[0:indexes[0]+1]}{rev[:: -1]}{s[indexes[-1]:]}')


