# expression | string    | search string match ?
#            | abs       | No match
#            | alias     |  match
# ^a...s$    | abyss     | No match
#            | Alias     |  match
#            | an abacus | No match
# ^P....N$ (RegEx) search pattern
# using meta characters (RegEx engine):
# []  .  ^ $ * + ? {} () \ |
# re.match = first word vs re.search = all words for first instance vs re.findall
import re

pattern = '^a...s$'
test_string = 'abyss'

result = re.match(pattern, test_string)

if result:
    print("Search successful")
else:
    print("Search unsuccessful")

pattern2 = '^a...s$'
test_string2 = 'abbbyss'

result2 = re.match(pattern2, test_string2)

if result2:
    print('Search successful')
else:
    print('Search unsuccessful')

# [] = to match, only find matches at start of string
input_str = "Thhhhe film Titanic was released in 1998"

result3 = re.match(r"[abc]", input_str)
print(result3)

input_str2 = "all film Titanic was released in 1998"

result4 = re.match(r"[abc]", input_str2)
print(result4)

input_str3 = "abba film Titanic was released in 1998"

result5 = re.match(r"[abc]", input_str3)
print(result5)

# re.search (pat, str) checks the whole string for first instance
input_str4 = "film Titanic was released in 1998"

result6 = re.search(r"[abc]", input_str4)
print(result6)

input_str5 = "111 film Titanic was released in 1998"

result7 = re.search(r"[abc]", input_str5)
print(result7)

# re.findall = finds all instance of [abc]
input_str6 = "111 film Titanic was released in 1998"

result8 = re.findall(r"[abct]", input_str6)
print(result8)

# other meta characters (RegEx engine):
# . = single char not \n and .. = 2 char (containing 4 char)
result9 = re.search(r'..', 'a')
print(result9)

result10 = re.search(r'..', 'ac')
print(result10)

result11 = re.search(r'..', 'acd')
print(result11)

result12 = re.search(r'..', 'acde')
print(result12)

result13 = re.findall(r'..', 'adde')
print(result13)

result14 = re.findall(r'..', 'acdefght')
print(result14)

# ^ = starts with certain
print(re.search(r'^a', 'a'))
print(re.search(r'^a', 'abc'))
print(re.search(r'^a', 'bac'))
print(re.search(r'^ab', 'abc'))
print(re.search(r'^ab', 'acb'))

# $ = ends with certain char
print(re.search(r'a$', 'a'))
print(re.search(r'a$', 'tabla'))
print(re.search(r'a$', 'cab'))

# * = 0 or more occurrences of pattern left to it
print(re.search(r'ma*n', 'mn'))
print(re.search(r'ma*n', 'man'))
print(re.search(r'ma*n', 'mann'))
print(re.search(r'ma*n', 'maaan'))
print(re.search(r'ma*n', 'main'))  # a is not followed by n
print(re.search(r'ma*n', 'maine')) # a is not followed by n
print(re.search(r'ma*n', 'woman'))

# + =  1 or more occurrences of pattern left to it
print(re.search(r'ma+n', 'mn'))
print(re.search(r'ma+n', 'man'))
print(re.search(r'ma+n', 'mann'))
print(re.search(r'ma+n', 'maaan'))
print(re.search(r'ma+n', 'main'))  # a is not followed by n
print(re.search(r'ma+n', 'maine')) # a is not followed by n
print(re.search(r'ma+n', 'woman'))

# ? = 0 or 1 occurrences of pattern left to it
print(re.search(r'ma?n', 'mn'))
print(re.search(r'ma?n', 'man'))
print(re.search(r'ma?n', 'mann'))
print(re.search(r'ma?n', 'maaan'))
print(re.search(r'ma?n', 'main'))  # a is not followed by n
print(re.search(r'ma?n', 'maine')) # a is not followed by n
print(re.search(r'ma?n', 'woman'))

# {} = {n,m} at least n and at most m repetitions of pattern left to it
print(re.search(r'a{2,3}', 'abc dat'))
print(re.search(r'a{2,3}', 'abc daat'))
print(re.search(r'a{2,3}', 'aabc daaat'))
print(re.search(r'a{2,3}', 'aabc daaaat'))

print(re.findall(r'a{2,3}', 'aabc daaat'))
print(re.findall(r'a{2,3}', 'aabc daaaat'))

# combining expressions = RegEx [0-9]{2,4} matches at least 2 digits but not more than 4 digits
print(re.findall(r'[0-9]{2,4}', 'ab123csde'))
print(re.findall(r'[0-9]{2,4}', '12 and 3456 and 34127 also 456788'))

# {m} = matches exactly m repetitions of the preceding regex
print(re.search('x-{3}x', 'x--x'))
print(re.search('x-{3}x', 'x---x'))
print(re.search('x-{3}x', 'x----x'))

