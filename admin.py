from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo


class AdminAblak:
    def __init__(self, jogosultsag):
        self.jogosultsag = jogosultsag
        self.root = Tk()
        self.root.title(f"Könyv Kezelési app {jogosultsag}-ként")
        self.root.config(bg="#895F3A")
        self.root.minsize(1500, 1000)
        self.root.maxsize(1500, 1000)
        self.root.geometry('1500x1000')

        self.kereso_kontener = Frame(self.root, bg="#A8764D")
        self.kereso_kontener.pack(fill=X, padx=20, pady=10)
        self.kereso_kontener.grid_columnconfigure(1, weight=1)

        self.szuro_opciok = ['Cím', 'Szerző', 'Kiadó', 'ISBN', 'Kategória']
        self.szuro_valtozo = StringVar(value=self.szuro_opciok[0])
        self.szuro_legordulo = Combobox(self.kereso_kontener, textvariable=self.szuro_valtozo,values=self.szuro_opciok, width=15, state="readonly")
        self.szuro_legordulo.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.kereso_mezo = Entry(self.kereso_kontener, font=("Arial", 12), width=50)
        self.kereso_mezo.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        self.kereso_gomb = Button(self.kereso_kontener, text="Keresés", command=self.kereses_vegrehajtasa, font=("Arial", 12))
        self.kereso_gomb.grid(row=0, column=2, padx=10, pady=5, sticky=E)

        self.konyhozzaadas_gomb = Button(self.root, text="Könyv Hozzáadása", width=38, height=4,font=("Arial", 12), bg="#A8764D", command=self.konyhozzaadas)
        self.konyhozzaadas_gomb.pack(side=LEFT, padx=20, pady=10)

    def kereses_vegrehajtasa(self):
        aktualis_szuro = self.szuro_valtozo.get()
        keresett_kifejezes = self.kereso_mezo.get()
        messagebox.showinfo("Keresés", f"Keresési szűrő: {aktualis_szuro}\n"f"Keresett kifejezés: {keresett_kifejezes}")

    def konyhozzaadas(self):
        showinfo("Test")

    def futtat(self):
        self.root.mainloop()


def megnyitas():
    admin_ablak = AdminAblak("admin")
    admin_ablak.futtat()


if __name__ == "__main__":
    megnyitas()


