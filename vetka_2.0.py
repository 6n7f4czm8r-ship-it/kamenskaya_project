# Задание 1
# a = int(input("Введите число 1:"))
# b = int(input("Введите число 2:"))
# numbers = range(a, b+1)
# for num in numbers:
#     if 21 % 7 != 0:
#         continue
#     print(num)
# else: print("None")

# Задание 2
a = int(input("Введите число 1:"))
b = int(input("Введите число 2:"))
# val = range(a, b+1)
numbers = range(b, a-1, -1)
# for c in range(a, b+1):
#     print(c)
# for num in numbers:
#     print(num)
for num in numbers:
    if 21 % 7 != 0:
        continue
    print(num)
else: print("None")
