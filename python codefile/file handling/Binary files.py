# pickle module is used to read and write from binary files.

import pickle

f = open("anudip.dat" , 'wb')
li = [10,20,30,40,50]
pickle.dump(li , f)   # write
f.close()




# read in binary files

f = open("anudip.dat" , 'rb')
data = pickle.load(f)
print(data)
f.close()





