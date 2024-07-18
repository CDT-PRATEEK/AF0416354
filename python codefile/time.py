time = int(input("Time in Seconds: "))

if(time >= 3600 ):

    hours = str(time//3600)
    rem_time = time % 3600
    
    min = str(rem_time//60)
    
    sec = str(rem_time %60)
    
    print(hours+ "hours" , min , "minutes" , sec , "Seconds")
    
elif(time >=60):
    
    min = str(time//60)
    
    sec = str(time % 60)
    
    print( min , "minutes" , sec , "Seconds")
    
elif(time>0):
    
    sec = str(time)
    
    print( sec , "Seconds")
    
else:
    
    print("error")
    
     # type: ignore