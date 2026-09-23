# Arithmetic

# + :

a = 45 + 4.5
b = True + False
c = (4 + 5j) + (6 + 7j)

# d = None + 5          # Error: None cannot be added to an integer
d = 5 + 5

e = [1, 2, 3] + [4, 5, 6]
f = (1, 2, 3) + (4, 5, 6)
g = 'rak' + 'esh'

# h = range(1, 4) + range(4, 7)   # Error: range objects cannot be added
h = list(range(1, 4)) + list(range(4, 7))

# i = {1, 2, 3} + {4, 5, 5}      # Error: sets cannot use +
i = {1, 2, 3} | {4, 5, 5}

# j = {1:'a', 2:'b'} + {3:'c', 4:'d'}   # Error: dictionaries cannot use +
j = {1: 'a', 2: 'b'} | {3: 'c', 4: 'd'}

# k = [1, 2, 3] + (1, 2, 3)       # Error: list + tuple is not allowed
k = [1, 2, 3] + list((1, 2, 3))

# l = [1, 2, 3] + 'rak'            # Error: list + string is not allowed
l = [1, 2, 3] + list('rak')

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)


# - :

a = 45 - 5.5
b = (4 + 5j) - (3 + 2j)
c = True - False

# d = [1, 2, 3] - [2, 3]       # Error: lists do not support -
# e = (1, 2, 3) - (2, 3)       # Error: tuples do not support -

d = set([1, 2, 3]) - set([2, 3])
e = set((1, 2, 3)) - set((2, 3))

f = {1, 2, 3, 4} - {2, 1}

# g = {1:'a', 2:'b', 3:'c'} - {2:'b', 3:'c'}   # Error: dictionaries do not support -
g = set({1: 'a', 2: 'b', 3: 'c'}) - set({2: 'b', 3: 'c'})

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


# * :

a = 4 * 5.4
b = True * False
c = (4 + 5j) * (3 + 2j)

# d = [1, 2, 3] * (2, 3)       # Error: list can only be multiplied by an integer
d = [1, 2, 3] * 2

e = [1, 2, 3] * 3

# f = [1, 2, 3] * 3.0          # Error: list cannot be multiplied by float
f = [1, 2, 3] * 3

g = (1, 2, 3) * 3
h = 'rakesh' * 3

# i = {1, 2, 3} * 3            # Error: sets cannot be multiplied
i = {1, 2, 3}

# j = {1:'a', 2:'b', 3:'c'} * 3    # Error: dictionaries cannot be multiplied
j = {1: 'a', 2: 'b', 3: 'c'}

k = [1, 2, 3]
l = range(1, 2, 3)
m = (4, 5, 6)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

print(*k)
print(*l)
print(*m)


# ** : power

a = 5 ** 2
b = 3 ** 2.3
c = (3 + 4j) ** (1 + 2j)

print(a)
print(b)
print(c)


# / :

a = 5 / 2

print(a)


# // :

a = 5 // 2

print(a)

a = 5.5 // 2

print(a)


# % :

a = 5 % 2

print(a)


# Relational Operators

print(5 == 6.5)
print(1 == True)
print(2 == None)
print(4 + 5j == 4 + 6j)

print(5 > 6.5)
print(1 > True)

# print(2 > None)                 # Error: None cannot be compared using >

# print(4 + 5j > 3 + 2j)         # Error: complex numbers do not support >

print([1, 2, 3] == [1, 2, 4])
print([1, 2, 3] > [1, 3, 4])
print((1, 2, 3) > (1, 3, 4))
print({1, 2, 3} > {1, 2})

# print({1:2, 2:3} > {3:4, 4:5})    # Error: dictionaries do not support >

print({1: 2, 2: 3} == {1: 2, 2: 3})
print([1, 2, 3] == (1, 2, 3))

# print([1, 2, 3] > (1, 2, 3))      # Error: list and tuple cannot be ordered compared


# True or False

print(bool(0))       # False
print(bool(4.5))     # True
print(bool(''))      # False
print(bool('r'))     # True
print(bool([]))      # False
print(bool([1]))     # True
print(bool(None))    # False

print()
print()


# Logical Operators

print(4 and 0 and 6)       # 0
print(4 and 1 and 6)       # 6
print(4 or 0 or 6)         # 4
print(0 or '' or [])       # []

# mixed

print(4 or 0 and 6)        # 4

# not reverses the boolean value

print(not False)           # True
print(not True)            # False


# Assignment Operators

a = 10

a += 20
a -= 10
a *= 2
a **= 2
a /= 2
a //= 3
a %= 3

print(a)


# Identity Operators

a = 34
b = 34
print(a is b)

a = 3 + 4j
b = 3 + 4j
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

a = 'rakesh'
b = 'rakesh'
print(a is b)

a = range(1, 4)
b = range(1, 4)
print(a is b)

a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)

a = {1, 2, 3}
b = {1, 2, 3}
print(a is b)

print()
print()


# Membership

a = [1, 2, 3, 4]
b = {1, 2, 3, 4}
c = 'rakesh'
d = (1, 2, 3, 4)
e = {1: 'a', 2: 'b', 3: 'c'}
f = range(1, 4)

print(5 in a)
print(3 in b)
print('r' in c)
print(4 in d)
print('b' in e)
print(3 in e)
print(4 in f)


# Walrus operator

# print(a = 4)       # Error: assignment expression required with :=

print(a := 4)
print(a)


# Ternary operator

a = 5 if 10 > 20 else 6

print(a)

a = [1, 2, 3] if 5 < 10 else (1, 2, 3)

print(a)
