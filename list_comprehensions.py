fruits = ["apple", "banana", "cherry", "grapes", "oranges", "kiwi", "mango"]

newlist = []

for x in fruits:
    if "o" in x :
        newlist.append(x)

print(newlist)

newlist2 = [each_fruit for each_fruit in fruits if "o" in each_fruit]

print(newlist2)

# store each letter
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

h_letters2 = [ letter2 for letter2 in 'human']
print(h_letters2)

# store number  if with list
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# store number nested if
num_list = [y for y in range(100) if y % 7 == 0 if y % 5 == 0]
print(num_list)

# store using if else with list
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

# show the first letter of each word
listOfWords = ["this", "is", "a", "list", "of", "words"]
items = [word[0] for word in listOfWords]
print(items)

# lower/upper case converter
[x.lower() for x in ["A", "B", "C"]]
['a', 'b', 'c']


# list comprehension in functions
def double(x):
    # squaring
    return x**2
b = [double(x) for x in range(10)]
print(b)

# no duplicates list comprehension
text = "life, uh, finds a way,in a great way indeed"
unique_vowels = {each_letter for each_letter in text if each_letter in 'aeiou'}
print(unique_vowels)

# dictionary comprehension

squares = {i: i * i for i in range(10)}
print(squares)
