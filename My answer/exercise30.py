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



# Question 14



















