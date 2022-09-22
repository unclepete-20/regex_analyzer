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

expresion = '(b|b)*abb(a|b)*'
w = 'babbaaaaa'

#CONSTRUCCION DE AFN
regex = Regex(expresion)

afn = AFN(regex)
print("Transiciones")
afn.archivo_txt("afn.txt", afn.simbolos, afn.estado_inicial, afn.estados, afn.estados_aceptacion, afn.transiciones)

print("\nSimulacion de la cadena")
print(afn.simulacion(w) + "\n")

print("Conversion de AFN a AFD")
afd_estados, afd_transiciones, afd_final, afd_inicial = afn.convertir_afd()
afn.archivo_txt("afd_de_afn.txt", afn.simbolos, afd_inicial, afd_estados, afd_final, afd_transiciones)

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

#afd_directo.graficar(mapping = afd_directo.state_mapping)


print('========> SIMULACION DE LA CADENA \'{0}\' EN AFD POR METODO DIRECTO <======== \n=> {1}\n=> {2} (ms)\n'.format(w, result, tiempo))
