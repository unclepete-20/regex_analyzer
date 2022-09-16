class Regex(object):

    def __init__(self, expresion):
        self.expresion = expresion
        self.simbolos = []
        self.caracteres = self.regexCaracteres()

    def regexCaracteres(self):
        caracteres = []
        for caracter in self.expresion:
            if(caracter != '|' and caracter != '*' and caracter != 'ε'):
                caracteres.append(caracter)
            else:
                self.simbolos.append(caracter)
        return caracteres

    