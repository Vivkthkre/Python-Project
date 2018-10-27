# import  modules
from tkinter import*
import random
import time
import datetime
import pyttsx3

# tkinter window
root=Tk()

#resolution of the Window
root.geometry("1600x800")

#title of the Window
root.title("Restaurant Management System")

#inserting a photo in tkinter window
photo = PhotoImage(file = "D:\\Python\\burger.png")
background_label = Label(root, image=photo)
background_label.place(x=0, y=0 )

text_Input=StringVar()

#global variables
operator=""
ttl=""

#Creating the Top Frame in the root
Tops=Frame(root, width=1600,height=70,bg="Purple",relief=GROOVE,bd=15)
Tops.pack(side=TOP)

#Creating Frame  f1 in the root
f1=Frame(root, width=800,height=700,bg="steelblue2",relief=GROOVE,bd=10)
f1.pack(side=LEFT)

#Creating Frame  f2 in the root
f2=Frame(root, width=300,height=700,bg="gray60",relief=RIDGE,bd=10)
f2.pack(side=RIGHT)

#=================================Time=========================================

time1 = ''
clock = Label(Tops, font=('arial', 20, 'bold'), bg='purple',fg='white',relief="raise",bd=10,anchor='w')

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%a %d %Y %I:%M:%S %p')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(500, tick)
tick()

#Label for the window
lblInfo=Label(Tops,font=('algerian',50,'bold'),text="18 Miles Food Court",fg="ghost white",bg="Purple",bd=30,relief="ridge",anchor='w')
lblInfo.grid(row=0,column=0)

clock.grid(row=1,column=0)
#================================Calculator====================================
def btnClick(numbers):
    global operator
    operator+=str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

txtDisplay = Entry(f2,font=('arail', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="palegreen3", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="7",bg="gray27",command=lambda:btnClick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="8",bg="gray27",command=lambda:btnClick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="9",bg="gray27",command=lambda:btnClick(9))
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',22,'bold'),text="+",bg="mediumorchid1",command=lambda:btnClick("+"))
Addition.grid(row=2,column=3)
#==============================================================================
btn4=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="4",bg="gray27",command=lambda:btnClick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="5",bg="gray27",command=lambda:btnClick(5))
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="6",bg="gray27",command=lambda:btnClick(6))
btn6.grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',22,'bold'),text="-",bg="mediumorchid1",command=lambda:btnClick("-"))
Subtraction.grid(row=3,column=3)
#==============================================================================
btn1=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="1",bg="gray27",command=lambda:btnClick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="2",bg="gray27",command=lambda:btnClick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="3",bg="gray27",command=lambda:btnClick(3))
btn3.grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',22,'bold'),text="*",bg="mediumorchid1",command=lambda:btnClick("*"))
Multiply.grid(row=4,column=3)
#===============================================================================
btn0=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="0",bg="gray27",command=lambda:btnClick(0))
btn0.grid(row=5,column=1)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="C",bg="deeppink3",command=btnClearDisplay)
btnClear.grid(row=5,column=0)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="=",bg="firebrick1",command=btnEqualsInput)
btnEquals.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="white",font=('arial',20,'bold'),text="/",bg="mediumorchid2")
Division.grid(row=5,column=3)
#================================Bill Calculation===============================

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if(Tea.get()==""):
        CoT=0
    else:
        CoT=float(Tea.get())

    if(Burger.get()==""):
        CoB=0
    else:
        CoB=float(Burger.get())

    if(Samosa.get()==""):
        CoS=0
    else:
        CoS=float(Samosa.get())

    if(IceCream.get()==""):
        CoI=0
    else:
        CoI=float(IceCream.get())

    if(Pulav.get()==""):
        CoP=0
    else:
        CoP=float(Pulav.get())

    if(Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

    CostofTea=CoT*10
    CostofBurger=CoB*30
    CostofSamosa=CoS*12
    CostofIceCream=CoI*20
    CostofPulav=CoP*50
    CostofDrinks=CoD*20

    Central_GST=(((CostofTea+CostofBurger+CostofSamosa+CostofIceCream+CostofPulav+CostofDrinks)*2.5)/100)

    State_GST=(((CostofTea+CostofBurger+CostofSamosa+CostofIceCream+CostofPulav+CostofDrinks)*2.5)/100)

    Total_cost=(CostofTea+CostofBurger+CostofSamosa+CostofIceCream+CostofPulav+CostofDrinks)

    CostofMeal='Rs',str('%.2f'%(CostofTea+CostofBurger+CostofSamosa+CostofIceCream+CostofPulav+CostofDrinks))

    C_gst='Rs',str('%.2f'%Central_GST)
    S_gst='Rs',str('%.2f'%State_GST)
    global ttl
    ttl=str('%.2f'%(Total_cost+Central_GST+State_GST))
    OverAllCost='Rs',str('%.2f'%(Total_cost+Central_GST+State_GST))

    Sgst.set(S_gst)
    Cost.set(CostofMeal)
    Cgst.set(C_gst)
    Total.set(OverAllCost)
    speechTotal()
              
def Reset():
    Tea.set("")
    Burger.set("")
    Samosa.set("")
    IceCream.set("")
    Pulav.set("")
    Drinks.set("")
    
    rand.set("")
    
    Cost.set("")
    Sgst.set("")
    Cgst.set("")
    Total.set("")
    
def qExit():
    root.destroy()

# speech
def speechTotal():
    engine= pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    #engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate' ,rate-40)
    engine.say('Total cost for your food is , ,'+ttl+'Rupees')
    engine.runAndWait()

# function for generating receipt
def Receipt():
    roor = Tk()
    roor.title("Receipt")
    roor.geometry("600x460+0+0")

    f1 = Frame(roor, width = 600, height = 460,bg="red2",bd = 20, relief = "ridge")
    f1.pack()
    
    lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=8,relief="raise", anchor='n')
    lblReceipt.grid(row=0, column=0,sticky=N)
    
    txtReceipt = Text(f1, width=67, height=20, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ rand.get() + '\t\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items                \t\t"+"Price of Item\n\n")
    txtReceipt.insert(END, 'Tea:\t\t\t\t\t' + Tea.get() + "\t\tRs 10\n")
    txtReceipt.insert(END, 'Drinks: \t\t\t\t\t' + Drinks.get() + "\t\tRs 20\n")
    txtReceipt.insert(END, 'IceCream: \t\t\t\t\t' + IceCream.get() + "\t\tRs 20\n")
    txtReceipt.insert(END, 'Burger: \t\t\t\t\t' + Burger.get() + "\t\tRs 50\n")
    txtReceipt.insert(END, 'Samosa: \t\t\t\t\t' + Samosa.get() + "\t\tRs 12\n")
    txtReceipt.insert(END, 'Rice-Plate: \t\t\t\t\t' + Pulav.get() + "\t\tRs 50\n")
    txtReceipt.insert(END, '\nTotal Cost of Food: \t\t\t\t' + Cost.get() + "\nCGST:\t\t\t\t" + Cgst.get() + "\nSGST:\t\t\t\t" + Sgst.get()+"\nTotal Payble amount:\t\t\t\t" + Total.get())
    
    roor.mainloop()

#================================Restauraunt Info1==================================

Tea=StringVar()
Burger=StringVar()
Samosa=StringVar()
IceCream=StringVar()
Pulav=StringVar()
Drinks=StringVar()
rand = StringVar()
Receipt_Ref=StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime('%d/%m/%y %I:%M:%S %p'))
Cost=StringVar()
Sgst=StringVar()
Cgst=StringVar()
Total=StringVar()

