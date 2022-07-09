def getSequenceUpTo(x):
    for i in range(x):
        yield i

seq = getSequenceUpTo((10))

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))