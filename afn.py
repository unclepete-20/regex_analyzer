class AFN(object):

    def __init__(self, regex):
        self.regex = regex
        self.regex_postfix = regex.postfixExpresion
        self.contador_estados = 0
        self.estados = []
        self.transiciones = []
        self.inicio = []
        self.aceptacion = []
        self.simbolos = []
        self.construccionThompson()
    
    #ARREGLAR STRING SOLO, ej: a

    def construccionThompson(self):
        stack_caracteres = []
        for caracter in self.regex_postfix:
            if(caracter == "."):
                self.concatenacion(stack_caracteres.pop(0))
            else:
                stack_caracteres.append(caracter)

    def concatenacion(self, exp):
        
        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_inicial = self.contador_estados

        self.contador_estados += 1
        self.estados.append(self.contador_estados)
        estado_final = self.contador_estados

        transicion = [estado_inicial, exp, estado_final]
        self.transiciones.append(transicion)

