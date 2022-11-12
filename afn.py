# -*-coding:utf-8 -*-
'''
@File    :   afn.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188) y Oscar Lopez (20679)
@Version :   1.0
@Desc    :   Implementacion de construccion de AFN por medio de Thompson, subconjuntos y AFN => AFD
'''

class AFN(object):

    #Se inicializa la clase por medio de la expresion regular
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
        self.construccionThompson()
        self.definir_Transiciones()

    #Se hace la funcion de Thompson
    def construccionThompson(self):

        caracter = self.stack_caracteres.pop()

        #Dependiendo del caracter se realiza un procedimiento diferente debido a la construccion de cada uno
        if(caracter == "."):
            return self.concatenacion()
        elif(caracter == "|"):
            return self.union()
        elif(caracter == "*"):
            return self.klenee()
        elif(len(self.stack_caracteres) == 0):
            return self.unidad_estados(caracter)


    #Funcion que crea estados, los cuales son unificados por un conector o caracter
    def unidad_estados(self, conector):

        if(conector not in self.simbolos):
            self.simbolos.append(conector)

        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_inicial = self.contador_estados

        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_final = self.contador_estados

        transicion = [estado_inicial, conector, estado_final]
        self.transiciones.append(transicion)

        return estado_inicial, estado_final

    #Funcion que realiza la concatenacion
    def concatenacion(self):

        caracter_1 = self.stack_caracteres.pop()
        caracter_2 = self.stack_caracteres.pop()

        #Si la se encuentra en la expresion alguno de los operadores se realiza la recursion de la funcion de construccion
        if(caracter_1 in ".|*"):

            self.stack_caracteres.append(caracter_2)
            self.stack_caracteres.append(caracter_1)

            inicial_1, final_1 = self.construccionThompson()

            if(len(self.stack_caracteres) != 1):
                inicial_2, final_2 = self.construccionThompson()
            else:
                caracter_nuevo = self.stack_caracteres.pop()
                inicial_2, final_2 = self.unidad_estados(caracter_nuevo)

            #Se realizan las transiciones de los estados iniciales y finales con respecto a las contrucciones que se realizaron recursivamente
            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)

        #Se verifica nuevamente
        elif(caracter_2 in ".|*"):

            self.stack_caracteres.append(caracter_2)

            inicial_1, final_1 = self.unidad_estados(caracter_1)
            inicial_2, final_2 = self.construccionThompson()

            #Se realiza la transicion
            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)

        #Para casos simples se realiza esta opcion
        else:
            inicial_1, final_1 = self.unidad_estados(caracter_1)
            inicial_2, final_2 = self.unidad_estados(caracter_2)
            transicion = [final_1, "ε", inicial_2]
            self.transiciones.append(transicion)

        #Se regresan los estados final e inicial de la construccion, esto para la recursion
        return inicial_1, final_2
            
    #Funcion de la union
    def union(self):

        caracter_1 = self.stack_caracteres.pop()
        caracter_2 = self.stack_caracteres.pop()

        #Si la se encuentra en la expresion alguno de los operadores se realiza la recursion de la funcion de construccion
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

            #Se realizan las transiciones de los estados iniciales y finales con respecto a las contrucciones que se realizaron recursivamente
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

        #Se regresan los estados final e inicial de la construccion, esto para la recursion
        return estado_transicion_1, estado_transicion_2

    #Funcion de Klenee que realiza las operaciones unarias
    def klenee(self):

        #Se llama solo a un caracter
        caracter_1 = self.stack_caracteres.pop()

        #Se realiza la recursividad si se encuentra un operador
        if(caracter_1 in ".|*"):
            
            self.contador_estados += 1
            estado_transicion_1 = self.contador_estados
            self.estados.append(self.contador_estados)

            self.stack_caracteres.append(caracter_1)

            inicial_1, final_1 = self.construccionThompson()

            self.contador_estados += 1
            estado_transicion_2 = self.contador_estados
            self.estados.append(self.contador_estados)
            
            #Se realizan todas las transiciones siguiendo la forma de la construccion
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

        #Se retornan los estados final e inicial para la recursividad
        return estado_transicion_1, estado_transicion_2

    #Con esta funcion se da "vuelta" a las transiciones debido a que los estados van a N a 1
    #Con esto se consigue que los estados vayan de 1 a N
    def definir_Transiciones(self):

        self.estado_inicial.append(1)
        self.estados_aceptacion.append(self.contador_estados)

        for transicion in self.transiciones:
            elemento_1 = transicion[0]
            elemento_2 = transicion[2]

            transicion[0] = self.estados[len(self.estados) - elemento_2]
            transicion[2] = self.estados[len(self.estados) - elemento_1]
    
    #Se realiza la simulacion mediante el algoritmo
    def simulacion(self, cadena):

        #Se realiza el algoritmo visto en clase utilizando e-closure y move
        contador = 0
        estados = self.e_closure(self.estado_inicial)
        while(contador < len(cadena)):
            caracter = cadena[contador]
            estados = self.e_closure(self.move(estados, caracter))
            contador += 1
        set_estados = set(estados)
        set_finales = set(self.estados_aceptacion)
        if(set_estados.intersection(set_finales).__len__() != 0):
            return "Cadena Aceptada"
        else:
            return "Cadena No Aceptada"
    
    #Se realiza la conversion del afn a afd mediante el algoritmo
    def convertir_afd(self):

        #Se utiliza el algoritmo visto en clase con e-closure y move
        estados_afd = ["E0"]
        d_estados = [self.e_closure(self.estado_inicial)]
        transiciones_afd = []
        estado_inicial_afd = [d_estados[0]]
        estado_final_afd = [d_estados[len(d_estados) - 1]]
        contador = 0
        while(contador != len(d_estados)):
            for simbolo in self.simbolos:
                nuevo_estado = self.e_closure(self.move(d_estados[contador], simbolo))
                if(nuevo_estado not in d_estados):
                    d_estados.append(nuevo_estado)
                    transiciones_afd.append([estados_afd[contador], simbolo, "E"+str(len(estados_afd))])
                    estados_afd.append("E"+str(len(estados_afd)))
                else:
                    transiciones_afd.append([estados_afd[contador], simbolo, estados_afd[contador]])
            contador += 1     

        return estados_afd, transiciones_afd, estado_final_afd, estado_inicial_afd

    #Se realiza la funcion e-closure con el algoritmo visto
    def e_closure(self, estados):

        stack_estados = list(estados)
        resultado = list(estados)
        while(len(stack_estados) != 0):
            estado = stack_estados.pop()
            for i in self.transiciones:
                if(i[0] == estado and i[1] == "ε"):
                    if(i[2] not in resultado):
                        resultado.append(i[2])
                        stack_estados.append(i[2])
        
        return resultado

    #Se regresa la funcion de move con el mismo algoritmo de e-closure, en este caso buscando un caracter
    def move(self, estados, caracter):

        stack_estados = list(estados)
        resultado = []

        while(len(stack_estados) != 0):
            estado = stack_estados.pop()
            for i in self.transiciones:
                if(i[0] == estado and i[1] == caracter):
                    if(i[2] not in resultado):
                        resultado.append(i[2])
                        stack_estados.append(i[2])

        return resultado

    #Se realiza un archivo txt
    def archivo_txt(self, nombre, simbolos, estado_inicial, estados, estados_aceptacion, transiciones):
        with open(nombre,"w", encoding="utf-8") as file:
            file.write("\nAFD DIRECTO CONSTRUIDO POR PEDRO ARRIOLA (20188) Y OSCAR LOPEZ (20679)\n")
            file.write("\n -- CARACTERES DEL ALFABETO --\n")
            file.write(" => " + str(simbolos) + "\n")
            file.write("\n -- ESTADO INICIAL --\n")
            file.write(" => " + str(estado_inicial) + "\n")
            file.write("\n -- ESTADOS DEL AUTOMATA --\n")
            for state in estados:
                file.write("      " + str(state) + "\n")
            file.write("\n -- ESTADOS DE ACEPTACION --\n")
            file.write(" => " + str(estados_aceptacion) + "\n")
            file.write("\n -- TRANSICIONES --\n")
            for i in transiciones:
                transicion = str(i[0]) + "=> " + i[1] + " => " + str(i[2]) + "\n"
                file.write(transicion)
            file.close()