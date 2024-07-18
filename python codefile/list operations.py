list1 = [1,2,3,4,55,'hello', 67 ,55, 99, 88 ,66]

print(list1)
print(*list1)       # without formatting

#FETCHING OF ELEMENTS 

print(list1[-2])
print(list1[-2:1])              #sublist = listname[startIndex : endIndex : step]

#4th element from last

print(list1[-4])

print("from 3rd to 10th position:" , list1[2:10])

print("alternate elements from 3rd to 10th : ", list1[2:10:2])


print("--------------------------------------")

#removing elements from list

# pop -> deletes element from specified position in list    -> list.pop(index)

# if we do not specify the index, last element is deletedd automatically

list1.pop(5)
print(list1)

# remove() -> to delete specified element from position of first occurence

list1.remove(55)
print(list1)

# clear() -> to delete all elements from the list

list1.clear()

print(list1)
