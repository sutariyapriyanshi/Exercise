from currency_converter import CurrencyConverter
import tkinter as tk
a=CurrencyConverter()

# print(a.convert(12,"USD","INR"))
def clicked():
    amount=int(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data=a.convert(amount,cur1,cur2) 
    l5=tk.Label(window,text=data,font="Times 20 bold").place(x=70,y=350)

window=tk.Tk()
window.geometry("1000x600")
l1=tk.Label(window,text="Currency Converter", font="Times 40 bold").place(x=300,y=30)
l2=tk.Label(window,text="Enter your Amount here: ",font="Times 20 bold").place(x=70,y=100)
e1=tk.Entry(window)

l3=tk.Label(window,text="Enter Currency: ",font="Times 20 bold").place(x=70,y=150)
e2=tk.Entry(window)

l4=tk.Label(window,text="Enter Required Currency: ",font="Times 20 bold").place(x=70,y=200)
e3=tk.Entry(window)

b1=tk.Button(window,text="Click",font="Times 20 bold",command=clicked).place(x=70,y=250)
e1.place(x=380,y=112)
e2.place(x=280,y=162)
e3.place(x=400,y=212)
window.mainloop()
# a=CurrencyConverter()

# print(a.convert(12,"USD","INR"))
