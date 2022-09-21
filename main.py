#REGEX DE PRUEBA
# (a|b)*abb
#

from regex import *
from afn import * 
from afd_directo import *
from SyntaxTree import *
from progress.bar import ChargingBar
import os, time, random

print("\nBienvenido al ANALIZADOR LEXICO 9000\n")

# expresion = input("Ingresa la expresion para convertir: ")
# cadena = input("Ingresa la cadena para verficar: ")

expresion = '(a|b)*aab'
w = 'bbbaab'

regex = Regex(expresion)
#afn = AFN(regex)
#print(afn.transiciones)

print(regex.postfixExpresion)

afn = AFN(regex)
print(afn.transiciones)


# CONSTRUCCION AFD DIRECTO
print('\n========> CONSTRUCCION AFD DIRECTO <========\n')
regex_directo = Regex(expresion)
extended_regex = regex_directo.postfixRegex()
extended_regex += '#.'

bar2 = ChargingBar('Construyendo:', max = 100)
for num in range(100):
    time.sleep(random.uniform(0, 0.03))
    bar2.next()
bar2.finish()

print('\n')

hash_tree = SyntaxTree(extended_regex, directo = True)
print('REGEX: ' + str(hash_tree.postfix))


nodos = hash_tree.traverse_postorder(hash_tree.raiz, full=True)


afd_directo = AFD_DIRECTO(syntax_tree = hash_tree, directo = True, nodes = nodos)

afd_directo.directo()

tiempo, result = afd_directo.simulacion_cadena(w)

print('========> SIMULACION DE LA CADENA \'{0}\' EN AFD POR METODO DIRECTO <======== \n=> {1}\n=> {2} (ms)\n'.format(w, result, tiempo))

