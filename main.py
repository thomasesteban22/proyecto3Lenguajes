import sys
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from MyVisitor import MyVisitor

def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
    else:
        print("Por favor, proporciona el archivo de entrada.")
        return

    lexer = gramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.program()
    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()