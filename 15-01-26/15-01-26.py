#1
# def text():
#     print ("""`Don`t compare yourself with anyone in this world…
# if you do so, you are insulting yourself`
# Bill Gates""")
#
# text()


#2
# def numb (x,y):
#     z = []
#     for i in range (x, y+1):
#         if i %2==0:
#             z.append(i)
#     print(z)
#
# x = int(input("Первое число: "))
# y = int(input("Второе число: "))
# numb(x, y)

#4
# def cycle(a,b,c,d,e):
#     x = min(a,b,c,d,e)
#     print(x)
#     print(a,b,c,d,e)
#     return x
#
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# c = int(input("Третье число: "))
# d = int(input("Четвертое число: "))
# e = int(input("Пятое число: "))
# cycle(a,b,c,d,e)

# 5
# def numbers(a,b):
#     rez = 1
#     if a == b:
#         print("Error")
#     if a > b:
#         for i in range(b, a + 1):
#             rez *= i
#             print(rez)
#     else:
#         for i in range (a,b+1):
#             rez *= i
#             print(rez)
#     return rez
#
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# print(numbers(a,b))

# 6
# count = 0
# def my_number(x):
#     count = 0
#     # конвертация числа в список
#     for i in x:
#         count =+1
#     print(count)
#     return count
#
#
# x = int(input("Число: "))
# my_number(x)
# print("Количесво символов в числе", my_number(x), "=", count)


# def sum(start_arg: int = 2, end_arg: int = 1):
#     c = start_arg + end_arg
#     print (c)
#
# sum(start_arg=5, end_arg=3)

#7
# def palliandrom(a:int = 123321):
#     x = a // 1000
#     y = a % 1000
#     z = ""
#     for i in str (y) [::-1]:
#         z += i
#     print(z)
#
#     if x == int (z):
#         print("паллиандром")
#     else:
#         print("не паллиандром")
#
# print(palliandrom())
#


