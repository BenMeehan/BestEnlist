# Day 13 - Regex
import re

# 1.
st = input()
match = re.match("^[a-zA-Z0-9]*$", st)
if match:
    print("True")


# 2.
st = "ndfbdmabdfjnfj"
match = re.match(".*ab.*", st)
print(match)

# 3.
word = "today 20"
print(bool(re.search("\d$", word)))

# 4.
st = input()
print(re.match(".*[0-9]{1,3}.*", st).group())


# 5.
st = "ABCD"
match = re.match("^[A-Z]*$", st)
if match:
    print("True")
