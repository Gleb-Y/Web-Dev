x = input("Введите число: ")
d = input("Введите цифру: ")
count = 0
for digit in x:
    if digit == d:
        count += 1
print("Цифра", d, "встречается", count, "раз(а)")