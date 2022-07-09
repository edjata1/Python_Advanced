# fibonacci number series

def fibonacci(max):
    a, b = 0, 1

    while a < max:
        yield a
        a, b = b, a + b

fib = fibonacci(10)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
