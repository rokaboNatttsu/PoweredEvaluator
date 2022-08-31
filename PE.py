from math import exp, log, sqrt, sin, cos, log10, log2

class PowerdEvalator:
    def __init__(self, eq):
        self.substituted_variables = set()
        self.eq = eq
        self.existing_operators = []
        self.vdic = {}
        self.variables_name_set = set()
        self.find_operator()


    def find_operator(self):
        developing_operators = ["exp", "log", "sqrt", "sin", "cos", "log10", "log2"]
        primary_operators = ["+", "-", "*", "/", "**", "//", "%"]
        parenthesis_operators = ["(", ")", "[", "]"]
        existing_operators = [False]*len(self.eq)
        for start in range(len(self.eq)):
            if self.eq[start] in parenthesis_operators:
                existing_operators[start] = True
                continue
            for stop in range(start+1, len(self.eq)+1):
                if self.eq[start:stop] in developing_operators:
                    for i in range(start, stop):
                        existing_operators[i] = True
                if self.eq[start:stop] in primary_operators:
                    for i in range(start, stop):
                        existing_operators[i] = True
        self.existing_operators = existing_operators
    

    def find_variables(self):
        self.find_operator()
        existing_variables = [self.existing_operators[i] == False for i in range(len(self.existing_operators))]
        variables_name_set = set()
        variable_name = ""
        for i, TF in enumerate(existing_variables):
            if TF and self.eq[i] != " ":
                variable_name += self.eq[i]
            else:
                if variable_name != "" and not variable_name.isdecimal():
                    variables_name_set.add(variable_name)
                variable_name = ""
        self.variables_name_set = variables_name_set


    def substitute(self, vdic={}):
        if vdic:
            self.vdic = vdic
        else:
            return self.eq
        for v in self.vdic:
            if (v in self.eq) and (v not in self.substituted_variables):
                self.substituted_variables.add(v)
                index = 0
                self.find_operator()
                part_eqs = list(self.eq.split(v))
                new_eq = ""
                for part_eq in part_eqs:
                    index += len(part_eq)
                    if any(self.existing_operators[index:index+len(v)]):
                        new_eq += part_eq + v
                    else:
                        new_eq += part_eq + "(" + str(self.vdic[v]) + ")"
                    index += len(v)
                new_eq = new_eq[:-len(str(self.vdic[v]))-2]
                self.eq = new_eq
                
        return self.eq
                

    def evaluate(self, partrial_eq=None):
        if partrial_eq is None:
            partrial_eq = self.eq
        elif partrial_eq == "":
            return ""
        operators = ["exp", "log", "sqrt", "sin", "cos", "log10", "log2"]
        for opr in operators:
            if opr + "[" in partrial_eq:
                start, stop = None, None
                for i in range(len(partrial_eq) - len(opr + "[")):
                    if partrial_eq[i:i+len(opr + "[")] == opr + "[":
                        start = i + len(opr + "[")
                        break
                counter = 1
                for j in range(start+1, len(partrial_eq)):
                    if partrial_eq[j] == "[":
                        counter += 1
                    elif partrial_eq[j] == "]":
                        counter -= 1
                    if partrial_eq[j] == "]" and counter == 0:
                        stop = j
                        break
                
                if opr == "exp":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(exp(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
                elif opr == "log":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(log(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
                elif opr == "sqrt":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(sqrt(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
                elif opr == "sin":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(sin(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
                elif opr == "cos":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(cos(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
                elif opr == "log10":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(log10(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
                elif opr == "log2":
                    partrial_eq = partrial_eq[:start-len(opr + "[")] + "(" + str(log2(self.evaluate(partrial_eq=partrial_eq[start:stop]))) + ")" + partrial_eq[j+1:]
        
        return eval(partrial_eq)


    def direct_substitute(self, **args):
        if args is not None:
            self.vdic = args
        for v in self.vdic:
            if (v in self.eq) and (v not in self.substituted_variables):
                self.substituted_variables.add(v)
                index = 0
                self.find_operator()
                part_eqs = list(self.eq.split(v))
                new_eq = ""
                for part_eq in part_eqs:
                    index += len(part_eq)
                    if any(self.existing_operators[index:index+len(v)]):
                        new_eq += part_eq + v
                    else:
                        new_eq += part_eq + str(self.vdic[v])
                    index += len(v)
                new_eq = new_eq[:-len(str(self.vdic[v]))]
                self.eq = new_eq
                
        return self.eq
    

    def interactive_substitute(self):
        self.find_variables()
        for variable_name in self.variables_name_set - self.substituted_variables:
            value = float(input("input value of "+variable_name+" : "))
            self.vdic[variable_name] = value
        self.substitute(vdic=self.vdic)




if "__name__" == __name__:
    eq = input("input equation : ")
    evaluator = PowerdEvalator(eq)
    evaluator.interactive_substitute()
    print("substituted equation :",evaluator.eq)
    print(evaluator.evaluate())


"""実行サンプル

vdic = {
    "a":10,
    "b":2,
    "x":100,
    "y":10,
}
eq = "a*log[x]+b*exp[y]"
eq2 = "sin[a*x]**2 + cos[a*x]**2"
eq3 = "1 + 2 * 3 / 4 - 5"

evaluator = PowerdEvalator(eq3)
print(evaluator.eq)
evaluator.substitute(vdic)
print(evaluator.evaluate())


"""


