a = int(input("Введите a: "))
b = int(input("Введите b: "))
for num in range(a, b + 1):
    if (num ** 0.5) == int(num ** 0.5):
        print(num, end=" ")