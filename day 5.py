num = int(input("Input a non-negative number you want to find its factorial: "))
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

print("Factorial of", num, "is", factorial(num))