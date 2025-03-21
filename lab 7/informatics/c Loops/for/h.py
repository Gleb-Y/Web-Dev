x = int(input("Введите число: "))
print("Делители числа:", end=" ")
for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")