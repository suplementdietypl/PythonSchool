#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import random
import os
import sys
#from totomax import ustawienia, losujliczby, wyniki, pobierztypy
from totomax import *

def main(args):
    #ustawienia gry
    nick, ileliczb, maksliczba, ilelos = ustawienia()
    
    #losujemy liczby
    wylosowaneLiczby = losujliczby (ileliczb, maksliczba)


    #pobieramy typy uzytkownika i sprawdzamy, ile liczb trafił
    iletraf = wyniki(set(wylosowaneLiczby), typy)

    print ("Wylosowane liczby:", wylosowaneLiczby)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
