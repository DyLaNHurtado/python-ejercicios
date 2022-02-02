def factorial (n):
    if(n<=1):
        return 1
    return n + factorial(n-1)


print("Factorial de 3 : ",factorial(3))
print("Factorial de 9 : ",factorial(9))
print("Factorial de 0 : ",factorial(0))
print("Factorial de -2 : ",factorial(-2))