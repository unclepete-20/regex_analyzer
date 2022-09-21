# -*-coding:utf-8 -*-
'''
@File    :   afd_directo.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Implementacion de construccion de AFD por el metodo directo
'''

from regex import *
from Automata import Automata
import uuid
import shortuuid
from timeit import default_timer as timer

# DEFINICION DE ALFABETO PARA IDENTIFICAR NODOS Y ESTADOS DEL AUTOMATA
shortuuid.set_alphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

class AFD_DIRECTO(Automata):
    
    def __init__(self, nfa = None, 
                 syntax_tree = None, 
                 symbols = None, 
                 states = [], 
                 tfunc = {}, 
                 istate = None, 
                 tstate = [], 
                 directo = False, 
                 nodes = None):
        
        self.syntax_tree = syntax_tree
        self.nfa = nfa
        self.nodes = nodes
        self.state_mapping = None
        
        
        # instanciamos el objeto de tipo Automata para generar cierto nivel de herencia
        Automata.__init__(
            self, 
            symbols = nfa.symbols if nfa else syntax_tree.alfabeto,
            states = states, 
            tfunc = tfunc,
            istate = istate, 
            tstate = tstate
        )

    
    def define_alphabet(self):
        alphabet = []
        regex = self.postfix
        
        for char in regex:
            if (char != '(' and char != ')' and char != '|' and char != '*' and char != '.' and char != '+' and char != '#'):
                alphabet.append(char)
            
        alphabet = set(alphabet)
        alphabet = list(alphabet)
        alphabet.sort()
        
        return alphabet
    
    
    def followpos_computation(self):
        self.followpos = {}
        
        for node in self.nodes:
            if node.pos:
                self.followpos[node.pos] = []
            
        for node in self.nodes:
            if node.data == '.':
                for i in node.left.lastpos:
                    self.followpos[i] += node.right.firstpos
                    
            if node.data == '*':
                for i in node.lastpos:
                    self.followpos[i] += node.firstpos
    
    
    # Aplicacion del algoritmo para la construccion directa de un AFD apartir de un REGEX
    def directo(self):
        self.followpos_computation()
        
        print('followpos: ' + str(self.followpos))
        
        final_pos = 0
        
        for node in self.nodes:
            if node.data == '#':
                final_pos = node.pos

        t_func = {}
        subset_mapping = {}
        
        dstates_u = [self.syntax_tree.raiz.firstpos]
        dstates_m = []
        
        while len(dstates_u) > 0:
            T = dstates_u.pop(0)
            dstates_m.append(T)
            
            for symbol in self.symbols:
                U = []
                for node in self.nodes:
                    if node.data == symbol and node.pos in T:
                        U += self.followpos[node.pos]
                        U = list(set(U))
                
                if len(U) > 0:
                    if U not in dstates_u and U not in dstates_m:
                        dstates_u.append(U)
                        
                    try: 
                        subset_mapping[tuple(T)]
                    except:
                        subset_mapping[tuple(T)] = shortuuid.encode(uuid.uuid4())[:2]
                        
                    try:
                        subset_mapping[tuple(U)]
                    except:
                        subset_mapping[tuple(U)] = shortuuid.encode(uuid.uuid4())[:2]
                        
                    
                    t_func[(subset_mapping[tuple(T)], symbol)] = subset_mapping[tuple(U)]                        

        for state in dstates_m:
            if final_pos in state:
                self.terminal_states.append(subset_mapping[tuple(state)])

        self.initial_state = subset_mapping[tuple(dstates_m[0])]
        self.states = dstates_m
        self.transition_function = t_func
        self.state_mapping = subset_mapping
        
        self.imprimir_automata("AFD DIRECTO", self.initial_state, self.terminal_states, self.states, self.symbols, self.transition_function, state_mapping=subset_mapping)
        self.archivo_txt("AFD DIRECTO", self.initial_state, self.terminal_states, self.states, self.symbols, self.transition_function, state_mapping=subset_mapping)
    
    # Simulacion de cadena ingresada por el usuario    
    def simulacion_cadena(self, cadena):
        inicio = timer()
        
        s = self.initial_state
        terminal = False
        
        # Se verifica si pertenece a L(r) o no
        for char in cadena:
            if char not in self.symbols:
                terminal = None
                break
                exit()
            
            try:
                s = self.transition_function[(s, char)]
            except:
                break
        
        terminal = True if s in self.terminal_states else terminal
        
        final = timer()
        
        tiempo_resultante = (final - inicio) * 1000
        
        pertenece_lenguaje = terminal if terminal is None else 'La cadena SI pertenece a L(r)' if terminal else 'La cadena NO pertenece a L(r)'
        
        return (tiempo_resultante, pertenece_lenguaje)