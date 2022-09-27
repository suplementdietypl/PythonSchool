#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from cmath import sqrt
import math
console = True

iloscNasionek = int(input("Ile masz nasionek?"))
iloscPowtorzen = (int(iloscNasionek / 2))
iloscPowtorzen = iloscPowtorzen
#int(input("Ile powtorzen wykonac?"))+1
dzielniki = set()
for i in range(iloscPowtorzen):
    if (i==0):
        i = 1
    else:
        if (iloscNasionek % i == 0):
            val2 = int(iloscNasionek/i)
            print ("Twoje pole może mieć wymiary",i,"na",val2)
            dzielniki.add(i)
            i = i + 1
#print ("Optymalna liczba rzędów wynosi",max(dzielniki))
print ("pierwiastek z liczby",iloscNasionek," wynosi",sqrt(iloscNasionek))


#if(sqrt(iloscNasionek)%sqrt(iloscNasionek)==0):
#else:
#    print(iloscNasionek,"nie posiada pierwiastka")




#    if (i >= iloscPowtorzen):
#        if (iloscNasionek) % i == 0:
#            print (iloscNasionek,"jest podzielna przez",i)
#            i = i + 1
#    else:
#        print (iloscNasionek,"nie jest podzielna przez",i)