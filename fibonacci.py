# not memoized
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage:
n= int(input("Enter a number: "))
fib_sequence = fibonacci_recursive(n)
print("Fibonacci sequence for n =", n, ":", fib_sequence)

#memoized
from functools import wraps

def memoize(func):
     cache = {}

     @wraps(func)
     def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
             cache[key] = func(*args, **kwargs)

        return cache[key]
     return wrapper

@memoize
def recur(n):
    if n < 2:
        return n
    return recur(n-1) + recur(n-2)

fib = int(input("Enter a number: "))
print(f"Fibonnaci sequence until the {fib} position")
for i in range(fib):
    if i != fib-1:
        print(recur(i), end=', ')
    else:
        print(recur(i))
