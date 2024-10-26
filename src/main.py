#!/usr/bin/env python3
import sys
from tokenizer import Tokenize
from parser import Parse
from common import variables, line


code = ""
if len(sys.argv) > 1:
    try:
        code = open(sys.argv[1], "r").read()
        for lines in code.split("\n"):
            variables.update(Parse(Tokenize(lines).tokens).return_vars())
            line += 1
    except Exception as e:
        print("Exception occurred: ", str(e))
else:
    while True:
        try:
            variables.update(Parse(Tokenize(input(">>> ")).tokens).return_vars())
        except Exception as e:
            print("Exception occurred: ", str(e))
