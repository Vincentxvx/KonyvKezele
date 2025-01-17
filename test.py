
file_path = 'books.txt'  


with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        attributes = line.strip().split(';')
        if len(attributes) == 5:
            isbn, kiado, cim, szerzo, mufaj = attributes
            print(f"ISBN: {isbn}")
            print(f"Kiadó: {kiado}")
            print(f"Cím: {cim}")
            print(f"Szerző: {szerzo}")
            print(f"Műfaj: {mufaj}")
            print("-" * 40)  
