from tokenTypes import Tokens


class Tokenize:
    def __init__(self, code):
        self.code = code.split(" ")
        self.keyword = None
        self.tokens = self.tokenize()

    def tokenize(self):
        tokens = []
        match self.code[0]:
            case "PRINT":
                self.keyword = Tokens.PRINT
            case "ADD":
                self.keyword = Tokens.ADD
            case "SUB":
                self.keyword = Tokens.SUB
            case "MUL":
                self.keyword = Tokens.MUL
            case "DIV":
                self.keyword = Tokens.DIV
            case "ASSIGN":
                self.keyword = Tokens.ASSIGN
            case "REPLACE":
                self.keyword = Tokens.REPLACE
            case "USE":
                self.keyword = Tokens.USE
            case "TOSTRING":
                self.keyword = Tokens.TOSTRING
            case "TONUMBER":
                self.keyword = Tokens.TONUMBER
            case "EXIT":
                self.keyword = Tokens.EXIT
            case "//":
                self.keyword = Tokens.NOTE
            case _:
                if self.code[0] == "":
                    pass
                else:
                    self.keyword = Tokens.ILLEGAL

        for token in range(1, len(self.code)):
            tokens.append(self.code[token])
        return {"KEYWORD": self.keyword, "TOKENS": tokens}
