# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a // b)
        print(a % b)
        print(divmod(a, b))