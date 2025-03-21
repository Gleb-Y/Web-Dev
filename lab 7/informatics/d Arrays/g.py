N = int(input("Введите количество элементов: "))
elements = list(map(int, input("Введите элементы через пробел: ").split()))
for i in range(N // 2):
    elements[i], elements[N - 1 - i] = elements[N - 1 - i], elements[i]
print("Массив после перестановки:", " ".join(map(str, elements)))