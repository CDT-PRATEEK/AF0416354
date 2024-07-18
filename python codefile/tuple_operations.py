
tup1 = (1, 2, 3)
tup2 = ('a', 'b', 'c')

# Accessing elements
print(tup1[0])
print(tup2[1])

# Slicing tuples
print(tup1[1:3])
print(tup2[:2])

# Concatenating tuples
tup3 = tup1 + tup2
print(tup3)

# Repeating tuples
tup4 = tup1 * 2
print(tup4)

# Checking if an element exists
print(2 in tup1)
print('d' in tup2)

# Iterating over a tuple
for item in tup1:
    print(item)

# Getting the length of a tuple
print(len(tup1))

# Finding the index of an element
print(tup2.index('b'))

# Counting occurrences of an element
print(tup1.count(2))


