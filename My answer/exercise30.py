# # Question 1
# count = 0
# for a in range(1, 5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#             if a != b and b != c and a != c:
#                 print(a, b, c)
#                 count += 1
# print('Total number is: ', count)



# # Question 2
# import numpy as np
# I = float(input('利润（万元）： '))
# a = np.array([0, 10, 20, 40, 60, 100])
# rate = np.array([0, 10, 7.5, 5, 3, 1.5, 1]) / 100
# money = 0
# for i in range(1, len(a)):
#     if I >= a[i]:
#         money += (a[i] - a[i - 1]) * rate[i]
#     else:
#         money += (I - a[i - 1]) * rate[i]
#         break
# print('奖金总数是： ', money, '万元')



# # Question 3
# for i in range(10000):
#     a = 0
#     b = 0
#     a = (i + 100) ** 0.5
#     b = (i + 268) ** 0.5
#     if a % 1 == 0 and b % 1 == 0:
#         print(i)



# # Question 4
# #输入某年某月末日：yyyy/mm/dd
# import numpy as np
#
# data = input('请输入日期：')
# data = data.split('/')
#
# year = int(data[0])
# month = int(data[1])
# day = int(data[2])
#
# arr_run = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
# arr_ping = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
#
#
# if year % 4 == 0:
#     arr_year = arr_run
# else:
#     arr_year = arr_ping
#
# days = 0
# for i in range(1, len(arr_run) + 1):
#     if i < month:
#         days += arr_year[i - 1]
#     elif month == i:
#         days += day
#         break
#
# print('总天数: ', days)



# # Question 5
# import numpy as np
# x = int(input('第一个整数：'))
# y = int(input('第二个整数：'))
# z = int(input('第三个整数：'))
#
# data = np.array([x, y, z])
# data.sort()
#
# print('从小到大为：', data)



# # Question 6
# list_num = int(input('数列长度为： '))
# fb = [1, 1]
# for i in range(2, list_num + 2):
#     para = fb[i - 1] + fb[i - 2]
#     fb.append(para)
#
# print(fb)




# # Question 7
# list_orig = [1,2,1,6,'a']
# list_copy = list_orig[:]
# print('original list is ', list_orig)
# print('copy list is ', list_copy)




# # Question 8
# for i in range(1, 10):
#     for j in range(1, 10):
#         print('%d * %d = %d' % (i, j, i * j))




# # Question 9
# import time
#
# user = {
#     'zhhhhhh': '1233123aaa'
# }
#
# def login():
#     global name
#     name = input('Username: ')
#     pswd = input('Password: ')
#     if name not in user:
#         return False
#     return user[name] == pswd
#
# while (not login()):
#     time.sleep(3)
#     print('Authorised failure')
#
# print('Authorised successfully')




# # Question 10
# import time
# format = '%Y-%m-%d %H:%M:%S'
# time_local = time.localtime(time.time())
# print(time.strftime(format, time_local))



# # Question 11
# r1, r2 = 1, 1
# for i in range(1, 22):
#     print(r1, end = ' ')
#     print(r2, end=' ')
#     r1 = r1 + r2
#     r2 = r1 + r2



# # Question 12
# count = 0
# su = []
# for i in range(101, 201):
#     judge = True
#     for j in range(2, int(i**(1/2)) + 1):
#         if i % j == 0:
#             judge = False
#     if judge:
#         count += 1
#         su.append(i)
# print(su)
# print('共有', count)




# # Question 13
# for num in range(100, 1000):
#     hundred = int(num / 100)
#     ten = int((num - hundred * 100) / 10)
#     one = num - hundred * 100 - ten * 10
#     if hundred**3 + ten**3 + one**3 == num:
#         print('水仙花数：', num)



# # Question 14
# num = int(input('待分解的正整数：'))
# arr = []
# pri = 2
# num_ori = num
#
# if num <= 1:
#     print('输入数需要大于1')
# else:
#     while num != 1:
#         if num % pri == 0:
#             num = num / pri
#             arr.append(pri)
#         else:
#             pri += 1
#     mtply = '*'.join(map(str, arr))
#     print('%d = %s' % (num_ori, mtply))




# # Question 15
# score = int(input('请输入成绩：'))
# if score <= 100 and score >= 90:
#     rank = 'A'
# elif score < 90 and score >= 60:
#     rank = 'B'
# elif score <60 and score >= 0:
#     rank = 'C'
# else:
#     rank = 'Wrong input'
# print('%d 属于等级 %s' % (score, rank))




