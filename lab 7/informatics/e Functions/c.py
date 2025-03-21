def xor(x, y):
    return (x and not y) or (not x and y)

x = int(input("Введите x (0 или 1): "))
y = int(input("Введите y (0 или 1): "))

x_bool = bool(x)
y_bool = bool(y)

print("Результат исключающего ИЛИ:", int(xor(x_bool, y_bool)))