def warunki_atmosferyczne():
    wpisywanie = True
    while wpisywanie:
        wspolczynnik_SFI = input("Podaj współczynnik SFI (100 - 700): ")
        wspolczynnik_K = input("Podaj współczynnik K (0 - 7): ")
        if (wspolczynnik_SFI.isdigit() and int(wspolczynnik_SFI) >= 100 and int(wspolczynnik_SFI) <= 700 and
                wspolczynnik_K.isdigit() and int(wspolczynnik_K) >= 0 and int(wspolczynnik_K) < 8):
            warunki_pogodowe = (int(wspolczynnik_SFI), int(wspolczynnik_K))
            return warunki_pogodowe
        print("Zły wybór !!!. Jeszcze raz !!!")

# TODO Dane: dopisanie danych o pogodzie: wskaźniki SFI i K, skrapowane ze strony internetowej
