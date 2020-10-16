import math

var = []
val = []




class Syntax:
    # implement your syntaxes here
    # ... or derive subclasses and implement there
    def charsToSyntaxes(symbols):
        global var, val
        symbols = symbols.replace('\n', ' ')
        symbols = symbols.replace('\r', ' ')
        symbols = symbols.replace('\t', ' ')
        symbols = symbols.replace('(', ' ( ')
        symbols = symbols.replace(')', ' ) ')
        symbols = symbols.split()
        for i in range(len(symbols)):
            if symbols[i] == 'apply':
                var.append(symbols[i+1])
                ii = i + 3
                temp = []
                score = 1
                while symbols[ii] != ')':
                    temp.append(symbols[ii])
                    ii += 1
                val.append(temp)
        return symbols
    def __hash__(self):
        # implement your hash algorithm for the symbols here
        # you may make use of the default hash algorithms of strings, numbers, etc.
        pass
    def __eq__(self, rhs):
        # implement your syntax equality determination here
        pass
    pass

class EvaluationContext:

    def __init__(self, prev):

        self.prev = prev

    def store(self, name, value):

        setattr(self, name, value)

    def load(self, name):
        
        obj = self

        while obj:

            if hasattr(obj, name):

                return getattr(obj, name)

            else:
                
                obj = obj.prev
        
        return None

    def push(self):
        
        empty = EvaluationContext(self)

        return empty

    def pop(self):
        
        return self.prev

class ASTNode:
    # implement your AST Nodes here
    # ... or derive subclasses and give actual implementations there

    def evaluate(astlist):

        global var, val
        if type(astlist) == list:

            if astlist[0] == 'numi':
                return int(astlist[1])

            elif astlist[0] == 'numf':
                return float(astlist[1])

            elif astlist[0] == 'neg':
                if type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float:
                    return -ASTNode.evaluate(astlist[1])
                elif ASTNode.evaluate(astlist[1]) in var:
                    return -ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))])
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    return astlist

            elif astlist[0] == 'sin':

                if type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float:
                    return math.sin(ASTNode.evaluate(astlist[1]))
                elif ASTNode.evaluate(astlist[1]) in var:
                    return math.sin(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]))
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    return astlist

            elif astlist[0] == 'cos':
                if type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float:
                    return math.cos(ASTNode.evaluate(astlist[1]))
                elif ASTNode.evaluate(astlist[1]) in var:
                    return math.cos(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]))
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    return astlist

            elif astlist[0] == 'exp':
                if type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float:
                    return math.exp(ASTNode.evaluate(astlist[1]))
                elif ASTNode.evaluate(astlist[1]) in var:
                    return math.exp(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]))
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    return astlist

            elif astlist[0] == '+':
                if (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    return ASTNode.evaluate(astlist[1]) + ASTNode.evaluate(astlist[2])
                elif (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (ASTNode.evaluate(astlist[2]) in var):
                    return ASTNode.evaluate(astlist[1]) + ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])
                elif (ASTNode.evaluate(astlist[1]) in var) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    return ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]) + ASTNode.evaluate(astlist[2])
                elif (ASTNode.evaluate(astlist[1]) in var) and (ASTNode.evaluate(astlist[2]) in var):
                    return ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]) + ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    astlist[2] = ASTNode.evaluate(astlist[2])
                    return astlist

            elif astlist[0] == '-':
                if (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    return ASTNode.evaluate(astlist[1]) - ASTNode.evaluate(astlist[2])
                elif (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (ASTNode.evaluate(astlist[2]) in var):
                    return ASTNode.evaluate(astlist[1]) - ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])
                elif (ASTNode.evaluate(astlist[1]) in var) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    return ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]) - ASTNode.evaluate(astlist[2])
                elif (ASTNode.evaluate(astlist[1]) in var) and (ASTNode.evaluate(astlist[2]) in var):
                    return ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]) - ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    astlist[2] = ASTNode.evaluate(astlist[2])
                    return astlist

            elif astlist[0] == '*':
                if (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    return ASTNode.evaluate(astlist[1]) * ASTNode.evaluate(astlist[2])
                elif (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (ASTNode.evaluate(astlist[2]) in var):
                    return ASTNode.evaluate(astlist[1]) * ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])
                elif (ASTNode.evaluate(astlist[1]) in var) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    return ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]) * ASTNode.evaluate(astlist[2])
                elif (ASTNode.evaluate(astlist[1]) in var) and (ASTNode.evaluate(astlist[2]) in var):
                    return ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]) * ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    astlist[2] = ASTNode.evaluate(astlist[2])
                    return astlist

            elif astlist[0] == 'pow':
                if (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    if (type(ASTNode.evaluate(astlist[1])) == int) and (type(ASTNode.evaluate(astlist[2])) == int):
                        return int(math.pow(ASTNode.evaluate(astlist[1]), ASTNode.evaluate(astlist[2])))
                    return math.pow(ASTNode.evaluate(astlist[1]), ASTNode.evaluate(astlist[2]))
                elif (type(ASTNode.evaluate(astlist[1])) == int or type(ASTNode.evaluate(astlist[1])) == float) and (ASTNode.evaluate(astlist[2]) in var):
                    if (type(ASTNode.evaluate(astlist[1])) == int) and (type(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])) == int):
                        return int(math.pow(ASTNode.evaluate(astlist[1]), ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])))
                    return math.pow(ASTNode.evaluate(astlist[1]), ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))]))
                elif (ASTNode.evaluate(astlist[1]) in var) and (type(ASTNode.evaluate(astlist[2])) == int or type(ASTNode.evaluate(astlist[2])) == float):
                    if (type(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))])) == int) and (type(ASTNode.evaluate(astlist[2])) == int):
                        return int(math.pow(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]), ASTNode.evaluate(astlist[2])))
                    return math.pow(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]), ASTNode.evaluate(astlist[2]))
                elif (ASTNode.evaluate(astlist[1]) in var) and (ASTNode.evaluate(astlist[2]) in var):
                    if (type(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))])) == int) and (type(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])) == int):
                        return int(math.pow(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]), ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))])))
                    return math.pow(ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[1]))]), ASTNode.evaluate(val[var.index(ASTNode.evaluate(astlist[2]))]))
                else:
                    astlist[1] = ASTNode.evaluate(astlist[1])
                    astlist[2] = ASTNode.evaluate(astlist[2])
                    return astlist

            elif astlist[0] == 'apply':
                val[var.index(astlist[1])] = ASTNode.evaluate(astlist[2])
                return ASTNode.evaluate(astlist[3])

            elif astlist[0] == 'lambda':
                if astlist[1] in var:
                    return ASTNode.evaluate(astlist[2])
                else:
                    return [astlist[0], astlist[1], ASTNode.evaluate(astlist[2])]

        else:
            if astlist in var:
                return ASTNode.evaluate(val[var.index(astlist)])
            else:
                return astlist


