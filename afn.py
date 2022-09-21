from typing import List


class AFN(object):

    def __init__(self, regex):
        self.regex = regex
        self.regex_postfix = regex.postfixExpresion
        self.stack_caracteres = list(self.regex_postfix)
        self.contador_estados = 0
        self.estados = []
        self.transiciones = []
        self.estado_inicial = []
        self.estados_aceptacion = []
        self.simbolos = []
        self.estado_inicio = 0
        self.estado_final = 0
        self.construccionThompson()
    
    #ARREGLAR STRING SOLO, ej: a

    def construccionThompson(self):

        while len(self.stack_caracteres) != 0:
            caracter = self.stack_caracteres.pop()
            
            if(caracter == "."):
                self.concatenacion()
            elif(caracter == "|"):
                self.union()
            elif(caracter == "*"):
                self.klenee()

    def construccionThompson_Interna(self, stack):

        while len(stack) != 0:
            caracter = stack.pop()
            
            if(caracter == "."):
                self.concatenacion()
            elif(caracter == "|"):
                self.union()
            elif(caracter == "*"):
                self.klenee()
                

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

        if(caracter_1 in ".|"):
            pass
        elif(caracter_2 in ".|"):
            pass
        elif(caracter_1 in ".|" and caracter_2 in ".|"):
            pass
        else:
            inicial_1, final_1 = self.unidad_estados(caracter_1)
            inicial_2, final_2 = self.unidad_estados(caracter_2)
            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)
            
 
    def union(self):

        caracter_1 = self.stack_caracteres.pop()
        caracter_2 = self.stack_caracteres.pop()

        if(caracter_1 in ".|"):
            pass
        elif(caracter_2 in ".|"):
            pass
        elif(caracter_1 in ".|" and caracter_2 in ".|"):
            pass
        else:

            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados

            inicial_1, final_1 = self.unidad_estados(caracter_1)
            inicial_2, final_2 = self.unidad_estados(caracter_2)

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados

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

        if(caracter_1 in ".|"):
            pass
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

        return estado_transicion_1, estado_transicion_2