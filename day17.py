
# Normal function
def add(x, y):
    return x + y

print(add(10, 20))
print(type(add))

# Lambda function
a = lambda x, y: x + y
print(a(10, 20))
print(type(a))

# Correct lambda syntax
b = lambda x, y: x + y
print(b(10, 20))

# Lambda cannot use return statement explicitly
c = lambda x, y: x + y
print(c(10, 20))
