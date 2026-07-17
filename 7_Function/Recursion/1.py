# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1
 
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))
print(factorial(4))
print(factorial(5))


# --------------------------------------------------------

# Fibonacci Sequence

def fibonacci(n):
    # Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive Case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(21):
    print(fibonacci(i), end=" ")
