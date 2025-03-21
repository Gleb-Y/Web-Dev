N = int(input("Введите количество элементов: "))
elements = list(map(int, input("Введите элементы через пробел: ").split()))
result = "NO"
for i in range(1, N):
    if (elements[i] > 0 and elements[i - 1] > 0) or (elements[i] < 0 and elements[i - 1] < 0):
        result = "YES"
        break
print(result)