class AST:
    def __init__(self, ASTlist):

        self.ASTlist = ASTlist

    def syntaxesToAST(syntaxes):
        for i in range(len(syntaxes)):
            if '(' in syntaxes[i + 1:]:
                pass
            else:
                for ii in range(i + 1, len(syntaxes)):
                    if syntaxes[ii] == ')':
                        temp = syntaxes[i + 1 : ii]
                        del syntaxes[i:ii+1]
                        syntaxes.insert(i, temp)
                        return AST.syntaxesToAST(syntaxes)
        return AST(syntaxes[0])

    def evaluate(self, eval_context):
        return ASTNode.evaluate(self.ASTlist)



class Evaluator:
    # implement your evaluator here
    def getInputAsChars(self):
        # retrieve the input as characters from the input file here
        # ... generator is greatly recommended.
        with open('input.txt', 'r') as f:
            return f.read()
    def evaluate(self):

        global var, val

        chars = self.getInputAsChars()
        syntaxes = Syntax.charsToSyntaxes(chars)
        ast = AST.syntaxesToAST(syntaxes)
        ec = EvaluationContext(None)
        return ast.evaluate(ec)
    def stringifyResult(self, result):
        if type(result) == int:
            return ('(' + 'numi ' + str(result) + ')')
        elif type(result) == float:
            result = format(result, '.5f')
            return ('(' + 'numf ' + result + ')')
        elif type(result) == list:
            result = str(result)
            result = result.replace('\'', '')
            result = result.replace('[', ' ( ')
            result = result.replace(']', ' ) ')
            result = result.replace(',', ' ')
            result = result.split()
            result = result[1:-1]
            i = 0
            while i < len(result):
                if result[i].isdigit():
                    result[i:i+1] = ['(', 'numi', result[i], ')']
                    i += 2
                    
                elif '.' in result[i]:
                    result[i] = float(result[i])
                    result[i] = str(format(result[i], '.5f'))
                    result[i:i+1] = ['(', 'numf', result[i], ')']
                    i += 2
                i += 1
                    
            result = '(' + ' '.join(result) +')'
            result = result.replace('( ', '(')
            result = result.replace(' )', ')')
            return result


            
    def writeOutput(self, s):
        with open('output.txt', 'w') as f:
            f.write(s)


if __name__ == "__main__":
    evaluator = Evaluator()
    result = evaluator.evaluate()
    s = evaluator.stringifyResult(result)
    evaluator.writeOutput(s)
