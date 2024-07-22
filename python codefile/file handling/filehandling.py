# w 

file = open("anudip.txt" , 'w')
file.write("Today is the topic of file handling")
file.close()
print("file is written")

# r

file = open("anudip.txt" , 'r')
data = file.read(10)
print(data)
file.close()


# file.tell()->  returns the current position of the file pointer in the file, 
# which will be 0 at the start of the file.

# file.seek(12) -> moves the file pointer to the position 12 in the file

file = open("anudip.txt" , 'r')
print(file.tell())
file.seek(12)
data = file.read(5)
print(data)
print(file.tell()) # prints the current position of the file pointer after reading 5 characters. Given the file pointer was at position 12 before the read operation, it will now be at position 17 (12 + 5)
file.close()




