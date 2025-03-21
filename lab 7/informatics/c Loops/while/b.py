N = int(input("Введите число N: "))
divisor = 2
while N % divisor != 0:
    divisor += 1
print("Наименьший делитель, отличный от 1:", divisor)