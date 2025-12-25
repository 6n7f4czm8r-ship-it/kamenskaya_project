#1
expression = input("Введите выражение: ")
list_of_symbol = ["+", "-", "*", "/"]
operation = ""
for symb in list_of_symbol:
    result = expression.split(symb)
    if len(result) == 2:
        operation = symb
        break
print (result, operation)

# if operation == "*":
#     a = int(result[0]) * int(result[1])
#     print(a)
# if operation == "+":
#     a = int(result[0]) + int(result[1])
#     print(a)
# if operation == "/":
#     a = int(result[0]) / int(result[1])
#     print(a)
# if operation == "-":
#     a = int(result[0]) - int(result[1])
#     print(a)


#2
import random
random_numbers = [random.randint(-5, 10) for _ in range(15)]
print(random_numbers)

# x = min(random_numbers)
# print(x)

# y = max(random_numbers)
# print(y)

count = 0
a = 0
positive_numb_count = 0
negative_numb_count = 0
for _ in random_numbers:
    if _ == 0:
        count +=1
        continue
    elif _ > 0:
        positive_numb_count +=1
        continue
    elif _ < 0:
        negative_numb_count +=1
print (f"{a} повторяется {count} раз\n"
       f"Число положительных элементов повторяется {positive_numb_count} раз\n"
       f"Число отрицательных элементов повторяется {negative_numb_count} раз")