for i in range(1, 6):
    s = f"x{'-' * i}x"
    print(f'{i} {s:10}', re.search('x-{2,4}x', s))

print(re.search('a{3,5}', 'aaaaaaaa'))
print(re.search('a{3,5}?', 'aaaaaaaa'))

# () = used to group sub-patterns
print(re.findall(r'(a|b|c)xz', 'ab xz'))
print(re.findall(r'(a|b|c)xz', 'abxz'))
print(re.findall(r'(a|b|c)xz', 'axz cabxz'))

# grouping constructs = breaks regex into subexpressions or groups
# purposes = grouping (single syntactic entity) and caturing (capture portion of search string : matching subexpression)
print(re.search('(bar)', 'foo bar baz'))
print(re.search('bar', 'foo bar baz'))

print(re.findall('(bar)', 'foo bar baz ggg bar abar'))

print(re.search('bar+', 'foo bar baz'))
print(re.search('(bar)+', 'foo bar baz'))
print(re.search('(bar)+', 'foo barbar baz'))
print(re.search('(bar)+', 'foo barbarbarbar baz'))

# (ba[rz]){2,4}(qux)? = matches 2 or 4 occurrences of either 'bar' or 'baz', followed by 'qux'
print(re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux'))
print(re.search('(ba[rz]){2,4}(qux)?', 'barbar'))

# nested grouping parentheses
print(re.search('(foo(bar)?)+(cow)?', 'foofoobar'))
print(re.search('(foo(bar)?)+(cow)?', 'foofoobarcow'))
print(re.search('(foo(bar)?)+(cow)?', 'foofoocow'))

# | = used for alternation (or operator)
print(re.findall(r'a|b', 'cde'))
print(re.findall(r'a|b', 'ade'))
print(re.findall(r'a|b', 'acdbea'))

# \ = escape various characters including all metacharacters
# \$a = match if a string contains $ followed by a

# \A = match if specified characters are at the start of a string
print(re.findall(r'\Athe', 'the telegraph')) # match
print(re.findall(r'\Athe', 'In the sun')) # no match

# \b = matches if specified char are at beginning or end of a word
print(re.findall(r'\bfoo', 'fooball')) # match
print(re.findall(r'\bfoo', 'a football')) # match
print(re.findall(r'\bfoo', 'afootball')) # no match

print(re.findall(r'foo\b', 'the foo')) # match
print(re.findall(r'foo\b', 'the afoo test')) # match
print(re.findall(r'foo\b', 'theafootest')) # no match

# \B = matches if specified char are NOT at beginning or end of a word
print(re.findall(r'\Bfoo', 'fooball')) # no match
print(re.findall(r'\Bfoo', 'a football')) # no match
print(re.findall(r'\Bfoo', 'afootball')) # match

print(re.findall(r'foo\B', 'the foo')) # no match
print(re.findall(r'foo\B', 'the afoo test')) # no match
print(re.findall(r'foo\B', 'theafootest')) # match

# \d = matches any decimal digit. Equivalent to [0-9]
print(re.findall(r'\d', '17abc6')) # match 1, 7, 6
print(re.findall(r'\d', 'Python Data Science')) # no match

print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar'))
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123'))
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foobar123'))

# \D = matches any NON decimal digit. Equivalent to [^0-9]
print(re.findall(r'\D', '1ab34"50')) # match a, b, "
print(re.findall(r'\D', '1234')) # no match

print(re.search('(foo(bar)?)+(\D\D\D)?', '1234'))
print(re.search('(foo(bar)?)+(\D\D\D)?', 'foofoobar123'))
print(re.search('(foo(bar)?)+(\D\D\D)?', 'foobar123'))

# \s - matches where a string contains any NON whitespace character
print(re.findall(r'\s', 'Python RegEx')) # match
print(re.findall(r'\s', 'PythonRegEx')) # no match

# \S - matches where a string contains any whitespace character
print(re.findall(r'\S', 'a b c')) # match
print(re.findall(r'\S', '')) # no match

# \w - match any alphanumeric character (digit and alphabets) = [a-zA-Z0-9_]
print(re.findall(r'\w', '12&":;c'))
print(re.findall(r'\w', '%">!'))

# \W - match any NON alphanumeric character (digit and alphabets) = = [^a-zA-Z0-9_]
print(re.findall(r'\W', '12&":;c'))
print(re.findall(r'\W', '&#&#&#&#&'))

print(re.findall(r'\W', '1a%">!c'))
print(re.findall(r'\W', 'Python'))

# \Z - matches if the specified characters are at the end of a string
print(re.findall(r'Python\Z', 'I like Python'))
print(re.findall(r'Python\Z', 'I like Python Programming'))
print(re.findall(r'Python\Z', 'Python is fun'))

# \t = check tab
# \n = line break
# \r
# \f
# \v