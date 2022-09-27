#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random
import os


def ustawienia():
    """"Funkcja pobiera nick użytkownika, ilość losowanych lizb, maksymalną losowaną wartość oraz ilość typowań. Ustawienia zapisuje. """


    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoja ustawienia:\nLiczb: %s\nZ Maks: %s\n Losowań: %s" %
            (gracz[1], gracz[2], gracz[3]))
        odp = input ("Zmieniasz (t/n?) ")

    if not gracz or odp.lower() == "t":
        while True:
            try:
                ileliczb = int(input("Ile liczb chcesz odgadnąć?\n"))
                maksliczba = int(input("Podaj maksymalną liczbę\n"))
                if ileliczb > maksliczba:
                    print("Błędne dane!\nNie da się wylosować",ileliczb,"różnych liczb z",maksliczba,"liczb")
                    continue
                ilelos = int(input("Ile chcesz mieć prób?"))
                break
            except ValueError:
                print("Błędne dane! Należy podać cyfrę!")
                continue
        gracz = [nick, str(ileliczb), str(maksliczba), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)

    return gracz[0:1] + [int(x) for x in gracz[1:4]]


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False

def zapisz_ust(nazwapliku,gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()

def losujliczby(ileliczb,maksliczba):
    wylosowaneLiczby =[]
    i=0
    while i < ileliczb:
        losowanaLiczba = random.randint(1,maksliczba)   
        if wylosowaneLiczby.count(losowanaLiczba) == 0:
            wylosowaneLiczby.append(losowanaLiczba)
            i = i + 1
        return wylosowaneLiczby

def pobierztypy(ileliczb, maksliczba):
    print("Wytypuj %s z %s liczb: "%(ileliczb, maksliczba))
    #typy = set()
    typy = 1 
    i=0
    while i < ileliczb:
        try:
            typ = int(input ("Podaj liczbę %s: \n" % (i + 1)))
        except ValueError:
            print("Błędne dane! Należy podać cyfrę!")
        if 0<typ>maksliczba:
            print("Błędne dane!\nPodana liczba przekracza maksymalną wartość")
            continue
        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)
            i = i + 1


def wyniki (wylosowaneLiczby, typy):
        for i in range (ilelos):
            typy = pobierztypy (ileliczb, maksliczba)
            trafione = set(wylosowaneLiczby) & typy
            if trafione:
                print("\nIlość trafień: %s" %len(trafione))
                print("Trafione liczby: %s" % trafione)
            else:
                print("Brak trafień. Spróbuj jeszcze raz!")
            print ("'n" + "x" * 40 + "\n") #wydrkuj 40 znaków x
            return len(trafione)