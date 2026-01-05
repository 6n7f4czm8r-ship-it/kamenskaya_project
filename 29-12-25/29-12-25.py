import random
random_numbers = [random.randint(-5, 10) for _ in range(15)]
# random_numbers = [1,-3,-2,-1,0,1,2,3]
# print(random_numbers)

a = 0
# b = 0
# c = 0
# for _ in random_numbers:
#     if _ < 0:
#         a +=_
#     elif _ % 2 == 0 and _ >0:
#         b +=_
#     elif _ % 2 != 0 and _ >0:
#         c +=_
# print(f"Сумма отрицательных чисел = {a}\n"
#       f"Сумма четных чисел = {b}\n"
#       f"Сумма нечетных чисел = {c}n")

numbers = []
# y = 1
# for d in random_numbers:
#     if d %3 == 0:
#         numbers.append(d)
#         continue
#     for num in numbers:
#         y *= num
#         print (y)

rez = min (random_numbers)
# # print (rez)
val = max (random_numbers)
# # print (val)
# print (rez * val)

# for a in random_numbers:
#     if a > 0:
#         numbers.append(a)
#         continue
# print(random_numbers)
# print(numbers)
# first = numbers[0]
# last = numbers[-1]
# print(first, last)
#
# summ_numbers = 0
# for num_1 in random_numbers:
#     if num_1 == first:
#         first_index = random_numbers.index(num_1)
#
# for num_2 in random_numbers[::-1]:
#     if num_2 == last:
#         last_index = random_numbers.index(num_2)
#
# my_list = random_numbers[first_index+1:last_index]
# # summ_numbers += random_numbers[first_index+1:last_index]
# pass






