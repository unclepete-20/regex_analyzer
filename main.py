#
#
#

from regex import *

print("Bienvenido")

expresion = input("Ingresa la expresion para convertir: ")
cadena = input("Ingresa la cadena para verficar: ")

regex = Regex(expresion)
print(regex.postfixExpression)