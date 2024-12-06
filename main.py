# main.py
import sys
import os
from antlr4 import *
from MLDSLParser import MLDSLParser
from MLDSLLexer import MLDSLLexer
from MLDSLVisitorImpl import MLDSLVisitorImpl

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def main():
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        # Leer el archivo en UTF-8
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
        input_stream = InputStream(data)
        lexer = MLDSLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MLDSLParser(stream)
        tree = parser.program()
        visitor = MLDSLVisitorImpl()
        visitor.visit(tree)
    else:
        repl()

def repl():
    from antlr4 import InputStream, CommonTokenStream
    visitor = MLDSLVisitorImpl()
    print("Bienvenido a MLDSL REPL. Escribe 'exit' para salir.")
    while True:
        try:
            line = input('MLDSL> ')
            if line.strip() == 'exit':
                break
            input_stream = InputStream(line)
            lexer = MLDSLLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = MLDSLParser(stream)
            tree = parser.statement()
            visitor.visit(tree)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
