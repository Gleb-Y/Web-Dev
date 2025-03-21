N = int(input("Введите количество элементов: "))
elements = list(map(int, input("Введите элементы через пробел: ").split()))
count = 0
for i in range(1, N - 1):
    if elements[i] > elements[i - 1] and elements[i] > elements[i + 1]:
        count += 1
print("Количество элементов, больших обоих соседей:", count)