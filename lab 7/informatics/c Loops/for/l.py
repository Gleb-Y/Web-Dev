binary = input("Введите двоичное число: ")
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
print("Десятичное число:", decimal)