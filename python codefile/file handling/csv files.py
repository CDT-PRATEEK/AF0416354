import csv

f = open("anudip.csv" ,'a')                     # writing csv

wo = csv.writer(f)
data = [['a','b','c','d'], [1,2,3,4,5],[6,7,8,9,10]]
wo.writerows(data)
f.close()




f = open("anudip.csv",'r')                      # reading csv
re = csv.reader(f)
li = list(re)
for row in li:
    print(row)
