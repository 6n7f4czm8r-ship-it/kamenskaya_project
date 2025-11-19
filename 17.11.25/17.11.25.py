#1
# text = input("Строка: ") [::-1]
# print(text)

#2
# text = input("Строка: ")
# letter = 0
# number = 0
# for symb in text:
#     if symb.isalpha():
#         letter +=1
#     elif symb.isdigit():
#         number +=1
# print(f"Букв: {letter} ")
# print(f"Цифр: {number}")

#3
# text = input("Строка: ")
# symb = input("Нужный символ: ")
# c = 0
# for i in text:
#     if i == symb:
#         c += 1
# print(f"Символ {i} повторяется {c} раз")

#4
# text = input("Строка: ")
# word = input("Нужное слово: ")
# val = text.count(word)
# print(f"Слово {word} повторяется {val} раз")

#5
# text = input("Строка: ")
# word = input("Нужное слово: ")
# word_2 = input("Замена: ")
# text_2 = text.replace(word, word_2)
# print(text_2)