lblItems= Label(f1, font=('times', 20, 'bold'),text="    Items    ",fg="white",bg="gray10",bd=12,relief="ridge",anchor="n")
lblItems.grid(row=0, column=1)

lblTea= Label(f1, font=('arial', 16, 'bold'),text="Tea",bg="steelblue2",bd=16,anchor="w")
lblTea.grid(row=1, column=0)
lblTea=Entry(f1,font=('arial',16,'bold'),textvariable=Tea,bd=10,insertwidth=4,bg="white",justify='right')
lblTea.grid(row=1,column=1)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bg="steelblue2",bd=16,anchor="w")
lblDrinks.grid(row=2, column=0)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="white",justify='right')
txtDrinks.grid(row=2,column=1)

lblIceCream= Label(f1, font=('arial', 16, 'bold'),text="Ice-Cream",bg="steelblue2",bd=16,anchor="w")
lblIceCream.grid(row=3, column=0)
lblIceCream=Entry(f1, font=('arial',16,'bold'),textvariable=IceCream,bd=10,insertwidth=4,bg="white",justify='right')
lblIceCream.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bg="steelblue2",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="white",justify='right')
txtBurger.grid(row=4,column=1)

lblSamosa= Label(f1, font=('arial', 16, 'bold'),text="Samosa",bg="steelblue2",bd=16,anchor="w")
lblSamosa.grid(row=5, column=0)
txtSamosa=Entry(f1, font=('arial',16,'bold'),textvariable=Samosa,bd=10,insertwidth=4,bg="white",justify='right')
txtSamosa.grid(row=5,column=1)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Rice-Plate",bg="steelblue2",bd=16,anchor="w")
lblPulav.grid(row=6, column=0)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="white",justify='right')
txtPulav.grid(row=6,column=1)
#==============================BillInfo==========================================
billdetail= Label(f1, font=('times', 20, 'bold'),text="       Bill Details       ",fg="white",bg="gray10",relief="ridge",bd=12,anchor="w")
billdetail.grid(row=0, column=3)

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bg="steelblue2",bd=16,anchor="w")
lblReference.grid(row=1, column=2)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=1,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bg="steelblue2",bd=16,anchor="w")
lblCost.grid(row=2, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=2,column=3)


lblSgst= Label(f1, font=('arial', 16, 'bold'),text="SGST",bg="steelblue2",bd=16,anchor="w")
lblSgst.grid(row=3, column=2)
txtSgst=Entry(f1, font=('arial',16,'bold'),textvariable=Sgst,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSgst.grid(row=3,column=3)


lblCgst= Label(f1, font=('arial', 16, 'bold'),text="CGST",bg="steelblue2",bd=16,anchor="w")
lblCgst.grid(row=4, column=2)
txtCgst=Entry(f1, font=('arial',16,'bold'),textvariable=Cgst,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCgst.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bg="steelblue2",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="khaki",justify='right')
txtTotalCost.grid(row=5,column=3)
#==============================Buttons===========================================

btnReciept=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial', 16, 'bold'),width=10,text="Receipt",bg="sandybrown",command=Receipt).grid(row=7,column=0)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial', 16, 'bold'),width=10,text="Total",bg="chartreuse3",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial', 16, 'bold'),width=10,text="Reset",bg="gold2",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial', 16, 'bold'),width=10,text="Exit",bg="red3",command=qExit).grid(row=7,column=3)
#==============================Welcome Speech====================================
def speechWelcome():
    engine= pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate' ,rate-45)
    engine.say('Welcome to 18 Miles food court.')
    engine.runAndWait()
speechWelcome()

#End the loop
root.mainloop()






