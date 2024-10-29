#!/usr/bin/env python3
import sys
from tokenizer import Tokenize
from parser import Parse
from common import public
from colorama import Fore, Style


code = ""
if len(sys.argv) > 1:
    try:
        code = open(sys.argv[1], "r").read()
        for lines in code.split("\n"):
            public.variables.update(Parse(Tokenize(lines.strip()).tokens).return_vars())
            public.line += 1
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "Exception occurred: ", str(e) + Style.REST_ALL)
        exit(1)
else:
    console = True
    while True:
        try:
            public.variables.update(Parse(Tokenize(input(">>> ").strip()).tokens).return_vars())
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + "Exception occurred: ", str(e) + Style.REST_ALL)
