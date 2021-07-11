# Day 21

# 1.
li1 = [1, 2, 3]
li2 = ['a', 'b', 'c']
merged = list(zip(li1, li2))
print(merged)

# 2.
ran = range(1, 9)
li = ['apple', 'mango', 'orange', 'kiwi', 'white', 'yellow', 'blue', 'black']
range_merge = list(zip(ran, li))
print(range_merge)

# 3.
li.sort()
print(li)

# 4.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(filter(lambda x: x % 2 != 0, li))
print(res)
