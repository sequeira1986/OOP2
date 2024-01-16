class Person:
    def __init__(self, name, age, gender, location, job, farba_oci):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location # ak nastavim private dediaci objekt nemoze pouzit tuto hodnotu / pri student funkcii vyhodi chybu
        self.job = job
        self.oci_farba = farba_oci
def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")
