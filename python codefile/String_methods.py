# String methods->

# capitalize()- makes first letter capital(must store after capitalizing)

str = "prateek Sinha"
print(str)
u=str.capitalize()
print(u)


# center(width, fillchar)-> aligns strings to center by filling paddings left and right,fillchar is optional

str= str.center(19,"@")
print(str)

# count( substring , start index , end index) method-> counts the occurences of substring, start and end index are optional

str2 = "mybane si payaejbs jjsbdj"

n = str2.count('a' , 8 , 15)
print(n)

# endwith(substring, start, end)-> returns boolean

isends = str2.endswith("a",0,2)
print(isends)

# find(substring, start , end)-> returns index, otherwise -1

str3 = "welcome to python class"
str4 = str3.find("q")
print(str4)


# index()-> same as find(), except returns error on failure

str5 = str3.index("e")
print(str5)

# isalnum() -> checks if character is alpha numeric, gives falsee on space and speacial characters

str6 = "ihave3pens "
s = str6.isalnum()
print(s)

# isalpha() -> checks if alphabet or not, gives false on space

s = str6.isalpha()
print(s)

# isupper()-> 

str7 = "Hii"
p = str7.isupper()
print(p)

# islower()->

str7 = "hii"
p = str7.islower()
print(p)

# lstrip() , rstrip(), strip()-> removes extra spaces and unwanted characters

str8 = "    Prateek Sinha"

str8 = str8.lstrip()
print(str8)

# rstrip()
str9 = "prateek**"
str9 = str9.rstrip("*")
print(str9)

#strip()

str10 = "@@@prateek@@@"
str10 = str10.strip("@")
print(str10)

# replace()->

s = "java is a programming language. i learn java"
s = s.replace("java", "C", 1)
print(s)

# swapcase()->

e = "prateek"
e = e.swapcase()
print(e)

