# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Programa principal para ejecutar todas la funcionalidad implementadas
'''

#REGEX DE PRUEBA
# (a|b)*abb
#

from regex import *
from afn import * 
from afd_directo import *
from SyntaxTree import *
from progress.bar import ChargingBar
import time, random

print("\nBienvenido al ANALIZADOR LEXICO 9000\n")

# expresion = input("Ingresa la expresion para convertir: ")
# cadena = input("Ingresa la cadena para verficar: ")

expresion = '(b|b)*abb(a|b)*'
w = 'babbaaaaa'

regex = Regex(expresion)
#afn = AFN(regex)
#print(afn.transiciones)

print(regex.postfixExpresion)

afn = AFN(regex)
print(afn.transiciones)
afn.simulacion(w)

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

arbol_sintactico = SyntaxTree(extended_regex, directo = True)
print('REGEX: ' + str(arbol_sintactico.postfix))


nodos = arbol_sintactico.traverse_postorder(arbol_sintactico.raiz, full=True)

afd_directo = AFD_DIRECTO(syntax_tree = arbol_sintactico, directo = True, nodes = nodos)

afd_directo.directo()

print("\n[INFO] ARCHIVO TXT GENERADO\n")

tiempo, result = afd_directo.simulacion_cadena(w)

afd_directo.graficar(mapping = afd_directo.state_mapping)


print('========> SIMULACION DE LA CADENA \'{0}\' EN AFD POR METODO DIRECTO <======== \n=> {1}\n=> {2} (ms)\n'.format(w, result, tiempo))

