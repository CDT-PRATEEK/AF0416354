list1 = [1,2,3,4,55,'hello', 67 , 99, 88 ,661 ,2,3,4,55,'hello', 67 , 99, 88 ,66 ,77]

print("elements in backward direction using forward index: ")

print(list1[20::-1])

print("--------------------------------------")


for i in range(len(list1)-1,0,-1):
    print(list1[i] , end =",")

print("--------------------------------------")

list2= ['a','b','c','d','e']

list1.append(list2)

print(list1, end="\n")

print("--------------------------------------\n")

# extend() -> to insert all elements of any sequence datatype at end of the list

#syntax-> 

list1.extend(list2)

print(list1)

print("--------------------------------------")

# insert() -> to insert element at specified index

list1.insert(0 ,69)             #list.insert(index , value)

print(list1)

print("--------------------------------------")

# find a methiod to insert all the elements of another sequence datatype at a particular index in the list,
# but all the elements must be inserted one by one 

list3 =[1,2,3,4]

list2[2:3] = list3

print(list3)


   