N = int(input("Введите число N: "))
power = 1
while power < N:
    power *= 2
if power == N:
    print("YES")
else:
    print("NO")