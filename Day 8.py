# Day 8

# 1. Merge dictionaries
from statistics import mean, median, mode
dt1 = {'a': "apple", 'b': "ball"}
dt2 = {1: "melon", 2: "kiwi"}
dt_merged = {}

for (key, value) in dt1.items():
    dt_merged[key] = value
for (key, value) in dt2.items():
    dt_merged[key] = value

print("1. Merged Dictionary", dt_merged)

# 2. Sort and Set
li = [1, 6, 3, 5, 2]
for i in range(0, len(li)-1):
    for j in range(i+1, len(li)):
        if(li[j] > li[i]):
            t = li[j]
            li[j] = li[i]
            li[i] = t

print("2. Sorted List : ", li)
print("2. Set = ", set(li))

# 3. Sort dictionary
dt = {'a': "apple", 'm': "mango", 'o': "orange"}
count = 0
for i in dt:
    count += 1
print("3. No of items : ", count)
# without built in function


def sort(dt):
    keys = list(dt.keys())
    for i in range(0, len(keys)-1):
        for j in range(i+1, len(keys)):
            if(keys[j] < keys[i]):
                t = keys[j]
                keys[j] = keys[i]
                keys[i] = t
    for i in keys:
        print(f"{i} : {dt[i]}", end=",")
    print("\n")


sort(dt)

# Using built-in function

sorted_dt = dict(sorted(dt.items()))
print(sorted_dt)


# 4. Replace word
str1 = input("Enter the string : ")
str2 = input("Enter word to replace : ")
str3 = input("Enter new word")

str_new = str1.replace(str2, str3, 1)
print("4. New String : ", str_new)


# 5. Captialize
str1 = input("Enter a string : ")
print("5. Answer : ", str1.title())

# 6. Repeated Items
li = [2, 3, 4, 2, 3]
m = {}

for i in li:
    m[i] = 0

for i in li:
    m[i] += 1

print("6. Repeated elements are : ", end="")

for i in m:
    if(m[i] > 1):
        print(i, end=", ")


# 7. Sum
(a, b, c) = (30, 50, 300)
print("The numbers are : ", a, b, c)
n = int(input("Enter a number : "))
print(f"7. ({a}+{b}+{c})/{n} = {(a+b+c)/n}")


# 8. Mean, Median, Mode
a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))

print(
    f"7. Mean = {mean((a,b,c))}\nMedian = {median((a,b,c))}\nMode = {mode((a,b,c))}")


# 9. Swap Cases
str1 = input()
print(f"8. {str1.swapcase()}")


# 10. Binary and Octa
n = int(input())
bina = 0
place = 1

t = n

while(t > 0):
    res = t & 1
    bina += res*place
    place *= 10
    t = t >> 1

print(f"10.\nBinary : {bina}\nOcta : {oct(n)}")
