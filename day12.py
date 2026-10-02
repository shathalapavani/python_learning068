# #FOR LOOP PROBLEMS
#basic understanding
#1. print numbers from 1 to 10 in one line
for i in range(1, 11):
    print(i, end=" ")
#2. print even numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 == 0:
        print(i, end=" ")
#3. print odd numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 != 0:
        print(i, end=" ")
#4. print numbers divisible by 5 from 1 to 30 in one line
for i in range(1, 31):
    if i % 5 == 0:
        print(i, end=" ")
#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")
#6. sum of numbers from 10 to 25 
total = 0

for i in range(10, 26):
    total += i

print(total)
#7. sum of numbers in any list
numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total += i

print(total)
#8. multiplication table of a number 
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)

#interview problems
#9. factorial 
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)
#10. fibonacci 
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#11. reverse a string
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)

#12. count vowels in a string
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print(count)
#13. count z's and y's in a string
text = input("Enter a string: ")

z_count = 0
y_count = 0

for ch in text:
    if ch == "z":
        z_count += 1
    elif ch == "y":
        y_count += 1

print("z:", z_count)
print("y:", y_count)
#14. check whether a number is prime number or not 
num = int(input("Enter a number: "))

count = 0

for i in range(2, num):
    if num % i == 0:
        count += 1

if num > 1 and count == 0:
    print("Prime")
else:
    print("Not Prime")


#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
i = 1

while i <= 10:
    print(i, end=" ")
    i += 1
#print even numbers from 1 to 10
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i, end=" ")

    i += 1
#print numbers divisible by both 5 and 7 from 1 to 500 
i = 1

while i <= 500:
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")

    i += 1

#interview problems
#count digits
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)
#reverse a number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)
#palindrome number 
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#palindrome string (without slicing, built in function)
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#armstrong number
num = int(input("Enter a number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** 3
    num = num // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
 