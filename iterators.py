# Empress Djata
# iterator = object contains a countable number of valuws
# methods iter() and next()

# list
for i in [2, 4, 6, 8, 10, 12]:
    print(i)

# string
for char in "Empress is a coder":
    print(char)

# dictionary
for k in {"n": 27, "m": 23}:
    print(k)

# set
for x in {1, 3, 5, 7, 9}:
    print(x)

# tuples
for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(x)

# define a list
my_list = [1, 2, 3, 4, 5]

# get an iterator using iter()
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# create an iterator object from that iterable
iter_obj = iter(my_list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        print("Hit break, iteration stopped")
        break

# for loop
for another_element in my_list:
    print(another_element)
print("End the for loop")