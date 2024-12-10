# ErrorListener.py

from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self, output_file):
        super(MyErrorListener, self).__init__()
        self.output = output_file

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error de sintaxis en línea {line}, columna {column}: {msg}"
        self.output.write(error_message + '\n')
        print(error_message)  # Para depuración en consola
