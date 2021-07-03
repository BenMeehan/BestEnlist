# Day 9

# 1.
import math
li = [1, 2, 3, 4]
for i in range(0, len(li)):
    li[i] += 2

print(li)

# 2.
i = 5
while(i > 0):
    j = i
    while(j > 0):
        print(j, end="")
        j -= 1
    print("\n")
    i -= 1

# 3. Fibonacci
n = int(input())
f1 = 0
f2 = 1
print(f1, end=" ")
print(f2, end=" ")
for i in range(n):
    t = f1
    print(f1+f2, end=" ")
    f1 = f2
    f2 = f2+t

# 4. Amstrong number is a number in which the sum of cubes of digit is equal to the number itself
num = int(input("\nEnter a number: "))
summ = 0
temp = num
while temp > 0:
    digit = temp % 10
    summ += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# 5.
n = int(input())
for i in range(1, n+1):
    print(f"{i}x9 = {i*9}")

# 6.
n = int(input())
if(n >= 0):
    print("Positive")
elif(n < 0):
    print("Negative")

7.
n = int(input())
if n >= 365:
    years = int(n/365)
    months = (n % 365)/30

    print(f"{years} years and {months} months old.")
else:
    print(f"{n} days old.")

8.

a = math.pi/2

print("The value of sine of pi/2 is : ", end="")
print(math.sin(a))

print("The value of tan of pi/2 is : ", end="")
print(math.tan(a))

9.
print("Select an operation.")
print("+")
print("-")
print("*")
print("/")
op = input("Enter operation")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if op == '+':
    print(a, "+", b, "=", a+b)
elif op == '-':
    print(a, "-", b, "=", a-b)
elif op == '*':
    print(a, "*", b, "=", a*b)
elif op == '/':
    print(a, "/", b, "=", a/b)
else:
    print("Invalid input")
