import time
import datetime
from tkinter import *
import tkinter.messagebox 

root=Tk()
root.title("Employee payroll system")
root.geometry('1350x650+0+0')
root.configure(background="gold")

Tops=Frame(root,width=1350,height=50,bd=8,bg="azure")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=12,bg="white",relief="ridge")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=12,bg="sienna1",relief="groove")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=200,bd=8,bg="gray20")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="gray20")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('algerian',45,'bold'),text="Employee Payment Management system ",bd=12,bg="slateblue",fg="white",relief="ridge")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  wageshour.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Employer.set("")
  NINumber.set("")
  txtpayslip.delete("1.0",END)
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Employer :\t\t"+Employer.get()+"\n\n")
  txtpayslip.insert(END,"NI Number :\t\t"+NINumber.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n") 
def weeklywages():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(wageshour.get())
  
  paydue=wagesperhours*hoursworkedperweek
  paymentdue="INR",str('%.2f'%(paydue))
  Payable.set(paymentdue)
  
  tax=paydue*0.2
  taxable="INR",str('%.2f'%(tax))
  Taxable.set(taxable)
  
  netpay=paydue-tax
  netpays="INR",str('%.2f'%(netpay))
  NetPayable.set(netpays)
  
  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime="INR",str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs="INR",str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)  
  return  
    
#=============================== Variables ========================================================
Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OverTimeBonus=StringVar()
Employer=StringVar()
NINumber=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#================================ Label Widget =================================================

lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=0,column=0)
lblAddress=Label(fla,text="Address",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=0,column=2)
lblEmployer=Label(fla,text="Employer",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=1,column=0)
lblNINumber=Label(fla,text="NI Number",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=1,column=2)
lblHoursWorked=Label(fla,text="Hours Worked",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=2,column=0)
lblHourlyRate=Label(fla,text="Hourly Rate",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=2,column=2)
lblTax=Label(fla,text="Tax",font=('arial',16,'bold'),bd=20,anchor='w',fg="white",bg="gray20").grid(row=3,column=0)
lblOverTime=Label(fla,text="OverTime",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=3,column=2)
lblGrossPay=Label(fla,text="GrossPay",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=4,column=0)
lblNetPay=Label(fla,text="Net Pay",font=('arial',16,'bold'),bd=20,fg="white",bg="gray20").grid(row=4,column=2)

#=============================== Entry Widget =================================================

etxname=Entry(fla,textvariable=Name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxname.grid(row=0,column=1)

etxaddress=Entry(fla,textvariable=Address,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxaddress.grid(row=0,column=3)

etxemployer=Entry(fla,textvariable=Employer,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxemployer.grid(row=1,column=1)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxnin=Entry(fla,textvariable=NINumber,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxnin.grid(row=1,column=3)

etxgrosspay=Entry(fla,textvariable=Payable,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxgrosspay.grid(row=4,column=1)

etxnetpay=Entry(fla,textvariable=NetPayable,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxnetpay.grid(row=4,column=3)

etxtax=Entry(fla,textvariable=Taxable,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxtax.grid(row=3,column=1)

etxovertime=Entry(fla,textvariable=OverTimeBonus,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxovertime.grid(row=3,column=3)

#=============================== Text Widget ============================================================

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold'),fg="white",bg="sienna1").grid(row=0,column=0)
txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="white")
txtpayslip.grid(row=1,column=0)

#=============================== buttons ===============================================================

btnsalary=Button(flb,text='Weekly Salary',padx=16,pady=16,bd=10,font=('arial',16,'bold'),width=14,fg="white",bg="darkorchid",command=weeklywages).grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=16,pady=16,bd=10,font=('arial',16,'bold'),width=14,command=reset,fg="azure",bg="green4").grid(row=0,column=1)

btnpayslip=Button(flb,text='View Payslip',padx=16,pady=16,bd=10,font=('arial',16,'bold'),width=14,command=enterinfo,fg="azure",bg="purple").grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=10,font=('arial',16,'bold'),width=14,command=exit,fg="White",bg="red").grid(row=0,column=3)

root.mainloop()
