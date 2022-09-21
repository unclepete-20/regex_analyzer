#
#
#

from regex import *
from afn import * 

print("Bienvenido")

expresion = input("Ingresa la expresion para convertir: ")
cadena = input("Ingresa la cadena para verficar: ")

regex = Regex(expresion)
print(regex.postfixExpresion)

afn = AFN(regex)
print(afn.transiciones)