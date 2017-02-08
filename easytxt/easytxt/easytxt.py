'''
Opis biblioteki easytxt:


'''

__all__ = [
      'wiadomosc'
    , 'taknie'
    , 'kontynuowac'
    , 'podajLiczbe'
    , 'podajHaslo'

]

import os
import sys
import string


'''
if sys.hexversion >= 0x020600F0:
    runningPython26 = True
else:
    runningPython26 = False

if sys.hexversion >= 0x030000F0:
    runningPython3 = True
else:
    runningPython3 = False
'''
#-----------------------------------------------------------------------
# wiadomosc(tresc) - pozwala wyswietlic wiadomosc dowolnej tresci
#-----------------------------------------------------------------------

def wiadomosc(tresc):

	print "\n", tresc
	
	return

#-----------------------------------------------------------------------
# taknie(pytanie) - pozwala zadac pytanie z mozliwymi odpowiedziami tak i nie
#-----------------------------------------------------------------------	

def taknie(pytanie):
	
	print "\n", pytanie
	p=raw_input('Odpowiedz "Tak(ENTER)" lub "Nie" ')
	q=p.lower() #zmieniamy na male litery aby ulatwic walidacje

	if(q=="tak" or q==""):
		return True
	elif(q=="nie"):
		return False
	else:
		return taknie(pytanie)
	
#-----------------------------------------------------------------------
# kontynuowac() - umozliwia zapytanie czy kontunuowac dzialanie programu
#-----------------------------------------------------------------------
	
def kontynuowac():
	
	print "\nKontynuowac? "
	p=raw_input('Odpowiedz "Kontynuuj(ENTER)" lub "Anuluj" ')
	q=p.lower() #zmieniamy na male litery aby ulatwic walidacje

	if(q=="kontynuuj" or q==""):
		return True
	elif(q=="anuluj"):
		return False
	else:
		return kontynuowac()
		
#-----------------------------------------------------------------------
# podajLiczbe(od, do)  - umozliwia wprowadzenie i walidacje liczby calkowitej
#-----------------------------------------------------------------------

def podajLiczbe(od, do):
	
	print "\nPodaj liczbe z przedzialu od {0} do {1}".format(od, do)
	q=raw_input()
	d=int(q)
	if ((d > od and d < do) and isinstance(d, int)):
		return d
	else:
		return podajLiczbe(od, do)
	
#-----------------------------------------------------------------------
# podajHaslo(znaki) - umozliwia wprowadzenie zamaskowanego hasla
# o ustalonej minimalnej liczbie znaków oraz zaszyfrowanie go
#-----------------------------------------------------------------------

def podajHaslo(znaki):
	
	import getpass
	import hashlib
	
	print "\nPodaj haslo skladajace sie z minimum {0} znakow".format(znaki)
	haslo = getpass.getpass('Podaj haslo: ')
	if len(haslo) < znaki:
		return podajHaslo(znaki)
	else:
		haslo = hashlib.md5(haslo).hexdigest()
		return haslo

#-----------------------------------------------------------------------
# dowolne(tresc)  - umozliwia utworzenie zmiennej dowolnej tresci
#-----------------------------------------------------------------------
		
def dowolne(tresc):

	z = tresc
	return z
	
#-----------------------------------------------------------------------
# () - 
#-----------------------------------------------------------------------

