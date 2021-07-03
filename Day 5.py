# Day 5

# 1.
n = int(input())
li = [x for x in range(n)]
print(li)

item = int(input())
li.append(item)
print(li)

item = int(input())
li.remove(item)
print(li)

maxx = max(li)
mini = min(li)
print(maxx, mini)


# 2.
tup = (1, 2, 3, 4, 5)
rev = tup[::-1]
print(tup)
print(rev)


# 3.
tup = ('a', 1, 2)
print(tup)
li = list(tup)
print(li)
