from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
import tkinter.font as tkFont


class KonyvKartya:
    def __init__(self, cim, szerzo, kiado, isbn, kategoria):
        self.cim = cim
        self.szerzo = szerzo
        self.kiado = kiado
        self.isbn = isbn
        self.kategoria = kategoria


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
        self.szuro_legordulo = Combobox(self.kereso_kontener, textvariable=self.szuro_valtozo,
                                        values=self.szuro_opciok, width=15, state="readonly")
        self.szuro_legordulo.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.kereso_mezo = Entry(self.kereso_kontener, font=("Arial", 12), width=50)
        self.kereso_mezo.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        self.kereso_gomb = Button(self.kereso_kontener, text="Keresés",
                                  command=self.kereses_vegrehajtasa, font=("Arial", 12))
        self.kereso_gomb.grid(row=0, column=2, padx=10, pady=5, sticky=E)

        self.konyhozzaadas_gomb = Button(self.root, text="Könyv Hozzáadása", width=38, height=4,
                                         font=("Arial", 12), bg="#A8764D",
                                         command=self.konyhozzaadas)
        self.konyhozzaadas_gomb.pack(side=LEFT, padx=20, pady=10)

        self.konyv_kontener = Frame(self.root)
        self.konyv_kontener.pack(side=LEFT, padx=20, pady=10, fill=BOTH, expand=True)

        self.canvas = Canvas(self.konyv_kontener)
        self.scrollbar = Scrollbar(self.konyv_kontener, orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.konyvek = self.konyvek_betoltese('konyvek.txt')
        self.konyvkartyak_megjelenites()

    def konyvek_betoltese(self, fajlnev):
        konyvek = []
        try:
            with open("konyvek.txt", 'r', encoding='utf-8') as f:
                sorok = f.read().strip().split('\n')
                for sor in sorok:
                    adatok = sor.split(';')
                    if len(adatok) == 5:
                        konyv = KonyvKartya(adatok[2], adatok[3], adatok[1], adatok[0], adatok[4])
                        konyvek.append(konyv)
        except FileNotFoundError:
            messagebox.showerror("Hiba", f"A {fajlnev} fájl nem található!")
        return konyvek

    def konyvkartyak_megjelenites(self):
        for i, konyv in enumerate(self.konyvek):
            sor = i // 3
            oszlop = i % 3

            kartya_frame = Frame(self.scrollable_frame, relief=RAISED, borderwidth=1, width=400, height=300,
                                 bg="#D2B48C")
            kartya_frame.grid(row=sor, column=oszlop, padx=10, pady=10)
            kartya_frame.grid_propagate(False)

            cim_label = Label(kartya_frame, text=konyv.cim, font=("Arial", 14, "bold"), wraplength=380, bg="#D2B48C")
            cim_label.pack(pady=(10, 5))

            szerzo_label = Label(kartya_frame, text=f"Szerző: {konyv.szerzo}", font=("Arial", 12), bg="#D2B48C")
            szerzo_label.pack()

            kiado_label = Label(kartya_frame, text=f"Kiadó: {konyv.kiado}", font=("Arial", 12), bg="#D2B48C")
            kiado_label.pack()

            isbn_label = Label(kartya_frame, text=f"ISBN: {konyv.isbn}", font=("Arial", 12), bg="#D2B48C")
            isbn_label.pack()

            kategoria_label = Label(kartya_frame, text=f"Kategória: {konyv.kategoria}", font=("Arial", 12),
                                    bg="#D2B48C")
            kategoria_label.pack()

            gomb_frame = Frame(kartya_frame, bg="#D2B48C")
            gomb_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

            modositas_gomb = Button(gomb_frame, text="Módosítás", width=15)
            modositas_gomb.pack(side=LEFT, padx=5)

            torol_gomb = Button(gomb_frame, text="Törlés", width=15)
            torol_gomb.pack(side=RIGHT, padx=5)

    def kereses_vegrehajtasa(self):
        aktualis_szuro = self.szuro_valtozo.get()
        keresett_kifejezes = self.kereso_mezo.get()
        messagebox.showinfo("Keresés",
                            f"Keresési szűrő: {aktualis_szuro}\n"
                            f"Keresett kifejezés: {keresett_kifejezes}")

    def konyhozzaadas(self):
        hozzaadablak = Toplevel()
        hozzaadablak.title("Könyv Hozzáadása")
        hozzaadablak.maxsize(300, 450)
        hozzaadablak.minsize(300, 450)
        hozzaadablak.geometry("300x450")
        hozzaadablak.config(bg="#D3C2B2")

        cimLabel = Label(hozzaadablak, text="Cím: ")
        cimLabel.pack()
        cimEntry = Entry(hozzaadablak, width=100)
        cimEntry.pack(pady=10, padx=5)

        szerzoLabel = Label(hozzaadablak, text="Szerzö: ")
        szerzoLabel.pack()
        szerzoEntry = Entry(hozzaadablak, width=100)
        szerzoEntry.pack(pady=10, padx=5)

        kiadoLabel = Label(hozzaadablak, text="Kiadó: ")
        kiadoLabel.pack()
        kiadoEntry = Entry(hozzaadablak, width=100)
        kiadoEntry.pack(pady=10, padx=5)

        isbnLabel = Label(hozzaadablak, text="ISBN: ")
        isbnLabel.pack()
        isbnEntry = Entry(hozzaadablak, width=100)
        isbnEntry.pack(pady=10, padx=5)

        kategoriaLabel = Label(hozzaadablak, text="Kategória: ")
        kategoriaLabel.pack()
        kategoriaEntry = Entry(hozzaadablak, width=100)
        kategoriaEntry.pack(pady=10, padx=5)

        def hozzaadas():
            if not all([cimEntry.get(), szerzoEntry.get(), kiadoEntry.get(), isbnEntry.get(), kategoriaEntry.get()]):
                messagebox.showerror("Hiba", "Minden mezőt ki kell tölteni!")
                return
            try:
                ujkonyv = KonyvKartya(
                    cimEntry.get(),
                    szerzoEntry.get(),
                    kiadoEntry.get(),
                    isbnEntry.get(),
                    kategoriaEntry.get()
                )

                with open("konyvek.txt", 'a', encoding='utf-8') as f:
                    f.write(f" {isbnEntry.get()};{kiadoEntry.get()};{cimEntry.get()};{szerzoEntry.get()};{kategoriaEntry.get()}")

                for widget in self.scrollable_frame.winfo_children():
                    widget.destroy()
                self.konyvek.append(ujkonyv)
                self.konyvkartyak_megjelenites()

                hozzaadablak.destroy()

            except FileNotFoundError:
                messagebox.showerror("Hiba", "Ez a fájl nem található!")

        hozzaadasgomb = Button(hozzaadablak, text="HOZZÁADÁS", command=hozzaadas)
        hozzaadasgomb.pack(pady=30, padx=5)


    def futtat(self):
        self.root.mainloop()


def megnyitas():
    admin_ablak = AdminAblak("admin")
    admin_ablak.futtat()


if __name__ == "__main__":
    megnyitas()
