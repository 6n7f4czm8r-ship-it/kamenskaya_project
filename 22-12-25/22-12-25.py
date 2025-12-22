#1
expression = input("Введите выражение: ")
list_of_symbol = ["+", "-", "*", "/"]
operation = ""
for symb in list_of_symbol:
    result = expression.split(symb)
    if len(result) == 2:
        operation = symb
        break
# print (result, operation)

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
