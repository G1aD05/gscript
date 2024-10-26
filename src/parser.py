from tokenTypes import Tokens
from common import line, variables


class Parse:
    def __init__(self, tokens):
        self.line = line
        self.tokens = tokens
        self.index = 0
        self.variables = variables
        self.parse()

    def parse(self):
        join = ""
        if self.tokens["KEYWORD"] == Tokens.ILLEGAL:
            print(f"Invalid keyword found at line {self.line + 1}")
            exit(0)

        elif self.tokens["KEYWORD"] == Tokens.PRINT:
            self.index += 1
            for token in range(len(self.tokens["TOKENS"])):
                join += str(self.parse_variable(self.tokens["TOKENS"][token])) + " "
            print(join)

        elif self.tokens["KEYWORD"] == Tokens.ADD:
            sum = int(self.parse_variable(self.tokens["TOKENS"][self.index])) + int(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))
            self.index = 2
            self.variables[self.tokens["TOKENS"][self.index]] = sum

        elif self.tokens["KEYWORD"] == Tokens.SUB:
            difference = int(self.parse_variable(self.tokens["TOKENS"][self.index])) - int(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))
            self.index = 2
            self.variables[self.tokens["TOKENS"][self.index]] = difference

        elif self.tokens["KEYWORD"] == Tokens.MUL:
            product = int(self.parse_variable(self.tokens["TOKENS"][self.index])) * int(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))
            self.index = 2
            self.variables[self.tokens["TOKENS"][self.index]] = product

        elif self.tokens["KEYWORD"] == Tokens.DIV:
            quotient = int(self.parse_variable(self.tokens["TOKENS"][self.index])) / int(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))
            self.index = 2
            self.variables[self.tokens["TOKENS"][self.index]] = quotient

        elif self.tokens["KEYWORD"] == Tokens.ASSIGN:
            for token in range(1, len(self.tokens["TOKENS"])):
                join += str(self.parse_variable(self.tokens["TOKENS"][token])) + " "
            self.variables[self.tokens["TOKENS"][self.index]] = join

        elif self.tokens["KEYWORD"] == Tokens.REPLACE:
            for token in range(3, len(self.tokens["TOKENS"])):
                join += str(self.parse_variable(self.tokens["TOKENS"][token])) + " "
            self.variables[self.tokens["TOKENS"][self.index]] = join.replace(self.parse_variable(str(self.tokens["TOKENS"][self.index + 1])), self.parse_variable(str(self.tokens["TOKENS"][self.index + 2])))

        elif self.tokens["KEYWORD"] == Tokens.USE:
            pass

        elif self.tokens["KEYWORD"] == Tokens.TOSTRING:
            self.variables[self.tokens["TOKENS"][self.index]] = str(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.TONUMBER:
            self.variables[self.tokens["TOKENS"][self.index]] = float(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.EXIT:
            exit(0)

        elif self.tokens["KEYWORD"] == Tokens.NOTE:
            pass

    def return_vars(self):
        return self.variables

    def parse_variable(self, variable):
        if variable.startswith("%"):
            return self.variables[variable[1:]]
        else:
            return variable
