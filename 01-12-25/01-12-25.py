#1
# def jobs():
#     print("“Don't let the noise of others' opinions")
#     print("drown out your own inner voice.“")
#     print("                                Steve Jobs")
# jobs()
# from tabnanny import check


#2
# def numbers(x,y):
#     check=[]
#     if x > y:
#         for i in range (y,x):
#             if i % 2!=0:
#                 check.append(i)
#         print(check)
#     else:
#         for i in range (x,y):
#             if i % 2!=0:
#                 check.append(i)
#         print(check)
#
# numbers(90,15)

#4
# def numbers(a,b,c,d):
#     check=[]
#     check.append(a)
#     check.append(b)
#     check.append(c)
#     check.append(d)
#     print(max(check))
#
# numbers(5,6,8,10)

#5
# def numbers(a,b):
#     check=[]
#     check.append(a)
#     check.append(b)
#     return (sum(check))
#
# a = numbers(10,222)
# print(a)

#6
# def is_prime (x):
#     if x // x == 1 and x // 1 == x:
#         return ("True")
#     else: return ("False")
#
# x = int(input("Число: "))
# print(is_prime (x))

#7
# number= int(input("Введите число: "))
# if number >= 100000 and number <= 999999:
#     # print((number % 10))
#     # print(((number // 10) % 10))
#     # print(((number // 100) % 10))
#     # print(((number // 1000) % 10))
#     # print(((number // 10000) % 10))
#     # print((number //  100000 % 10))
#     if ((number % 10)) + ((number // 10) % 10) + ((number // 100) % 10) == ((number // 1000) % 10) + ((number // 10000) % 10) + ((number // 100000 % 10)):
#         print("Счастливое число")
#     else:
#         print ("Несчастливое число")

