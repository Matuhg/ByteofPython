def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 3))

# Every function has a implicitly contains a return None statement at the end
# unless you supply your own return statement.
def some_function():
    pass

