class Regex(object):

    def __init__(self, regex):
        self.expresion = regex
        self.operatorStack = []
        self.postfixExpresion = self.postfixRegex()
    
    '''
    Se convertira la expresion normal a notacion postfix 
    por orden de presedencia utilizando como referencia el 
    algoritmo Shunting-Yard.
    
    Ref: https://blog.cernera.me/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm/
    
    
    ''' 
    def jerarquia(self, char):
        if (char == '('):
            return 1
        elif (char == '|'):
            return 2
        elif (char == '.'):
            return 3
        elif (char == '?'):
            return 4
        elif (char == '*'):
            return 4
        elif (char == '+'):
            return 4
        else:
            return 5
        
        
    def postfixRegex(self):
        
        operators = ['|', '?', '+', '*']
        bin = ['|']
        
        queue = ""

        for l in range(len(self.expresion)):
            
            s = self.expresion[l]
            
            if ((l + 1) < len(self.expresion)):
                r = self.expresion[l + 1]
                queue += s

                if ((s != '(') and (r != ')') and (r not in operators) and (s not in bin)):
                    queue += '.'

        queue += self.expresion[len(self.expresion) - 1]

        postfix = ''
        
        for exp in queue:
            
            if (exp == '('):
                self.operatorStack.append(exp)
                
            elif (exp == ')'):
                while (self.operatorStack[-1] !='('):
                    postfix += self.operatorStack.pop()

                self.operatorStack.pop()
                
            else:
                while (len(self.operatorStack) > 0):
                    ultimoChar = self.operatorStack[-1]
                    observado = self.jerarquia(ultimoChar)
                    actual = self.jerarquia(exp)

                    if (observado >= actual):
                        postfix += self.operatorStack.pop()
                        
                    else:
                        break
                    
                self.operatorStack.append(exp)

        
        while (len(self.operatorStack) > 0):
            postfix += self.operatorStack.pop()
        
        return postfix
    