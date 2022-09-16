class Regex(object):

    def __init__(self, expresion):
        self.expresion = expresion
        self.caracteres = self.regexCaracteres()
    
    def regexCaracteres(self):
        for caracter in self.expresion:
            if(caracter != ('|' or '*' or 'ε')):
                print(caracter)