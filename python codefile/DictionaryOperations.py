'''Removing elements from Dict-
    1- pop()-  used to delete element with specified key         (problem - no indexing)
            - only one key can pass.

                 syntax- dictname.pop(key) 
                 #if we do not specify the key then type error(pop expected at least 1 argument,got0).
     ------ student.popitem() - used to delete last key pair value

  METHODS - keys()= it will return a list of keys of all the element of dictionary.
                    --syntax- listvar=dictname.keys()
          - values()= it will return a list of all the values of all the elements of dictionary
                     --syntax- listvar = dictname.values()
          -items() =  it will returns a list of items(each item will be in the form of tuple with two mwmbers (i.e. key - value)
                      --syntax- var=dictname.items()
-clear() - remove all the elements of dict
-copy() - return a copy of a dict
- fromkeys() - return a dict with specfied keys and values     (syntax- dict.fromkeys(key,value))
- get() - return specfied key
-len() -  return lenghth of dict

--------------------------update() - update  or insert multiple elements (in  the key-value pair) in the dict.
                                               syntax - dict1.update(dict2)'''


dic1 = {'name': 'alok', 'age': 17, 'standard': '12th'}
dic2 = {'hindi': 68, 'age': 15, 'standard': '7th', 'english': 88}

# Accessing values
print(dic1['name'])
print(dic2['hindi'])

# Adding or updating values
dic1['math'] = 95
dic2['age'] = 16

# Deleting a key-value pair
del dic1['standard']

# Checking if a key exists
print('name' in dic1)
print('science' in dic2)

# Iterating over dictionary keys
for key in dic1:
    print(key)

# Iterating over dictionary values
for value in dic2.values():
    print(value)

# Iterating over dictionary items
for key, value in dic1.items():
    print(key, value)

# Getting a value with a default
math_score = dic2.get('math', 50)
print(math_score)

# Merging two dictionaries 
dic3 = dic1 | dic2
print(dic3)

# Using fromkeys to create a new dictionary with default values
keys = ['name', 'age', 'grade']
new_dic = dict.fromkeys(keys, 0)
print(new_dic)

# Clearing all items from a dictionary
dic1.clear()
print(dic1)

# Copying a dictionary
dic4 = dic2.copy()
print(dic4)
