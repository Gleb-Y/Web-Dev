N = int(input("Введите количество чисел: "))
count = 0
for _ in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        count += 1
print("Количество нулей:", count)