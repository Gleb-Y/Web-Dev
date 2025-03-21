def power(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

a = float(input("Введите число a: "))
n = int(input("Введите степень n: "))

print(f"{a} в степени {n} равно:", power(a, n))