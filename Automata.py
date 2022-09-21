import os
import shortuuid
import graphviz, tempfile

from Stack import *


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
    
    def archivo_txt(self):
        pass