class Tel:
    def __init__(self,imie, nazwisko, firma, stanowisko,email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.email = email

KarolKondracki = Tel(imie='Karol',nazwisko = 'kondracki',firma='BAS',stanowisko='Szef',email="karxol@o2.pl")
KarolinaKondracki = Tel(imie='Karolina',nazwisko = 'kondracki',firma='BAS',stanowisko='kierownik',email="kierownik@o2.pl")
AdamKondracki = Tel(imie='Adam',nazwisko = 'kondracki',firma='BAS',stanowisko='kierownik',email="kierownik@o2.pl")
MichalKondracki = Tel(imie='Michal',nazwisko = 'kondracki',firma='BAS',stanowisko='Szef',email="karxol@o2.pl")

adress_book =[KarolKondracki,KarolinaKondracki,AdamKondracki,MichalKondracki]
for i in adress_book:
    print(i.imie,i.nazwisko,i.firma,i.stanowisko,i.email)