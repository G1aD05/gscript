import random
from tokenTypes import Tokens
from common import *
import urllib.request
import re
import time
from tokenizer import Tokenize


class Parse:
    def __init__(self, tokens):
        self.line = line
        self.tokens = tokens
        self.index = 0
        self.variables = variables
        self.runtime_vars = {}
        self.parse()

    def parse(self):
        if self.tokens["KEYWORD"] == Tokens.ILLEGAL:
            print(f"Invalid keyword found at line {self.line + 1}")
            exit(0)

        elif self.tokens["KEYWORD"] == Tokens.PRINT:
            print(str(self.parse_variable(self.tokens["TOKENS"][self.index])))

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
            self.variables[self.tokens["TOKENS"][self.index]] = self.tokens["TOKENS"][self.index + 1]

        elif self.tokens["KEYWORD"] == Tokens.REPLACE:
            self.variables[self.tokens["TOKENS"][self.index]] = self.parse_variable(self.tokens["TOKENS"][self.index + 3]).replace(self.parse_variable(str(self.tokens["TOKENS"][self.index + 1])), self.parse_variable(str(self.tokens["TOKENS"][self.index + 2])))

        elif self.tokens["KEYWORD"] == Tokens.TOSTRING:
            self.variables[self.tokens["TOKENS"][self.index]] = str(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.TONUMBER:
            self.variables[self.tokens["TOKENS"][self.index]] = float(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.READ:
            self.variables[self.tokens["TOKENS"][self.index]] = open(self.parse_variable(self.tokens["TOKENS"][self.index + 1]), "r").read()

        elif self.tokens["KEYWORD"] == Tokens.WRITE:
            open(self.tokens["TOKENS"][self.index], 'w').write(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.INPUT:
            self.variables[self.tokens["TOKENS"][self.index]] = input(self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.DOWNLOAD:
            urllib.request.urlretrieve(self.parse_variable(self.tokens["TOKENS"][self.index]), self.parse_variable(self.tokens["TOKENS"][self.index + 1]))

        elif self.tokens["KEYWORD"] == Tokens.JOIN:
            self.variables[self.tokens["TOKENS"][self.index]] = self.parse_variable(self.tokens["TOKENS"][self.index + 1]) + (self.parse_variable(self.tokens["TOKENS"][self.index + 2]))

        elif self.tokens["KEYWORD"] == Tokens.RANDOM:
            self.variables[self.tokens["TOKENS"][self.index]] = random.randint(int(self.parse_variable(self.tokens["TOKENS"][self.index + 1])), int(self.parse_variable(self.tokens["TOKENS"][self.index + 2])))

        elif self.tokens["KEYWORD"] == Tokens.WAIT:
            time.sleep(int(self.parse_variable(self.tokens["TOKENS"][self.index])))

        elif self.tokens["KEYWORD"] == Tokens.RUN:
            code = open(self.tokens["TOKENS"][self.index], "r").read()
            self.runtime_vars = self.variables.copy()
            for lines in code.split("\n"):
                self.variables.update(Parse(Tokenize(lines.strip()).tokens).return_vars())

            self.variables.clear()
            self.variables = self.runtime_vars

        elif self.tokens["KEYWORD"] == Tokens.EXIT:
            exit(0)

        elif self.tokens["KEYWORD"] == Tokens.NOTE:
            pass

    def return_vars(self):
        return self.variables

    def parse_variable(self, variable):
        if "%" in variable:
            pattern = r'(%\w+)'

            # Function to replace based on dictionary
            def replace_match(match):
                key = match.group(0)
                return str(self.variables.get(key[1:], key[1:]))

            # Replace matching words based on dictionary
            result = re.sub(pattern, replace_match, variable)
            return result
        else:
            return variable
