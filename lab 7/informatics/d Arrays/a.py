N = int(input("Введите количество элементов: "))
elements = list(map(int, input("Введите элементы через пробел: ").split()))
result = []
for i in range(0, N, 2):
    result.append(str(elements[i]))
print(" ".join(result))