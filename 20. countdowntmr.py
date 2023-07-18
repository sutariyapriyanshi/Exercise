import time # imprting the time module

def countdown(sec): # creating the class for the countdown name as also countdown and passing the sec argument
    while sec: # for the sec do this loop iterating
        mins,secs = divmod(sec,60) # take mins and secs for the o/p and do divmod mins will return the quoitant and secs will return the remainder of your value 
        time_format="{:02d}:{:02d}".format(mins,secs) # floor division minutes is quoitant and second is remainder
        # format of the countdown timer is in minutes and seconds with {:02d} means to two values
        print(time_format) # print time_format 
        time.sleep(1) # with the sleep of the 1 second
        sec-=1 # at all time decrease the value of second with the 1 second
obj=countdown(61) # take countdown values in the from of the second
print("Stop") # after loop will complete print stop at last
