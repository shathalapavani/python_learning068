
# 1. Functions with return values

def add(a, b):
    print('add function')
    c = a + b
    return c
    print('HI')  # This line will not execute

def sub(a, b):
    print('sub function')
    c = a - b
    return c

def div(a, b):
    print('div function')
    c = a / b
    return c


x = add(10, 15)
y = sub(20, 10)
z = div(25, 10)

print(x)
print(y)
print(z)
print()


# 2. Positional and keyword arguments

def detail(name, age, rollno):
    print(f'My name is {name}')
    print(f'My age is {age}')
    print(f'My rollno is {rollno}')


# Positional arguments
detail('rakesh', 20, 'A101')

# Positional arguments in a different order (valid, but values change meaning)
detail(20, 'A101', 'rakesh')

# Keyword arguments
detail(age=20, rollno='A101', name='rakesh')
detail(rollno='A101', age=20, name='rakesh')
print()


# 3. Default arguments

def add_numbers(a, b=10, c=20):
    return a + b + c


print(add_numbers(1))
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))
print(add_numbers(c=3, a=1, b=2))
print()


# 4. Correct order of default arguments
# Required arguments must come before default arguments.

def sub_numbers(a, b, c=10):
    return a - b - c


print(sub_numbers(20, 5))
print(sub_numbers(20, 5, 2))
print(sub_numbers(a=20, b=5, c=2))
print()


# 5. Variable-length positional arguments (*args)

def f1(*a):
    print(a)
    print(type(a))


f1(1, 2, 3, 4)
print()


# 6. Variable-length keyword arguments (**kwargs)

def f2(**a):
    print(a)
    print(type(a))


f2(a=1, b=2, c=3, d=4)
   