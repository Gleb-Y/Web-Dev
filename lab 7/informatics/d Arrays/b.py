N = int(input("Введите количество элементов: "))
elements = list(map(int, input("Введите элементы через пробел: ").split()))
result = []
for num in elements:
    if num % 2 == 0:
        result.append(str(num))
print(" ".join(result))