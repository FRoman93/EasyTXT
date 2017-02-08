'''
Opis biblioteki easytxt:


'''

__all__ = [
      'taknie'
    , 'wybor'
#    , 'funkcja3'
    #itp !! zmienić
]

import os
import sys
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
# taknie
#-----------------------------------------------------------------------
def taknie(msg):
	
	 var1=raw_input(msg, "Tak/Nie? ")
	 
	 
	 if(var1)=="Tak":
	 return True
	 else:
	 return False
	  
	 