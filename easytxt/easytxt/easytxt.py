'''
Opis biblioteki easytxt:


'''

__all__ = [
      'taknie'
    , 'kontynuowac'
    , 'wiadomosc'

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
# wiadomosc
#-----------------------------------------------------------------------

def wiadomosc(tresc):

	print "\n", tresc

#-----------------------------------------------------------------------
# taknie
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
# kontynuowac?
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
# taknie
#-----------------------------------------------------------------------