# Question 16



# # Question 17
# class Code():
#     letter = 0
#     space = 0
#     digit = 0
#     others = 0
#     def __init__(self, content):
#         self.content = content
#     def count(self):
#         for i in self.content:
#             if i.isalpha():
#                 self.letter += 1
#             elif i.isspace():
#                 self.space += 1
#             elif i.isdigit():
#                 self.digit += 1
#             else:
#                 self.others += 1
#     def showcount(self):
#         form = '字母个数为%d, 空格个数为%d, 数字个数为%d, 其他字符个数为%d'
#         result = (self.letter, self.space, self.digit, self.others)
#         print(form % result)
#
# content = input('请输入一段字符：')
# code = Code(content)
# code.count()
# code.showcount()




# # Question 18
# num = int(input('请输入基数字：'))
# iter = int(input('重复的次数：'))
# n = 0
# arr = []
#
# for i in range(iter):
#     n += num * 10**i
#     arr.append(n)
# s = sum(arr)
# func = '+'.join(map(str, arr))
# print('%d = %s' % (s, func))




# # Question 19
# ws = []
# for num in range(2, 1000):
#     arr = []
#     ys = 1
#     while num != ys:
#         if num % ys == 0:
#             arr.append(ys)
#             ys += 1
#         else:
#             ys += 1
#     if num == sum(arr):
#         ws.append(num)
# print('完数是：', ws)






# # Qustion 20
# high = 100
# distance = high
# num = 10 # 落地次数
# if num > 1:
#     for i in range(2, num + 1):
#         distance += high
#         high = high / 2
# high = high / 2
# print('共经过%s米， 第十次反弹%s米' % (distance, high))




# # Question 21
# num = 1
# days = 9
# for i in range(days):
#     num = (num + 1) * 2
# print('桃子初始个数为：', num)



# # Question 22
# T1 = ['a', 'b', 'c']
# T2 = ['x', 'y', 'z']
# arr = []
# for i in range(len(T2)):
#     for j in range(len(T2)):
#         for k in range(len(T2)):
#             if i ==j or j == k or i == k:
#                 continue
#             c1 = T1[0] + T2[i]
#             c2 = T1[1] + T2[j]
#             c3 = T1[2] + T2[k]
#             c = tuple([c1, c2, c3])
#             arr.append(c)
# for i in arr:
#     if not (('ax' in i) or ('cx' in i) or ('cz' in i)):
#         print(i)




# # Question 23
# size = 5
# show = '*'
# hide = ' '
# for y in range(size - 1, -size, -1):
#     for x in range(-size + 1, size):
#         if y > -x - size and y < x + size and y > x - size and y < size - x:
#             print(show, end = '')
#         else:
#             print(hide, end = '')
#     print()




# # Question 24
# num, den = 2, 1
# arr = []
# arr.append(num / den)
#
# for i in range(19):
#     num += den
#     den = num - den
#     arr.append(num / den)
#
# arr_sum = sum(arr)
# print('数列之和是%s' % (arr_sum))






# # Question 25
# num = 20
# arr = []
# a = 1
# for i in range(1, num + 1):
#     a = a * i
#     arr.append(a)
# arr_sum = sum(arr)
# print(arr_sum)




# # Question 26
# def fac(num):
#     if num == 1:
#         return 1
#     elif num > 1:
#         return fac(num - 1) * num
# num = 5
# print(fac(num))






# # Question 27
# def reverse(string):
#     if len(string) == 1:
#         return string
#     else:
#         return reverse(string[1: ]) + string[0]
#
# string = input('输入一串字符：')
# string_reverse = reverse(string)
# print(string_reverse)




# # Question 28
# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return age(n - 1) + 2
#
# n = 5
#
# print(age(n))




# # Question 29
# num = int(input('输入一个不超过五位数的正整数：'))
# arr = []
# num_orgn = num
#
# while num != 0:
#     a = num % 10
#     arr.append(str(a))
#     num = num // 10
#
# print('%d 是 %d 位数' % (num_orgn, len(arr)))
# print('%d 反转是 %d' % (num_orgn, eval(''.join(arr))))




# # Question 30
# num_str = str(input('请输入一个五位数：'))
#
# l = len(num_str)
#
# for i in range(l // 2):
#     if num_str[i] != num_str[l - 1 - i]:
#         print('%d 不是回文数' % (eval(num_str)))
#         break
#     elif num_str[i] == num_str[l - 1 - i] and i == l // 2 - 1:
#         print('%d 是回文数' % (eval(num_str)))