# functions: first class objects
# meaning: functions are object, can be referenced, passed to a variable, returned from other functions
# can be defined inside another function & passed as arguments to another function

# Decorators: allow programmer to modify the behavior of function or class
# Decorators: wrap another function (extend behavior w/out parmanently modifying it)
# generic functionality: tacked on to existing class or function's behavior (Decoration)

# logging, enforcing access control & authentication, instrumentation & timing functions, rate-limiting, cashing & more

# 1.) function names are references to functions
# 2.) we can assign multiple names to the same function

from IPython.display import Image
# example 1:
def success(x):
    return x + 1
successor = success
print(successor(20))

# can delete "success" or "successor: w/out deleting function itself
del success
print(successor(10))

# example 2: function inside function
# executes f function
def f():

    # this is the g() function has 2 print statements
    # executes g function
    def g():
        print("Hi it's me 'g'")
        print("Thanks for calling me")

    # this is the f() function has 2 print statements
    print("HaHaHa, this is function 'f'")
    print("I am calling 'g' now from inside my soul:\n")

    # call g function
    g()

# call f function
f()

# example 3: using "proper" return statement in the function

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result

print(temperature(20))

# example 4: factorial
def factorial(n):
    """ calculates the factorial of n,
        n should be an integer and n <= 0 """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# example 5: factorial w/exception
def factorial(n):
    """ calculates the factorial of n,
        n should be an integer and n <= 0 """
    # this checks n every time factorial(n-1) is decreased (example 6 work around)
    if type(n) == int and n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    else:
        raise TypeError("n has to be a positive integer or zero")

print(factorial(9))

# example 6
def factorial(n):
    """ calculates the factorial of n,
        n should be an integer and n <= 0 """
    # function where results are calculated for factorial part
    def inner_factorial(n):
        if n == 0:
            print('returning ... {}'.format(n))
            return 1
        else:
            ret_value = n * inner_factorial(n-1)
            print('returning ... {}'.format(ret_value))

            return ret_value
    # only error check once: n  is int and >= 0
    if type(n) == int and n >= 0:
        # true = preform inner_factorial
        return inner_factorial(n)
    else:
        raise TypeError("n should be a positive int or 0")

# Functions returning Functions
print(factorial(3))

def f(x):
    def g(y):
        return y + x + 3
    return g
# passed 10 for x
print(f(10))
nf1 = f(10)
# passed 20 for y
print(nf1(20))

# example 7: p(x) = a * x^2 + b * x + c
def polynomial_creator(a, b, c):

    def polynomial(x):
        return a * x ** 2 + b * x + c
    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

print(p1)

for x in range(-2, 2, 1):
    print('{:5d}, {:5d}, {:5d}'.format(x, p1(x), p2(x)))

# example 8: polynomial coefficients a_n, ...a_1, a_0
def polynomial_creator(*coefficents):
    """ coefficients are in the form a_n, ... a_1, a_0
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficents[::-1]):
            res += coeff * x ** index
        return res
    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 3, 2)
p4 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))

# see what it does:
coefficents = [1, 23, 4, 45]
for index, coeff in enumerate(coefficents[::-1]):
    print(index, coeff)

# example 9: decorator

def polynomial_creator(*coeffs):
    """ coefficients are in the form a_n, a_n_1 ... a_1, a_0
    """
    def polynomial(x):
        res = coeffs[0]
        for i in range(1, len(coeffs)):
            res = res * x * coeffs[i]
        return res
    return polynomial
p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 3, 2)
p4 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))

# another decorator
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration: ")

foo("Hi")

print("We now decorate foo with f: ")
foo = our_decorator(foo)

print("We call foo after decoration: ")
print(foo(42))