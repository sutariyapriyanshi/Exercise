from currency_converter import CurrencyConverter # currentconverter is the module in python
import tkinter as tk # tkinter is used for the new window animation or GUI o/p
a=CurrencyConverter() # take a for to convert

# print(a.convert(12,"USD","INR"))
def clicked(): # for click use this function is used
    amount=int(e1.get()) # take amount as the input in integer e1 is for the integer number value
    cur1=e2.get() # cur1 variable is used for the currency 1 which your input currency is in which form
    cur2=e3.get() # required currency or desire currency
    data=a.convert(amount,cur1,cur2)  # data is used for the final answer which will accomplish the whole cur1 amount and cur2
    l5=tk.Label(window,text=data,font="Times 20 bold").place(x=70,y=350) #this label is for to print the final answer 
    # the final answer is in bold and size of the font is 20 and place is used for to place the value at at x axis 70 and y axis 350

window=tk.Tk() # tk is used for tkinter use window (Tk -> it is the moethod used in tkinter)
window.geometry("1000x600") # window size of the o/p is the 1000 x 600
l1=tk.Label(window,text="Currency Converter", font="Times 40 bold").place(x=300,y=30) # l1 is also label
l2=tk.Label(window,text="Enter your Amount here: ",font="Times 20 bold").place(x=70,y=100)
e1=tk.Entry(window) # it is generate a text field for to enter the input for the user in o/p

l3=tk.Label(window,text="Enter Currency: ",font="Times 20 bold").place(x=70,y=150)
e2=tk.Entry(window) # Entry is used for enter in the o/p window

l4=tk.Label(window,text="Enter Required Currency: ",font="Times 20 bold").place(x=70,y=200) # font is used to give the which font you have 
# to give and what is the size of your font
e3=tk.Entry(window)

b1=tk.Button(window,text="Click",font="Times 20 bold",command=clicked).place(x=70,y=250) # this b1 variable is used for crwating the button
e1.place(x=380,y=112) # for placing the at which you have to put your input
e2.place(x=280,y=162)
e3.place(x=400,y=212)
window.mainloop() # it will the mainloop of your window
# a=CurrencyConverter()

# print(a.convert(12,"USD","INR"))
