a = int(input("Введите a: "))
b = int(input("Введите b: "))
for num in range(a, b + 1):
    if num % 2 == 0:
        print(num, end=" ")