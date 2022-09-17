#
#
#

from regex import *

print("Bienvenido")

expresion = 'aa*|bb*'
#expresion = input("Ingresa la expresion para convertir: ")
#cadena = input("Ingresa la cadena para verficar: ")

# a?a*|b?b*

regex = Regex(expresion)
print(regex.postfixExpression)