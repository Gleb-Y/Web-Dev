a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
for num in range(a, b + 1):
    if num % d == c:
        print(num, end=" ")