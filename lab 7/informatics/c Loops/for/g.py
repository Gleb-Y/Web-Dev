x = int(input("Введите число: "))
for i in range(2, x + 1):
    if x % i == 0:
        print("Минимальный делитель:", i)
        break