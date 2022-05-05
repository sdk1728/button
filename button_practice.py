from tkinter import *
root=Tk()
root.geometry("555x666")
frame=Frame(root,borderwidth=17,bg="blue",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
def NAME():
    print("SHUBHAM DIPAK KAMBLE")

def college():
    print("COLLEGE OF ENGINEERING PUNE")

def mobno():
    print("7972799088")

def dob():
    print("28th june 1998")
b1=Button(frame,fg="red",text="NAME", command= NAME, relief= GROOVE, font= "bold 17",bg="black")
b1.pack(padx=15,pady=15)

b2= Button(frame,fg="green",text="COLLEGE NAME",command= college,relief= GROOVE,bg="black",font="bold 17")
b2.pack(pady=15,padx=15)

b3=Button(frame,fg="blue",text="MOB NO",command=mobno, relief= GROOVE,bg="black",font="bold 17")
b3.pack(padx=15,pady=15,)

b4=Button(frame,fg="violet",text="DOB",command=dob, relief=GROOVE,bg="black",font="bold 17")
b4.pack(pady=15,padx=15)



root.mainloop()