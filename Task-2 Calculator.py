from tkinter import *
def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnClear():
    global val
    val=""
    data.set("")
def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)
root = Tk()
root.title("Calculator by Sailatha")
root.geometry("361x381+500+200")
val=""
data=StringVar()
display=Entry(root, textvariable=data,bd=29,justify="right",bg="powder Blue", font=("lucida 30 bold" ))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#E3C614",height=2,width=6,command=lambda:btnClick('+'))   
btn_add.grid(row=1,column=3)

display.grid(row=0,columnspan=4)
btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#38C41D",height=2,width=6,command=lambda:btnClick('-'))
btn_sub.grid(row=2,column=3)

display.grid(row=0,columnspan=4)

btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#38C41D",height=2,width=6,command=lambda:btnClick('*'))
btn_mul.grid(row=3,column=3)

btnc=Button(root,text="C",font=("Ariel",12,"bold"),bd=12,fg="#fff",bg="#3697f5",height=2,width=6,command=btnClear)
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0))
btn0.grid(row=4,column=1)
btn_div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#D62BC0",height=2,width=6,command=lambda:btnClick('/'))
btn_div.grid(row=4,column=2)
btn_decimal=Button(root,text=".",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#D62BC0",height=2,width=6,command=lambda:btnClick('.'))
btn_decimal.grid(row=4,column=3)
btn_mod=Button(root,text="%",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#FF980F",height=2,width=6,command=lambda:btnClick('%'))
btn_mod.grid(row=5,column=0)


btn_openbrace=Button(root,text="(",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#FF980F",height=2,width=6,command=lambda:btnClick('('))
btn_openbrace.grid(row=5,column=1)
btn_closebrace=Button(root,text=")",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#FF980F",height=2,width=6,command=lambda:btnClick(')'))
btn_closebrace.grid(row=5,column=2)

btn_equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,fg="#0D0D0D",bg="#1D28C4",height=2,width=6,command=btnEquals)
btn_equal.grid(row=5,column=3)





              
root.mainloop()
