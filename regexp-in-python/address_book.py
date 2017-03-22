import re

names_file = open("./names.txt", encoding="utf-8")

data = names_file.read()

names_file.close()

last_name = 'Love'


# if matching at the beginning of a string, use match, if matching in the
# middle of a string, use search.

# print(re.match(last_name, data))
# print(re.search(r'Kenneth', data))


# \w matches any unicode word char
# \W matches anything that isn't a unicode char

# \s matches any whitespace
# \S matches anythng that isn't whitespace

# \d matches any number from 0 -9
# \D matches anything that isn't a number

# \b matches word boundaries or the edges of a word
# \B matches anything that isn't the edges of a word.

# Will return a unicode char follwed by a comma followed by a char, but only as an exact match.
# print(re.match(r'\w, \w', data))

# will return the first three digit hyphen four digit match it finds.
# print(re.search(r'\d\d\d-\d\d\d\d', data))
# Normally parens will create a regex group, by escape the they can be treated as regular chars.

# Three in curly braces will look for that number of the item. The question marks
# after the parens make them optional. Find all will search the whole document.
# Find all will return an array.
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# print(re.search(r'\w*, \w+', data))

# we can match with sets - this will match some email addresses
# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

# print(re.findall(r'\b[trehous]{9}\b', data))

# negative sets. The ^ indicates an ignore.
# print(re.findall(r'''
#     \b@[-\w\d.]*
#     [^gov\t]
#     ''', data, re.VERBOSE|re.I))
# First a word boundary, then an @, then any number of chars.
# Ignore one or more instances of the letters 'g', 'o' or 'b' and a tab

# print(re.findall(r'''
#     \b[-\w+]*, # Word boundary, 1+ hypehns or chars, and a comma
#     \s # find one whitespace
#     [-\w ]+ # 1+ hypehns and characters and explicit spaces
#     [^\t\n] # ignore tabs and newlines
# ''', data, re.X))

# line = re.search(r'''
#     ^(?P<name>[-\w ]*, \s[-\w ]+)\t # Last and first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
#     (?P<phone>\(?\d{3}\)?-?\s\d{3}-\d{4})?\t # phone number
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t? # job and company
#     (?P<twitter>@[\w\d]+)?$ # Twitter
# ''', data, re.X|re.M).groupdict()

# print(line)
# print(line.groupdict())


# this will compile the regex for later use. Leave out the data argument
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s\d{3}-\d{4})?\t # phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # job and company
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.M)

# print(re.search(line, data).groupdict())

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))
