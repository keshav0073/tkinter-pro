from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def newfile():
	global file
	root.title("kunnu-notepad")
	file=None
	TextArea.delete(1.0,END)

def openfile():
	global file
	file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
	if file=="":
		file=None
	else:
		root.title(os.path.basename(file) + "- notepad")
		TextArea.delete(1.0,END)
		f=open(file,"r")
		TextArea.insert(1.0,f.read())
		f.close()

def save():
	global file
	if file==None:
		file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if file=="":
			file=None
		else:
			#save as a new file
			f=open(file,"w")
			f.write(TextArea.get(1.0,END))
			f.close()

			root.title(os.path.basename(file) + "- notepad")
			print("file saved")

	else:
		#save the file
		f=open(file,"w")
		f.write(TextArea.get(1.0,END))
		f.close()





def cut():
	TextArea.event_generate(("<<Cut>>"))

def copy():
	TextArea.event_generate(("<<Copy>>"))

def paste():
	TextArea.event_generate(("<<Paste>>"))

def about():
	showinfo("kunnu-notepad","made by keshav")

if __name__ == '__main__':
	#basic tkinter setup
	root=Tk()
	root.title("kunnu-notepad")
	root.geometry("644x788")

	#add textarea
	TextArea=Text(root,font="chiller 12 bold")
	file=None
	TextArea.pack(fill=BOTH,expand=True)
	#add menu
	menu=Menu(root)
	#to start filemenu
	filemenu=Menu(menu,tearoff=0)
	#to open new file
	filemenu.add_command(label="new", command=newfile)
	#to open already existing file
	filemenu.add_command(label="open",command=openfile)
	#to save currnt file
	filemenu.add_command(label="save",command=save)
	filemenu.add_separator()
	filemenu.add_command(label="exit",command=exit)
	menu.add_cascade(label="file",menu=filemenu)
	#end filemenu
	#to start edit menu
	editmenu=Menu(menu,tearoff=0)
	editmenu.add_command(label="cut", command=cut)
	editmenu.add_command(label="copy", command=copy)
	editmenu.add_command(label="paste", command=paste)
	menu.add_cascade(label="edit",menu=editmenu)

	#end edit menu
	#to help start
	helpmenu=Menu(menu,tearoff=0)
	helpmenu.add_command(label="about",command=about)
	menu.add_cascade(label="about",menu=helpmenu)

	#end help end
	root.config(menu=menu)
	#adding scrollbar
	Scroll=Scrollbar(TextArea)
	Scroll.pack(fill="y",side="right")
	Scroll.config(command=TextArea.yview)
	TextArea.config(yscrollcommand=Scroll.set)



	root.mainloop()