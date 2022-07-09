# 1:18:10 timecode in video

def power(base, exponent):
    print('{} to the power {} = {}'.format(base, exponent, base ** exponent))
    return base ** exponent

def square(base):
    return power(base, 2)

def cube(base):
    return power(base, 3)

def fouth(base):
    return power(base, 4)

square(10)

cube(5)

fouth(16)

from functools import partial
square2 = partial(power, exponent=2)
cube2 = partial(power, exponent=3)
square2(2)
cube2(2)

# case 2

def f(a, b, c, x):
    return 1000*a + 100*b + 10*c +x

g = partial(f, 3, 1, 4)
print(g(10))

def add(a, b, c):
    return 100 * a + 10 * b + c

add_part = partial(add, c = 2, b = 1)

print(add_part(3))