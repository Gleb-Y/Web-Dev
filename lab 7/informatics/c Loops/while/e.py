N = int(input("Введите число N: "))
k = 0
power = 1
while power < N:
    power *= 2
    k += 1
print("Наименьшее k:", k)