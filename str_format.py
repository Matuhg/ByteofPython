# Basic use of format method to construct strings from variables.
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# Example 2 - Same Output, but sloppier and more error-prone
print(name + ' is ' + str(age) + ' years old')

# Numbers within the curly brackets are optional
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# The parameters can also be named instead of using numbers or blanks.
print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

#You can also use "f-strings," introduced in Python 3.6 as a shorter way
# to do named parameters.
print(f'{name} was {age} years old when he wrote this book') # notice the 'f'
print(f'Why is {name} playing with that python?')

# With Format Method, Python substitutes each argument value into the place of the specification
# There can be more detailed specifications, such as:
# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# Prevent \n character from printing by specifying a print should end with a blank.
print('a', end='')
print('b')
# Or end it with a space.
print('a', end=' ')
print('b', end=' ')
print('c')

# Escape sequences
# use \' to specify that a single quote within a quote doesn't end the quote.
print('What\'s your name?')
# Use \n to indicate the start of a new line
print('This is the first line\nThis is the second line.')
# A single backslash at the end of a line indicates the string is continued int he next line, but no new line is added.
print('This is the first sentence. \
      This is the second sentence')
# To specify strings with no special processing, such as escape sequences, specify a raw string by prefixing r or R
print(r'Newlines are indicated by \n')
