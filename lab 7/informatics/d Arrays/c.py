N = int(input("Введите количество элементов: "))
elements = list(map(int, input("Введите элементы через пробел: ").split()))
count = 0
for num in elements:
    if num > 0:
        count += 1
print("Количество положительных элементов:", count)