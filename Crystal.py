################################
# Crystal Programming Language #
################################

#############
# Constants #
#############

DIGITS = "0123456789"

##########
# Tokens #
##########

TT_NEWLINE  =        "NEWLINE"
TT_INT      =	     "INT"
TT_FLOAT    =	   	 "FLOAT"
TT_PLUS     =	     "PLUS"
TT_MINUS    =		 "MINUS"
TT_MUL      =		 "MUL"
TT_DIV      =		 "DIV"
TT_POW      =		 "POW"
TT_LPAREN   =		 "LPAREN"
TT_RPAREN   =		 "RPAREN"
TT_LSQUARE  =		 "LSQUARE"
TT_RSQUARE  =		 "RSQUARE"
TT_NE       =		 "NE"

##############
# Main Class #
##############

class Crystal:
    def __init__(self, input_text):
        self.input_text = input_text
        self.index = 0
        self.current_token = None
        self.current_char = self.input_text[self.index]
        self.tokens = []
    def advance(self):
        self.index+=1
    def make_number(self):
        num_str = ""
        dot_count = 0
        while self.index < len(self.input_text) and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                if dot_count == 1: break
                dot_count += 1
                num_str += "."
            else: num_str += self.current_char
            self.advance()
        if dot_count == 0:return (TT_INT, int(num_str))
        if dot_count == 1:return (TT_FLOAT, float(num_str))
    def lexer(self):
        while self.index < len(self.input_text):
            self.current_char = self.input_text[self.index]
            if self.current_char in " \t":
                self.advance()

            elif self.current_char in ";\n":
                self.current_token = TT_NEWLINE
                self.advance()
            
            elif self.current_char in DIGITS:
                self.current_token = self.make_number()
                self.advance()

            elif self.current_char == "+":
                self.current_token = TT_PLUS
                self.advance()

            elif self.current_char == "-":
                self.current_token = TT_MINUS
                self.advance()
            
            elif self.current_char == "*":
                self.current_token = TT_MUL
                self.advance()
                
            elif self.current_char == "/":
                self.current_token = TT_DIV
                self.advance()
                
            elif self.current_char == "^":
                self.current_token = TT_POW
                self.advance()
                
            elif self.current_char == "(":
                self.current_token = TT_LPAREN
                self.advance()
                
            elif self.current_char == ")":
                self.current_token = TT_RPAREN
                self.advance()
                
            elif self.current_char == "[":
                self.current_token = TT_LSQUARE
                self.advance()
                
            elif self.current_char == "]":
                self.current_token = TT_RSQUARE
                self.advance()

            else:
                raise NameError(f"Invalid charater '{self.current_char}'")

            self.tokens.append(self.current_token)
        return self.tokens
