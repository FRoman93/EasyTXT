'''
Opis biblioteki easytxt:

Biblioteka działa podobnie do biblioteki easygui z tym, że tutaj wymiana informacji 
z użytkownikiem odbywa się za pomoca terminala, nie posiada ona GUI

'''

__all__ = [
      'wiadomosc'
    , 'taknie'
    , 'kontynuowac'
    , 'podajLiczbe'
    , 'podajHaslo'
    , 'dowolne'
    , 'wybierzWiele'
]

import os
import sys
import string



if sys.hexversion >= 0x020600F0:
    runningPython26 = True
else:
    runningPython26 = False

if sys.hexversion >= 0x030000F0:
    runningPython3 = True
else:
    runningPython3 = False

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

def podajLiczbe(poczatek, koniec):
	
	print "\nPodaj liczbe z przedzialu od {0} do {1}".format(poczatek, koniec)
	
	try:
		d = int(raw_input())
		if (d > poczatek and d < koniec):
			return d
		else:
			return podajLiczbe(poczatek, koniec)
	except:
		return podajLiczbe(poczatek, koniec)
	
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
# wybierzWiele(*elementy) - pozwala na wybor wielu elementow z ustalonej listy
#-----------------------------------------------------------------------

if runningPython26:
	def wybierzWiele(*elementy):
	
		elementy = [str(element) for element in elementy]
		for i in range(0, len(elementy)):
			print "\n",[i], elementy[i]
		
		w = raw_input("Wybierz dowolna liczbe elementow, podajac ich numery oddzielone spacjami: ")
		numery = w.split()
		numery = map(int, numery)
		wybory = []
		for i in range(0, len(numery)):
			wybory.append(elementy[numery[i]])
			
		return wybory
else:
	def wybierzWiele(*elementy):
	
		elementy = [str(element) for element in elementy]
		for i in range(0, len(elementy)):
			print "\n",[i], elementy[i]
		
		w = raw_input("Wybierz dowolna liczbe elementow, podajac ich numery oddzielone spacjami: ")
		numery = w.split()
		numery = list(map(int, numery))
		wybory = []
		for i in range(0, len(numery)):
			wybory.append(elementy[numery[i]])
			
		return wybory