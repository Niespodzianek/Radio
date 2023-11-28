def raport_krotkofalarski():
    wpisywanie = True
    while wpisywanie:
        slyszalnosc = input("Wpisz poziom słyszalności (0 - 5; 0 to najsłabsza słyszalność, 5 to idealna słyszalność): ")
        if slyszalnosc.isdigit() and int(slyszalnosc) >= 0 and int(slyszalnosc) < 6:
            raport = (int(slyszalnosc), 0)
            return raport
        else:
            print("Zły wybór !!! Jeszcze raz !!!")
