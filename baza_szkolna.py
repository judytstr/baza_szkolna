class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy

class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

uczniowie = []
nauczyciele = []
wychowawcy = []

def utworz_ucznia():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    klasa = input("Podaj nazwę klasy ucznia: ")
    uczniowie.append(Uczen(imie, nazwisko, klasa))

def utworz_nauczyciela():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    przedmiot = input("Podaj nazwę przedmiotu: ")
    print("Podaj klasy, które prowadzi nauczyciel (wpisz 'koniec' aby zakończyć):")
    klasy = []
    while True:
        klasa = input()
        if klasa == 'koniec':
            break
        klasy.append(klasa)
    nauczyciele.append(Nauczyciel(imie, nazwisko, przedmiot, klasy))

def utworz_wychowawce():
    imie = input("Podaj imię wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    klasa = input("Podaj nazwę klasy, którą prowadzi wychowawca: ")
    wychowawcy.append(Wychowawca(imie, nazwisko, klasa))

def zarzadzaj_klasa():
    klasa = input("Podaj nazwę klasy: ")
    uczniowie_klasy = [uczen for uczen in uczniowie if uczen.klasa == klasa]
    wychowawca_klasy = [wychowawca for wychowawca in wychowawcy if wychowawca.klasa == klasa]
    print("Uczniowie klasy {}: ".format(klasa))
    for uczen in uczniowie_klasy:
        print(uczen.imie, uczen.nazwisko)
    print("Wychowawca klasy {}: ".format(klasa))
    for wychowawca in wychowawca_klasy:
        print(wychowawca.imie, wychowawca.nazwisko)

def zarzadzaj_uczen():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    for uczen in uczniowie:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            print("Uczeń {} {}: ".format(uczen.imie, uczen.nazwisko))
            print("Klasa: ", uczen.klasa)
            break
    else:
        print("Nie znaleziono ucznia o podanych danych.")

def zarzadzaj_nauczyciel():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    for nauczyciel in nauczyciele:
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            print("Nauczyciel {} {}: ".format(nauczyciel.imie, nauczyciel.nazwisko))
            print("Przedmiot: ", nauczyciel.przedmiot)
            print("Klasy: ", ', '.join(nauczyciel.klasy))
            break
    else:
        print("Nie znaleziono nauczyciela o podanych danych.")

def zarzadzaj_wychowawca():
    imie = input("Podaj imię wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    for wychowawca in wychowawcy:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            print("Wychowawca {} {}: ".format(wychowawca.imie, wychowawca.nazwisko))
            print("Klasa: ", wychowawca.klasa)
            uczniowie_klasy = [uczen for uczen in uczniowie if uczen.klasa == wychowawca.klasa]
            for uczen in uczniowie_klasy:
                print(uczen.imie, uczen.nazwisko)
            break
    else:
        print("Nie znaleziono wychowawcy o podanych danych.")

while True:
    print("\nMENU:")
    print("1. Utwórz")
    print("2. Zarządzaj")
    print("3. Koniec")
    opcja = input("Wybierz opcję: ")

    if opcja == 'utworz':
        while True:
            print("\nTworzenie użytkowników:")
            print("1. Uczeń")
            print("2. Nauczyciel")
            print("3. Wychowawca")
            print("4. Koniec")
            wybor = input("Wybierz opcję: ")

            if wybor == 'uczeń':
                utworz_ucznia()
            elif wybor == 'nauczyciel':
                utworz_nauczyciela()
            elif wybor == 'wychowawca':
                utworz_wychowawce()
            elif wybor == 'koniec':
                break
            else:
                print("Niepoprawna opcja.")

    elif opcja == 'zarzadzaj':
        while True:
            print("\nZarządzanie użytkownikami:")
            print("1. Klasa")
            print("2. Uczeń")
            print("3. Nauczyciel")
            print("4. Wychowawca")
            print("5. Koniec")
            wybor = input("Wybierz opcję: ")

            if wybor == 'klasa':
                zarzadzaj_klasa()
            elif wybor == 'uczeń':
                zarzadzaj_uczen()
            elif wybor == 'nauczyciel':
                zarzadzaj_nauczyciel()
            elif wybor == 'wychowawca':
                zarzadzaj_wychowawca()
            elif wybor == 'koniec':
                break
            else:
                print("Niepoprawna opcja.")

    elif opcja == 'koniec':
        break

    else:
        print("Niepoprawna opcja.")