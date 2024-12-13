from tkinter import *
from random import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage


class AdminAblak:
    def __init__(self, jogosultsag):
        self.jogosultsag = jogosultsag
        self.root = Tk()
        self.root.title(f"Köny Kezelési app {jogosultsag}-ként")
        self.root.config(bg="#895F3A")
        self.root.minsize(1500, 1000)
        self.root.maxsize(1500, 1000)
        self.root.geometry('1500x1000')
        self.root.mainloop()

def megynitas():
    AdminAblak("admin")

megynitas()
