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
    def keres(filter, beiro):
        val = filter.get()
        val2 = beiro.get()
        test.config(text=val2)
        with open("./konyvek.txt", 'r', encoding='utf-8') as file:
            for line in file:
                attributes = line.strip().split(';')
                isbn, kiado, cim, szerzo, mufaj = attributes
                match val:
                    case "ISBN":
                        if val2 == isbn:
                            print(f"ISBN: {isbn}")
                            print(f"Kiadó: {kiado}")
                            print(f"Cím: {cim}")
                            print(f"Szerző: {szerzo}")
                            print(f"Műfaj: {mufaj}")
                            print("-" * 40)   
                    case "Kiadó":
                        if val2 == kiado:
                            print(f"ISBN: {isbn}")
                            print(f"Kiadó: {kiado}")
                            print(f"Cím: {cim}")
                            print(f"Szerző: {szerzo}")
                            print(f"Műfaj: {mufaj}")
                            print("-" * 40)   
                    case "Cím":
                        if val2 == cim:
                            print(f"ISBN: {isbn}")
                            print(f"Kiadó: {kiado}")
                            print(f"Cím: {cim}")
                            print(f"Szerző: {szerzo}")
                            print(f"Műfaj: {mufaj}")
                            print("-" * 40)   
                    case "Szerző":
                        if val2 == szerzo:
                            print(f"ISBN: {isbn}")
                            print(f"Kiadó: {kiado}")
                            print(f"Cím: {cim}")
                            print(f"Szerző: {szerzo}")
                            print(f"Műfaj: {mufaj}")
                            print("-" * 40)   
                    case "Műfaj":
                        if val2 == mufaj:
                            print(f"ISBN: {isbn}")
                            print(f"Kiadó: {kiado}")
                            print(f"Cím: {cim}")
                            print(f"Szerző: {szerzo}")
                            print(f"Műfaj: {mufaj}")
                            print("-" * 40)   


    adminwindow = Toplevel()
    adminwindow.geometry("1000x750")
    adminwindow.minsize(1000, 750)
    adminwindow.maxsize(1000, 750)
    adminwindow.config(bg="#424242")
    adminwindow.title("User Profile")

    # KERESŐ

    kereso = Frame(adminwindow, width=1000, height=100) 
    kereso.place(relx=0.5, rely=0, anchor=N)
    beiro = Entry(kereso, width=25, bg="white", font=("Calibri",25))
    beiro.place(relx=0.5, rely=0.3, anchor=N)
    gombkereso = Button(kereso, text="keresés", command=lambda: keres(filter, beiro))
    gombkereso.place(rely=0.3, relx=0.76, anchor=N, height=44)
    n = StringVar()
    filter = ttk.Combobox(kereso, height=44, width=8, textvariable=N)
    filter ["values"] = ("ISBN", "Kiadó", "Cím", "Szerző", "Műfaj")
    filter.place(rely = 0.4, relx = 0.23, anchor = N)


    test = Label(adminwindow,text="test")
    test.place(relx=0.5, rely=0.5)




gomb = Button(text="CLICKME", command=admin)
gomb.place(relx=0.5, rely=0.5, anchor=N)
root.mainloop()