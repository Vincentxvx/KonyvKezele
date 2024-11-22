from tkinter import *
from random import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

root = Tk()
root.title("Mini közösségi app")
root.config(bg="#48CFCB")
root.minsize(500, 200)
root.maxsize(500, 200)
root.geometry('500x200')



test = Label(root,text="Test")

def admin():
    adminwindow = Toplevel()
    adminwindow.geometry("1000x750")
    adminwindow.minsize(1000, 750)
    adminwindow.maxsize(1000, 750)
    adminwindow.config(bg="#424242")
    adminwindow.title("User Profile")
    test = Label(adminwindow,text="test")
    test.place(relx=0.5, rely=0.5)
    # KERESŐ

    kereso = Frame(adminwindow, width=1000, height=100) 
    kereso.place(relx=0.5, rely=0, anchor=N)
    beiro = Entry(kereso, width=25, bg="white", font=("Calibri",25))
    beiro.place(relx=0.5, rely=0.3, anchor=N)
    gombkereso = Button(kereso, text="keresés")
    gombkereso.place(rely=0.3, relx=0.74, anchor=N, height=44)
    szuro = Combobox()


gomb = Button(text="CLICKME", command=admin)
gomb.place(relx=0.5, rely=0.5, anchor=N)
root.mainloop()