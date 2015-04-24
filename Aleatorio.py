"""
Andrea Silva Cala
08-03-15
"""

import random 

cuatro = ('radioburguer', 'la creperia')
uno= ('Fire&love', 'Aderezando', 'Tropical', 'silla de colores', 'special')
dos= ('combo saludable', 'combo uis', 'perro caliente', 'la vecina', 'Hamburguesa vegana')
print ("Hola, no sabes donde almorzar hoy?")
print ("Esto puede ayudarte")
Valor=int(input("cuanto dinero tienes")) 

print ("Estos son los retaurantes a los que puedes ir" )


if Valor  >5000 and Valor <= 10000:
    print (uno)
elif Valor >2000 and Valor <= 5000:
    print (dos)
elif Valor > 10000 and Valor <= 50000:
    print (cuatro)
elif Valor > 50000:
    print cuatro, dos, uno
elif Valor < 0:
    print ("Debes escribir un numero positivo")    
else:
    print ("Acude a tu director de tesis")
    
print ("Quieres escoger un restaurante de estos al azar?") 
print ("(s): si (n): no")
azar= raw_input()

runo= random.sample (uno, 1)
rdos= random.sample (dos, 1)
rcuatro= random.sample (cuatro, 1)

if Valor  >5000 and Valor <= 10000:
    print (runo)
elif Valor >2000 and Valor <= 5000:
    print (rdos)
elif Valor > 10000 and Valor <= 50000:
    print (rcuatro)
else:
    print ("Acude a tu director de tesis")
