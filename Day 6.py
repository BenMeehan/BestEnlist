# Day 6

# 1. Merge 2 dictionaries
dt1 = {1: "apple", 2: "mango"}
dt2 = {'a': "archer", 'b': "ball"}
dt3 = {}

for (key, value) in dt1.items():
    dt3[key] = value

for (key, value) in dt2.items():
    dt3[key] = value

print("Dictionary 1 : ", end="")
print(dt1)
print("Dictionary 2 : ", end="")
print(dt2)
print("Merged Dictionary : ", end="")
print(dt3)


# 2. Remove key from dictionary
dt3.pop('a')
print("After removing 'a' : ", dt3)


# 3. Map 2 lists into a dictionary
dt_map = {}
li1 = [1, 2, 3]
li2 = ['orange', 'bannana', 'kiwi']

for i in range(0, len(li1)):
    dt_map[li1[i]] = li2[i]

print("List 1 : ", li1)
print("List 2 : ", li2)
print("Mapped dictionary : ", dt_map)


# 4. Find length of set
s = set(li1)
length = 0

for i in s:
    length += 1

print("Set : ", s)
print(f"length of set is {length}")


# 5. Remove intersection of set 2 from set 1
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 6, 9, 7])

print("Set 1 : ", s1)
print("Set 2 : ", s2)

for i in range(0, len(s1)):
    if i in s2:
        s1.remove(i)

print("Set 1 after removing intersection : ", s1)
