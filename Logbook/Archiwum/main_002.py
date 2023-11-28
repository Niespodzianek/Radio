# Nazwa kodowa projektu: "Logbook"
# Aktualna wersja projektu: 0.0.2.
# Nazwa produkcyjna projektu: "Asystent krótkofalarza"
# Copyright: Michał Grzyb

import datetime

ZNAK = "SP9MRG"
RADIOODBIORNIKI = ["WebSDR", "Radio OK Model ORF 230-1"]
KODY_Q = ["QSO", "SWL"]
KARTA_SQL = ["SQL", "bez SQL"]

def wybor(opcje_wyboru):
    wybieranie = True
    while wybieranie:
        print("Wybierz jedną z dostępnych opcji:")
        for index, element in enumerate(opcje_wyboru):
            print(f"({index + 1}) - {element}")
        decyzja = input("Twój wybór to: ")
        if decyzja.isdigit() and ((int(decyzja) - 1) < len(opcje_wyboru)) and (int(decyzja) > 0):
            wybieranie = False
        else:
            print("Zły wybór !!! Jeszcze raz.\n")
    return opcje_wyboru[int(decyzja) - 1]

def wpisanie_korespondenta(info=" "):
    wpisywanie = True
    while wpisywanie:
        znak_korespondenta = input("Podaj znak" + f"{info}" + "korespondenta: ").upper()
        print(f"Debug: {znak_korespondenta} - {len(znak_korespondenta)}")
        if 3 < len(znak_korespondenta) < 7:
            if znak_korespondenta[0].isalpha() and znak_korespondenta[1].isalpha() and znak_korespondenta[2].isdigit() and znak_korespondenta[3].isalpha():
                print(f"Debug: {znak_korespondenta} - {len(znak_korespondenta)}")
                while len(znak_korespondenta) < 6:
                    znak_korespondenta += " "
                print(f"Debug: {znak_korespondenta} - {len(znak_korespondenta)}")
                return znak_korespondenta
            else:
                print("Nieprawidłowy znak !!! Jeszcze raz.")
        else:
            print("Nieprawidłowy znak !!! Jeszcze raz.")
    return 0

def raport_krotkofalarski():
    # raport = (0, 0)
    slyszalnosc = input("Wpisz poziom słyszalności (0 - 5; 0 to najsłabsza słyszalność, 5 to idealna słyszalność): ")
    raport = (int(slyszalnosc), 0)
    return raport

def pogoda():
    # warunki_pogodowe = (0, 0)
    wspolczynnik_SFI = input("Podaj współczynnik SFI: ")
    wspolczynnik_K = input("Podaj współczynnik K: ")
    warunki_pogodowe = (int(wspolczynnik_SFI), int(wspolczynnik_K))
    return warunki_pogodowe

def nowe_polaczenie(dotychczasowe_dane):
    czas_utc = datetime.datetime.utcnow()
    czas_lokalny = datetime.datetime.now()
    print(f"Debug: Czas UTC: {czas_utc}, czas lokalny: {czas_lokalny}")
    znak_korespondenta = wpisanie_korespondenta()
    raport = raport_krotkofalarski()
    warunki_atmosferyczne = pogoda()
    radio = wybor(RADIOODBIORNIKI)
    # kod_Q = wybor(KODY_Q)
    karta = wybor(KARTA_SQL)
    dotychczasowe_dane.append([czas_utc, "SQO", ZNAK, znak_korespondenta, radio, raport, warunki_atmosferyczne, karta, czas_lokalny])
    nowe_dane_polaczen = dotychczasowe_dane
    return nowe_dane_polaczen

def nowy_nasłuch(dotychczasowe_dane):
    czas_utc = datetime.datetime.utcnow()
    czas_lokalny = datetime.datetime.now()
    print(f"Debug: Czas UTC: {czas_utc}, czas lokalny: {czas_lokalny}")
    wpisywanie = True
    while wpisywanie:
        znak_korespondent_pierwszy = wpisanie_korespondenta(info=" pierwszego ")
        znak_korespondent_drugi = wpisanie_korespondenta(info=" drugiego ")
        if znak_korespondent_pierwszy != znak_korespondent_drugi:
            raport = raport_krotkofalarski()
            warunki_atmosferyczne = pogoda()
            radio = wybor(RADIOODBIORNIKI)
            # kod_Q = wybor(KODY_Q)
            karta = wybor(KARTA_SQL)
            dotychczasowe_dane.append([czas_utc, "SWL", znak_korespondent_pierwszy, znak_korespondent_drugi, radio,raport, warunki_atmosferyczne, karta, czas_lokalny])
            nowe_dane_polaczen = dotychczasowe_dane
            return nowe_dane_polaczen
        else:
            print("Wpisano te same znaki !!!! Jeszcze raz.")

def menu(dane_polaczen):
    wybor_menu = input("(1) Nowe połączenie\n(2) Nowy nasłuch\n(3) Przegląd połączeń\n(X) Notatnik\n(Y) ISS\n(Q) - Koniec pracy programu\n")
    if wybor_menu == "1":
        dane_polaczen = nowe_polaczenie(dotychczasowe_dane=dane_polaczen)
    elif wybor_menu == "2":
        dane_polaczen = nowy_nasłuch(dotychczasowe_dane=dane_polaczen)
    elif wybor_menu == "3":
        if len(dane_polaczen) == 0:
            print("Dotychczas jeszcze nie było żadnych wpisów !!! Logbook jest pusty !!!")
        else:
            for dane in dane_polaczen:
                print(dane)
    elif wybor_menu == "q" or wybor_menu == "Q":
        return False
    else:
        print("Niewłaściwy wybór opcji menu !!!")
    return True

def program():
    baza_polaczen = []
    praca_programu = True
    while praca_programu:
        print(f"Debug: {praca_programu}")
        praca_programu = menu(dane_polaczen=baza_polaczen)
        print(f"Debug: {praca_programu}")

if __name__ == "__main__":
    program()
    print("KONIEC PROGRAMU")
