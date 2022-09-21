# -*-coding:utf-8 -*-
'''
@File    :   afn.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Implementacion de construccion de AFN por medio de Thompson, subconjuntos y AFN => AFD
'''

class AFN(object):

    def __init__(self, regex):
        self.regex = regex
        self.regex_postfix = regex.postfixExpresion
        self.stack_caracteres = list(self.regex_postfix)
        self.contador_estados = 0
        self.estados = []
        self.transiciones = []
        self.transiciones_finales = []
        self.estado_inicial = []
        self.estados_aceptacion = []
        self.simbolos = []
        self.estado_inicio = 0
        self.estado_final = 0
        self.construccionThompson()
        self.definir_Transiciones()
    
    #ARREGLAR STRING SOLO, ej: a
    #Si se puede agregar caso para los dos ||

    def construccionThompson(self):

        caracter = self.stack_caracteres.pop()

        if(caracter == "."):
            return self.concatenacion()
        elif(caracter == "|"):
            return self.union()
        elif(caracter == "*"):
            return self.klenee()



    def unidad_estados(self, conector):

        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_inicial = self.contador_estados

        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_final = self.contador_estados

        transicion = [estado_inicial, conector, estado_final]
        self.transiciones.append(transicion)

        return estado_inicial, estado_final

    def concatenacion(self):
        caracter_1 = self.stack_caracteres.pop()
        caracter_2 = self.stack_caracteres.pop()

        if(caracter_1 in ".|*"):

            self.stack_caracteres.append(caracter_2)
            self.stack_caracteres.append(caracter_1)

            inicial_1, final_1 = self.construccionThompson()

            if(len(self.stack_caracteres) != 1):
                inicial_2, final_2 = self.construccionThompson()
            else:
                caracter_nuevo = self.stack_caracteres.pop()
                inicial_2, final_2 = self.unidad_estados(caracter_nuevo)

            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)

        elif(caracter_2 in ".|*"):

            self.stack_caracteres.append(caracter_2)

            inicial_1, final_1 = self.unidad_estados(caracter_1)
            inicial_2, final_2 = self.construccionThompson()

            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)

        else:
            inicial_1, final_1 = self.unidad_estados(caracter_1)
            inicial_2, final_2 = self.unidad_estados(caracter_2)
            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)

        return inicial_1, final_2
            
 
    def union(self):

        caracter_1 = self.stack_caracteres.pop()
        caracter_2 = self.stack_caracteres.pop()

        if(caracter_1 in ".|*"):

            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados
            self.estados.append(self.contador_estados)
            
            self.stack_caracteres.append(caracter_2)
            self.stack_caracteres.append(caracter_1)

            if(len(self.stack_caracteres) != 1):
                inicial_1, final_1 = self.construccionThompson()
            else:
                caracter_nuevo = self.stack_caracteres.pop()
                inicial_1, final_1 = self.unidad_estados(caracter_nuevo)

            inicial_2, final_2 = self.construccionThompson()

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados
            self.estados.append(self.contador_estados)

            transicion_1 = [estado_transicion_1, "ε", inicial_1]
            transicion_2 = [estado_transicion_1, "ε", inicial_2]
            transicion_3 = [final_1, "ε", estado_transicion_2]
            transicion_4 = [final_2, "ε", estado_transicion_2]

            self.transiciones.append(transicion_1)
            self.transiciones.append(transicion_2)
            self.transiciones.append(transicion_3)
            self.transiciones.append(transicion_4)

        elif(caracter_2 in ".|*"):
            
            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados
            self.estados.append(self.contador_estados)

            self.stack_caracteres.append(caracter_2)

            inicial_1, final_1 = self.construccionThompson()
            inicial_2, final_2 = self.unidad_estados(caracter_1)

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados
            self.estados.append(self.contador_estados)

            transicion_1 = [estado_transicion_1, "ε", inicial_1]
            transicion_2 = [estado_transicion_1, "ε", inicial_2]
            transicion_3 = [final_1, "ε", estado_transicion_2]
            transicion_4 = [final_2, "ε", estado_transicion_2]

            self.transiciones.append(transicion_1)
            self.transiciones.append(transicion_2)
            self.transiciones.append(transicion_3)
            self.transiciones.append(transicion_4)

        else:

            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados
            self.estados.append(self.contador_estados)

            inicial_1, final_1 = self.unidad_estados(caracter_2)
            inicial_2, final_2 = self.unidad_estados(caracter_1)

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados
            self.estados.append(self.contador_estados)

            transicion_1 = [estado_transicion_1, "ε", inicial_1]
            transicion_2 = [estado_transicion_1, "ε", inicial_2]
            transicion_3 = [final_1, "ε", estado_transicion_2]
            transicion_4 = [final_2, "ε", estado_transicion_2]

            self.transiciones.append(transicion_1)
            self.transiciones.append(transicion_2)
            self.transiciones.append(transicion_3)
            self.transiciones.append(transicion_4)

        return estado_transicion_1, estado_transicion_2

    def klenee(self):
        caracter_1 = self.stack_caracteres.pop()

        if(caracter_1 in ".|*"):
            
            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados
            self.estados.append(self.contador_estados)

            self.stack_caracteres.append(caracter_1)

            inicial_1, final_1 = self.construccionThompson()

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados
            self.estados.append(self.contador_estados)

            transicion_1 = [final_1, "ε", inicial_1]
            transicion_2 = [estado_transicion_1, "ε", inicial_1]
            transicion_3 = [final_1, "ε", estado_transicion_2]
            transicion_4 = [estado_transicion_1, "ε", estado_transicion_2]

            self.transiciones.append(transicion_1)
            self.transiciones.append(transicion_2)
            self.transiciones.append(transicion_3)
            self.transiciones.append(transicion_4)

        else:

            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados

            inicial_1, final_1 = self.unidad_estados(caracter_1)

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados

            transicion_1 = [final_1, "ε", inicial_1]
            transicion_2 = [estado_transicion_1, "ε", inicial_1]
            transicion_3 = [final_1, "ε", estado_transicion_2]
            transicion_4 = [estado_transicion_1, "ε", estado_transicion_2]

            self.transiciones.append(transicion_1)
            self.transiciones.append(transicion_2)
            self.transiciones.append(transicion_3)
            self.transiciones.append(transicion_4)

        return estado_transicion_1, estado_transicion_1

    def definir_Transiciones(self):

        for transicion in self.transiciones:
            elemento_1 = transicion[0]
            elemento_2 = transicion[2]

            transicion[0] = self.estados[len(self.estados) - elemento_2]
            transicion[2] = self.estados[len(self.estados) - elemento_1]