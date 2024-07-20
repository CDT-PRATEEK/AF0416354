months = ["january", "february","march", "january"]
print(months)
months = set(months)
print(months)

# add method- adds single element to the set

months.add("August")
print(months)

# update method- Adds multiple elements (from another set, list, tuple, or any iterable) to the set.

months.update(["April", "may", "june"])
print(months)

# pop() method- doessnt take any arg

l = months.pop()
print(months)
print(l)

#remove(element) method

months.remove("April")
print(months)

# discard() method- no error raised unlike remove()

months.discard("june")
print(months)

# clear() method

months.clear()
print(months)

# union()

days={"monday", "tuesday"}

months.union(days)
print(months)

# intersection()

months.intersection(days)
print(months)

