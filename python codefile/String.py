name = "I am a Java Trainer"  # slicing in Strings 

print(name)

print("name[2:4]", name[2:4])
print("name[5:9]", name[5:9])
print("name[:15]", name[:15])
print("name[2:]", name[2:])
print("name[:]", name[:])
print("name[0:17:3]", name[0:17:3])
print("name[::]", name[::])
print("name[::-1]", name[::-1])


# del

str = "Hello"

del str
print(str)


# is keyword - checks reference

x = ["apple" , "banana"]
y = ["apple" , "banana"]
z = x

print(x is z)
print(x is y)




