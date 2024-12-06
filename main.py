# main.py

import sys
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from MyVisitor import MyVisitor
from ErrorListener import MyErrorListener

def main():
    try:
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
            input_stream = FileStream(input_file, encoding='utf-8')
        else:
            print("Por favor, proporciona el archivo de entrada.")
            return

        lexer = gramaticaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = gramaticaParser(stream)

        with open('output.txt', 'w') as output_file:
            # Añadir el Error Listener personalizado
            error_listener = MyErrorListener(output_file)
            parser.removeErrorListeners()  # Remover listeners por defecto
            parser.addErrorListener(error_listener)

            tree = parser.program()

            # Verificar si hubo errores de sintaxis
            if output_file.tell() == 0:
                visitor = MyVisitor(output_file)
                visitor.visit(tree)
            else:
                print("Se encontraron errores de sintaxis. Revisar output.txt para más detalles.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
