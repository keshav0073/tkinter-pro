from tkinter import *

def click(event):
	global value
	text=event.widget.cget("text")
	print(text)
	if text == "=":
		if value.get().isdigit():
			svalue=int(value.get())
		else:
			svalue=eval(screen.get())
		value.set(svalue)
		screen.update()

	elif text=="c":
		value.set("")
		screen.update()
	else:
		value.set(value.get() + text)
		screen.update()



if __name__ == '__main__':
	root=Tk()
	root.geometry("644x900")
	root.title("kunnu-cal")
	root.configure(background="black")

	value=StringVar()
	value.set("")
	screen=Entry(root,textvar=value,font="lucida 40 bold")
	screen.pack(fill="x",ipadx=10,pady=4,padx=10)
	#frame
	f=Frame(root,bg="red")
	f.pack()

	b=Button(f,text="9",font="lucida 35 bold",padx="22",pady="8")
	b.pack(side="left",padx=18,pady=1)
	b.bind("<Button-1>",click)

	b1=Button(f,text="8",font="lucida 35 bold",padx="22",pady="8")
	b1.pack(side="left",padx=18,pady=1)
	b1.bind("<Button-1>",click)


	b2=Button(f,text="7",font="lucida 35 bold",padx="22",pady="8")
	b2.pack(side="left",padx=18,pady=1)
	b2.bind("<Button-1>",click)

	#f2
	f=Frame(root,bg="red")
	f.pack()

	b=Button(f,text="6",font="lucida 35 bold",padx="22",pady="8")
	b.pack(side="left",padx=18,pady=1)
	b.bind("<Button-1>",click)

	b1=Button(f,text="5",font="lucida 35 bold",padx="22",pady="8")
	b1.pack(side="left",padx=18,pady=1)
	b1.bind("<Button-1>",click)


	b2=Button(f,text="4",font="lucida 35 bold",padx="22",pady="8")
	b2.pack(side="left",padx=18,pady=1)
	b2.bind("<Button-1>",click)

	#f3
	f=Frame(root,bg="red")
	f.pack()

	b=Button(f,text="3",font="lucida 35 bold",padx="22",pady="8")
	b.pack(side="left",padx=18,pady=1)
	b.bind("<Button-1>",click)

	b1=Button(f,text="2",font="lucida 35 bold",padx="22",pady="8")
	b1.pack(side="left",padx=18,pady=1)
	b1.bind("<Button-1>",click)


	b2=Button(f,text="1",font="lucida 35 bold",padx="22",pady="8")
	b2.pack(side="left",padx=18,pady=1)
	b2.bind("<Button-1>",click)

	#f4
	f=Frame(root,bg="red")
	f.pack()

	b=Button(f,text="0",font="lucida 35 bold",padx="31",pady="8")
	b.pack(side="left",padx=18,pady=1)
	b.bind("<Button-1>",click)

	b1=Button(f,text="-",font="lucida 35 bold",padx="22",pady="8")
	b1.pack(side="left",padx=18,pady=1)
	b1.bind("<Button-1>",click)


	b2=Button(f,text="*",font="lucida 35 bold",padx="22",pady="8")
	b2.pack(side="left",padx=18,pady=1)
	b2.bind("<Button-1>",click)

	f=Frame(root,bg="red")
	f.pack()

	b=Button(f,text="/",font="lucida 35 bold",padx="20",pady="12")
	b.pack(side="left",padx=18,pady=5)
	b.bind("<Button-1>",click)

	b1=Button(f,text="%",font="lucida 35 bold",padx="22",pady="12")
	b1.pack(side="left",padx=18,pady=5)
	b1.bind("<Button-1>",click)


	b2=Button(f,text="=",font="lucida 35 bold",padx="22",pady="12")
	b2.pack(side="left",padx=18,pady=5)
	b2.bind("<Button-1>",click)

	f=Frame(root,bg="red")
	f.pack()

	b=Button(f,text="c",font="lucida 35 bold",padx="20",pady="12")
	b.pack(side="left",padx=18,pady=5)
	b.bind("<Button-1>",click)

	b1=Button(f,text=".",font="lucida 35 bold",padx="22",pady="12")
	b1.pack(side="left",padx=18,pady=5)
	b1.bind("<Button-1>",click)


	b2=Button(f,text="+",font="lucida 35 bold",padx="22",pady="12")
	b2.pack(side="left",padx=18,pady=5)
	b2.bind("<Button-1>",click)






	root.mainloop()