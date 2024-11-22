import tkinter as tk
from tkinter import messagebox
import os


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Könyvtár Bejelentkezés")
        self.root.geometry("300x250")

        self.users_file = 'users.txt'

        # Képzeljünk el két gombot: Admin és Felhasználó bejelentkezéshez
        self.login_as_label = tk.Label(root, text="Válaszd ki a bejelentkezés típusát", font=("Arial", 12))
        self.login_as_label.pack(pady=10)

        self.admin_button = tk.Button(root, text="Bejelentkezés Adminisztrátorként", width=30, command=self.login_as_admin)
        self.admin_button.pack(pady=5)

        self.user_button = tk.Button(root, text="Bejelentkezés Felhasználóként", width=30, command=self.login_as_user)
        self.user_button.pack(pady=5)

    def login_as_admin(self):
        self.login_window('admin')

    def login_as_user(self):
        self.login_window('user')

    def login_window(self, user_type):
        # Új ablak nyílik, ahol meg kell adni a felhasználónevet és a jelszót
        login_win = tk.Toplevel(self.root)
        login_win.title(f"Bejelentkezés {user_type.capitalize()}ként")
        login_win.geometry("300x200")

        # Felhasználó név
        tk.Label(login_win, text="Felhasználónév: ").pack(pady=5)
        username_entry = tk.Entry(login_win)
        username_entry.pack(pady=5)

        # Jelszó
        tk.Label(login_win, text="Jelszó:").pack(pady=5)
        password_entry = tk.Entry(login_win, show="*")
        password_entry.pack(pady=5)

        def check_login():
            username = username_entry.get()
            password = password_entry.get()
            if self.check_credentials(username, password, user_type):
                messagebox.showinfo("Sikeres bejelentkezés", "Sikeresen bejelentkeztél!")
                login_win.destroy()
                self.open_library_window(user_type)
            else:
                messagebox.showerror("Hiba", "Sikertelen bejelentkezés! Ellenőrizd a felhasználónevet és jelszót.")

        # Bejelentkezés gomb
        login_button = tk.Button(login_win, text="Bejelentkezés", command=check_login)
        login_button.pack(pady=10)

    def check_credentials(self, username, password, user_type):
        # Ellenőrizzük a felhasználót és jelszót a fájlban
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                for line in file:
                    stored_user, stored_pass = line.strip().split(':')
                    # Ha adminisztrátorként próbálkozik, akkor az admin-t ellenőrizzük
                    if user_type == 'admin' and stored_user == username and stored_pass == password:
                        return True
                    # Ha felhasználóként próbálkozik, akkor a user-t ellenőrizzük
                    elif user_type == 'user' and stored_user == username and stored_pass == password:
                        return True
        return False

    def open_library_window(self, user_type):
        # Új ablak nyílik a könyvtár kezelésére
        library_win = tk.Toplevel(self.root)
        library_win.title("Könyvtár Főablak")
        library_win.geometry("400x300")

        if user_type == 'admin':
            tk.Label(library_win, text="Adminisztrátor: Könyvek kezelése", font=("Arial", 12)).pack(pady=10)
            # Adminisztrátor funkciók: könyvek hozzáadása, törlése, módosítása
            tk.Button(library_win, text="Könyvek hozzáadása", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek törlése", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek módosítása", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek keresése", width=20).pack(pady=5)
        else:
            tk.Label(library_win, text="Felhasználó: Könyvek olvasása és kölcsönzése", font=("Arial", 12)).pack(pady=10)
            # Felhasználói funkciók: könyvek olvasása, kölcsönzése
            tk.Button(library_win, text="Könyvek olvasása", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek kölcsönzése", width=20).pack(pady=5)
            tk.Button(library_win, text="Kölcsönzött könyveim", width=20).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Könyvtár Bejelentkezés")
        self.root.geometry("300x250")

        self.users_file = 'users.txt'

        # Képzeljünk el két gombot: Admin és Felhasználó bejelentkezéshez
        self.login_as_label = tk.Label(root, text="Válaszd ki a bejelentkezés típusát", font=("Arial", 12))
        self.login_as_label.pack(pady=10)

        self.admin_button = tk.Button(root, text="Bejelentkezés Adminisztrátorként", width=30, command=self.login_as_admin)
        self.admin_button.pack(pady=5)

        self.user_button = tk.Button(root, text="Bejelentkezés Felhasználóként", width=30, command=self.login_as_user)
        self.user_button.pack(pady=5)

    def login_as_admin(self):
        self.login_window('admin')

    def login_as_user(self):
        self.login_window('user')

    def login_window(self, user_type):
        # Új ablak nyílik, ahol meg kell adni a felhasználónevet és a jelszót
        login_win = tk.Toplevel(self.root)
        login_win.title(f"Bejelentkezés {user_type.capitalize()}ként")
        login_win.geometry("300x200")

        # Felhasználó név
        tk.Label(login_win, text="Felhasználónév:").pack(pady=5)
        username_entry = tk.Entry(login_win)
        username_entry.pack(pady=5)

        # Jelszó
        tk.Label(login_win, text="Jelszó:").pack(pady=5)
        password_entry = tk.Entry(login_win, show="*")
        password_entry.pack(pady=5)

        def check_login():
            username = username_entry.get()
            password = password_entry.get()
            if self.check_credentials(username, password, user_type):
                messagebox.showinfo("Sikeres bejelentkezés", "Sikeresen bejelentkeztél!")
                login_win.destroy()
                self.open_library_window(user_type)
            else:
                messagebox.showerror("Hiba", "Sikertelen bejelentkezés! Ellenőrizd a felhasználónevet és jelszót.")

        # Bejelentkezés gomb
        login_button = tk.Button(login_win, text="Bejelentkezés", command=check_login)
        login_button.pack(pady=10)

    def check_credentials(self, username, password, user_type):
        # Ellenőrizzük a felhasználót és jelszót a fájlban
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                for line in file:
                    stored_user, stored_pass = line.strip().split(':')
                    # Ha adminisztrátorként próbálkozik, akkor az admin-t ellenőrizzük
                    if user_type == 'admin' and stored_user == username and stored_pass == password:
                        return True
                    # Ha felhasználóként próbálkozik, akkor a user-t ellenőrizzük
                    elif user_type == 'user' and stored_user == username and stored_pass == password:
                        return True
        return False

    def open_library_window(self, user_type):
        # Új ablak nyílik a könyvtár kezelésére
        library_win = tk.Toplevel(self.root)
        library_win.title("Könyvtár Főablak")
        library_win.geometry("400x300")

        if user_type == 'admin':
            tk.Label(library_win, text="Adminisztrátor: Könyvek kezelése", font=("Arial", 12)).pack(pady=10)
            # Adminisztrátor funkciók: könyvek hozzáadása, törlése, módosítása
            tk.Button(library_win, text="Könyvek hozzáadása", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek törlése", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek módosítása", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek keresése", width=20).pack(pady=5)
        else:
            tk.Label(library_win, text="Felhasználó: Könyvek olvasása és kölcsönzése", font=("Arial", 12)).pack(pady=10)
            # Felhasználói funkciók: könyvek olvasása, kölcsönzése
            tk.Button(library_win, text="Könyvek olvasása", width=20).pack(pady=5)
            tk.Button(library_win, text="Könyvek kölcsönzése", width=20).pack(pady=5)
            tk.Button(library_win, text="Kölcsönzött könyveim", width=20).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
