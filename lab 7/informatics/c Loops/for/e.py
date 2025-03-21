x = int(input("Введите число: "))
sum_digits = 0
for digit in str(x):
    sum_digits += int(digit)
print("Сумма цифр:", sum_digits)