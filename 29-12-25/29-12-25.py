import random
random_numbers = [random.randint(-5, 10) for _ in range(15)]
# random_numbers = [1,-3,-2,-1,0,1,2,3]
print(random_numbers)

a = 0
b = 0
for _ in random_numbers:
    if _ < 0:
        a +=_
    elif _ % 2 == 0 and _ >0:
        b +=_
print(f"Сумма отрицательных чисел = {a}\n"
      f"Сумма четных чисел = {b}")

