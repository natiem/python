# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

ilosc_par = 10

imiona_meskie = ['ANTONI','JAN','JAKUB','ALEKSANDER','SZYMON','FRANCISZEK','FILIP','MIKOŁAJ','WOJCIECH','ADAM','KACPER','STANISŁAW','MARCEL','LEON','MICHAŁ','NIKODEM','TYMON','IGNACY','WIKTOR','IGOR']
imiona_zenskie = ['ZUZANNA','JULIA','ZOFIA','MAJA','HANNA','LENA','ALICJA','MARIA','OLIWIA','AMELIA','WIKTORIA','ALEKSANDRA','ANTONINA','LAURA','EMILIA','POLA','MARCELINA','NATALIA','LILIANA','IGA']

nazwiska_meskie = ['NOWAK','KOWALSKI','WIŚNIEWSKI','WÓJCIK','KOWALCZYK','KAMIŃSKI','LEWANDOWSKI','ZIELIŃSKI','SZYMAŃSKI','DĄBROWSKI','WOŹNIAK','KOZŁOWSKI','JANKOWSKI','MAZUR','KWIATKOWSKI','WOJCIECHOWSKI','KRAWCZYK','KACZMAREK','PIOTROWSKI','GRABOWSKI']
nazwiska_zenskie = ['NOWAK','KOWALSKA','WIŚNIEWSKA','WÓJCIK','KOWALCZYK','KAMIŃSKA','LEWANDOWSKA','ZIELIŃSKA','SZYMAŃSKA','DĄBROWSKA','WOŹNIAK','KOZŁOWSKA','JANKOWSKA','MAZUR','KWIATKOWSKA','WOJCIECHOWSKA','KRAWCZYK','KACZMAREK','PIOTROWSKA','GRABOWSKA']

print ("M - Pary męskie")
print ("K - Pary żeńskie")

wybor = input('Twój wybór. Wybierz M lub K:')


if wybor == "M":
    imiona = imiona_meskie
    nazwiska = nazwiska_meskie
elif wybor == "K":
    imiona = imiona_zenskie
    nazwiska = nazwiska_zenskie

    
    
wyniki = []    
for i in range(ilosc_par):
    imie = imiona.pop(random.randint(0, len(imiona)-1))
    nazwisko = nazwiska.pop(random.randint(0, len(nazwiska)-1))
    wyniki.append (imie + ' ' + nazwisko) 
    
for wynik in wyniki:
    print (wynik)
    


