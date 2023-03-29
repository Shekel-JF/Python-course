Program napisany został na wersji Pythona 3.9.13.

Jest to lekko zmodyfikowana znana i kochana gra w statki.
Różnica polega na tym, że statki mogą być stawiane obok siebie, a gracz ma tylko 80 tur na zniszczenie wszystkich statków wroga.

Wszelkie instrukcje program będzie wyświetlał podczas działania, ale w skrócie:

1. Gracz ustawia swoje statki. Jeżeli stawiany statek jest podwójny lub większy, to gra zapyta czy ma być on poziomy czy pionowy i wtedy w zależności od naszego wyboru gra zapełni pola na prawo lub w dół od pola początkowego.

2. Gracz musi zgadywać pozycję statków przeciwnika. Analogicznie do ustawiania swoich statków będziemy typować interesujące nas wiersze i kolumny.

Spróbowałem troszkę urozmaicić bota, żeby nie strzelał on całkowicie losowo. Po udanym trafieniu będzie celował w jedno z dwóch sąsiednich pól.