from tkinter import *
import os
def reg_user():
	username_info=username.get()
	password_info=password.get()
	
	existing_user=os.listdir()
	if username_info in existing_user:
		Label(screen2,text=os.getcwd()).pack()
	else:
		file=open(username_info,"w")
		file.write(username_info+"\n")
		file.write(password_info)
		file.close()

		Label(screen2, text="Register Succesfully", bg="green").pack()
	


def destroy4():
	screen4.destroy()

def destroy5():
	screen5.destroy()

def destroy6():
	screen6.destroy()

def save():
	new_file1=new_file.get()
	notes1=notes.get()

	data=open(new_file1,"w")
	data.write(notes1)
	data.close()

	Label(screen8,text="Saved").pack()

def view():
	screen10=Toplevel(screen1)
	screen10.title("View")
	screen10.geometry("300x200")
	openfile1=openfile.get()
	data1=open(openfile1,"r")
	data2=data1.read()
	Label(screen10,text=data2).pack()


def delete():
	deletefile1=deletefile.get()
	os.remove(deletefile1)
	screen12=Toplevel(screen1)
	screen12.title("Delete")
	screen12.geometry("300x200")
	Label(screen12,text="Note is deleted").pack()

def NEW():
	global screen8
	screen8=Toplevel(screen1)
	screen8.title("Dashboard")
	screen8.geometry("300x200")

	global new_file
	new_file=StringVar()
	global notes
	notes=StringVar()

	Label(screen8, text="Enter note name").pack()
	Entry(screen8, textvariable=new_file).pack()
	Label(screen8, text="Note").pack()
	Entry(screen8, textvariable=notes).pack()

	Button(screen8, text="Save", command=save).pack()


def OPEN():
	screen9=Toplevel(screen1)
	screen9.title("Dashboard")
	screen9.geometry("300x200")
	allfile=os.listdir()
	global openfile
	openfile=StringVar()
	Label(screen9, text="Existing File are").pack()
	Label(screen9, text=allfile).pack()
	Label(screen9, text="wtite").pack()
	Entry(screen9, textvariable=openfile).pack()
	Button(screen9, text="open", command=view).pack()


def DEL():
	screen11=Toplevel(screen1)
	screen11.title("Delete  Notes")
	screen11.geometry("300x200")
	allfile=os.listdir()
	global deletefile
	deletefile=StringVar()
	Label(screen11, text="Existing File are").pack()
	Label(screen11, text=allfile).pack()
	Label(screen11, text="Delete").pack()
	Entry(screen11, textvariable=deletefile).pack()
	Button(screen11, text="delete", command=delete).pack()


def session():
	screen7=Toplevel(screen1)
	screen7.title("Dashboard")
	screen7.geometry("300x200")
	Label(screen7,text="Welcome to Dashboard").pack()
	Button(screen7, text="NEW",command=NEW).pack()
	Button(screen7, text="OPEN",command=OPEN).pack()
	Button(screen7, text="DEL",command=DEL).pack()


def login_sucess():
	global screen4
	screen4=Toplevel(screen1)
	screen4.title("Login Sucess")
	screen4.geometry("300x200")
	Label(screen4, text="Login Sucess").pack()
	Button(screen4, text="OK", command=session).pack()

def passnot():
	global screen5
	screen5=Toplevel(screen1)
	screen5.title("PNM")
	screen5.geometry("300x200")
	Label(screen5, text="Password not matched").pack()
	Button(screen5, text="OK", command=destroy5).pack()

def usernot():
	global screen6
	screen6=Toplevel(screen1)
	screen6.title("UNM")
	screen6.geometry("300x200")
	Label(screen6, text="Username not matched").pack()
	Button(screen6, text="OK", command=destroy6).pack()


def login_verify():
	username1=username_verify.get()
	password1=password_verify.get()

	list_of_files=os.listdir()
	if username1 in list_of_files:
		file1=open(username1,"r")
		verify=file1.read().splitlines()
		if password1 in verify:
			login_sucess()
		else:
			passnot()
	else:
		usernot()



def Register():
	global screen2
	screen2 = Toplevel(screen1)
	screen2.title("Register")
	screen2.geometry("300x200")

	global username
	global password
	username=StringVar()
	password=StringVar()

	Label(screen2, text="Please Enter the details below").pack()
	Label(screen2, text="").pack()
	Label(screen2, text="Username *").pack()
	Entry(screen2, textvariable=username).pack()
	Label(screen2, text="password *").pack()
	Entry(screen2, textvariable=password).pack()
	Label(screen2, text="").pack()
	Button(screen2, text="Register",command=reg_user).pack()


def Login():
	global screen3
	screen3=Toplevel(screen1)
	screen3.title("Login")
	screen3.geometry("300x200")

	global username_verify
	global password_verify
	username_verify=StringVar()
	password_verify=StringVar()

	Label(screen3, text="Please Enter the details below for login").pack()
	Label(screen3, text="").pack()
	Label(screen3, text="Username *").pack()
	Entry(screen3, textvariable=username_verify).pack()
	Label(screen3, text="password *").pack()
	Entry(screen3, textvariable=password_verify).pack()
	Label(screen3, text="").pack()
	Button(screen3, text="Login",command=login_verify).pack()



def main_screen():
	global screen1
	screen1 = Tk()
	screen1.geometry("300x200")
	screen1.title("Test")
	screen1.configure(bg='blue')
	Label(text="Test", bg="yellow", width="300", height="5").pack()
	Label(text="").pack()
	Button(text="Login", command=Login).pack()
	Label(text="").pack()
	Button(text="Register",command=Register).pack()
	screen1.mainloop()

main_screen()