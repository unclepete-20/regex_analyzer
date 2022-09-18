class AFN(object):

    def __init__(self, regex):
        self.regex = regex
        self.regex_postfix = regex.postfixExpresion
        self.contador_estados = 0
        self.estados = []
        self.transiciones = []
        self.estado_inicial = []
        self.estados_aceptacion = []
        self.simbolos = []
        self.estado_inicio = 0
        self.construccionThompson()
    
    #ARREGLAR STRING SOLO, ej: a

    def construccionThompson(self):
        stack_caracteres = []
        for caracter in self.regex_postfix:
            print(stack_caracteres)
            if(caracter == "."):
                self.concatenacion()
            else:
                stack_caracteres.append(caracter)

    def unidad_estados(self, conector):

        if(estado_inicial != 0):
            self.estados.append(self.contador_estados)

        estado_inicial = self.contador_estados

        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_final = self.contador_estados

        transicion = [estado_inicial, conector, estado_final]
        self.transiciones.append(transicion)

    def concatenacion(self, exp_1, exp_2):
        pass

    def union():
        pass

    def klenee():
        pass