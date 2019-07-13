# break statement will immediately end the loop, even though condition hasn't changed.
# If there is an else/elif block, it will not be executed in the case of a break statement.
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')