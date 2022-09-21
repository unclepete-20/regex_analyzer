# -*-coding:utf-8 -*-
'''
@File    :   Automata.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Implementacion de funcionalidades y caracteristicas base de un Automata
'''

import shortuuid
import graphviz

from Stack import *

# DEFINICION DE ALFABETO PARA IDENTIFICAR NODOS Y ESTADOS DEL AUTOMATA
shortuuid.set_alphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

class Automata(object):

    def __init__(self, symbols, states, tfunc, istate, tstate):
        self.states = states
        self.symbols = symbols
        self.transition_function = tfunc
        self.initial_state = istate
        self.terminal_states = tstate
        
    
    def imprimir_automata(self, type, i_state, t_state, states, symbols, t_function, state_mapping = None):
        
        print("\nDATOS: " + type + '\n')
        
        print("\n -- CARACTERES DEL ALFABETO --")
        print(" =>", symbols)
        
        print("\n -- ESTADO INICIAL --")
        print(" =>", i_state)
        
        print("\n -- ESTADOS DEL AUTOMATA --")
        for state in states:
            print("     ", state)
        
        print("\n -- ESTADOS DE ACEPTACION --")
        print(" =>", t_state)
        
        if state_mapping:
            print(" -- MAPPING --")
            for key, value in state_mapping.items():
                print("     ", key, "=>", value)
        
        print("\n -- TRANSICIONES --")
        for key, value in t_function.items():
            print("     ", key, "=>", value)
        
        print("\n")
        
        
    def simulacion_cadena(self):
        raise Exception ("=> FUNCION CREADA PARA HERENCIA EN CLASES RELACIONADAS <=")
    
    def archivo_txt(self, type, i_state, t_state, states, symbols, t_function, state_mapping = None):
        with open("afd_directo.txt","w") as file:
            file.write("\nAFD DIRECTO CONSTRUIDO POR PEDRO ARRIOLA (20188) Y OSCAR LOPEZ (20679)\n")
            file.write("\nDATOS: " + type + '\n')
            file.write("\n -- CARACTERES DEL ALFABETO --\n")
            file.write(" => " + str(symbols) + "\n")
            file.write("\n -- ESTADO INICIAL --\n")
            file.write(" => " + str(i_state) + "\n")
            file.write("\n -- ESTADOS DEL AUTOMATA --\n")
            for state in states:
                file.write("      " + str(state) + "\n")
            file.write("\n -- ESTADOS DE ACEPTACION --\n")
            file.write(" => " + str(t_state) + "\n")
            if state_mapping:
                file.write("\n -- MAPPING --\n")
                for key, value in state_mapping.items():
                    file.write("     " + str(key) + " => " + str(value) + "\n")
            file.write("\n -- TRANSICIONES --\n")
            for key, value in t_function.items():
                file.write("     " + str(key) + " => " + str(value) + "\n")
            file.close()
    
    def graficar(self, mapping = None):
        
        graphic = graphviz.Digraph(graph_attr = {'rankdir':'LR'}) # Se define a direccion de los nodos del AFD
        
        for i in self.states:
            i = i if not mapping else mapping[tuple(i)]
            if i not in self.terminal_states:
                graphic.attr('node', shape = 'circle')
                graphic.node(i)
            else:
                graphic.attr('node', shape = 'doublecircle')
                graphic.node(i)
                
        graphic.attr('node', shape = 'none')
        graphic.node('')
        graphic.edge('', self.initial_state)
        
        for key, value in self.transition_function.items():
            if isinstance(value, str):
                graphic.edge(key[0], value, label = (key[1]))
            else:
                for val in value:
                    graphic.edge(key[0], val, label = (key[1]))
        
        graphic.view('afd_directo.gv', cleanup = True)