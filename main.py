from lexer import Lexer
from parser import Parser

# Input program to test
program = "print(3 + 4 - 2);"

# Step 1: Lexical Analysis
lexer = Lexer().get_lexer()
tokens = lexer.lex(program)

# Step 2: Parsing and Evaluation
parser = Parser()  # No need for mock objects here
parser.parse()
ast = parser.get_parser().parse(tokens)

# Step 3: Evaluate and Execute
ast.eval()
