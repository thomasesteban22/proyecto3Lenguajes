from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor
import matplotlib.pyplot as plt
import numpy as np


class MyVisitor(gramaticaVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx: gramaticaParser.ProgramContext):
        print("Visiting Program")
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: gramaticaParser.StatementContext):
        print("Visiting Statement")
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: gramaticaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.memory[var_name] = value
        print(f"Assigned: {var_name} = {value}")
        return value

    # Métodos para cada tipo de expresión
    def visitExponentiation(self, ctx: gramaticaParser.ExponentiationContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        result = left ** right
        print(f"Exponentiation: {left} ^ {right} = {result}")
        return result

    def visitMultiplicative(self, ctx: gramaticaParser.MultiplicativeContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            result = left * right
            print(f"Multiplicative: {left} * {right} = {result}")
            return result
        elif op == '/':
            if right != 0:
                result = left / right
                print(f"Divisional: {left} / {right} = {result}")
                return result
            else:
                print("Error: División por cero")
                return 0
        elif op == '%':
            result = left % right
            print(f"Modulo: {left} % {right} = {result}")
            return result

    def visitAdditive(self, ctx: gramaticaParser.AdditiveContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            result = left + right
            print(f"Additive: {left} + {right} = {result}")
            return result
        elif op == '-':
            result = left - right
            print(f"Subtractive: {left} - {right} = {result}")
            return result

    def visitParentheses(self, ctx: gramaticaParser.ParenthesesContext):
        result = self.visit(ctx.expression())
        print(f"Parentheses: ({result})")
        return result

    def visitFunctionCallExpr(self, ctx: gramaticaParser.FunctionCallExprContext):
        return self.visitFunctionCall(ctx.functionCall())

    def visitMatrixOperationExpr(self, ctx: gramaticaParser.MatrixOperationExprContext):
        return self.visitMatrixOperation(ctx.matrixOperation())

    def visitNumberExpr(self, ctx: gramaticaParser.NumberExprContext):
        value = float(ctx.NUMBER().getText())
        print(f"Number: {value}")
        return value

    def visitIdExpr(self, ctx: gramaticaParser.IdExprContext):
        var_name = ctx.ID().getText()
        value = self.memory.get(var_name, 0)
        print(f"Variable: {var_name} = {value}")
        return value

    def visitFunctionCall(self, ctx: gramaticaParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.arguments():
            args = [self.visit(arg) for arg in ctx.arguments().expression()]
        print(f"Function Call: {func_name}({', '.join(map(str, args))})")

        if func_name == 'sin':
            return np.sin(args[0])
        elif func_name == 'cos':
            return np.cos(args[0])
        elif func_name == 'tan':
            return np.tan(args[0])
        elif func_name == 'sqrt':
            return np.sqrt(args[0])
        elif func_name == 'print':
            # 'print' es manejado por visitPrintStatement
            return None
        else:
            print(f"Función '{func_name}' no definida.")
            return None

    def visitPlotStatement(self, ctx: gramaticaParser.PlotStatementContext):
        args = [self.visit(expr) for expr in ctx.expression()]
        print(f"Plotting: {args}")
        plt.plot(args)
        plt.show()
        return None

    def visitFileOperation(self, ctx: gramaticaParser.FileOperationContext):
        operation = ctx.children[0].getText()
        filename = ctx.STRING().getText().strip('"')
        if operation == 'read':
            try:
                with open(filename, 'r') as file:
                    data = file.read()
                    print(f"Contenido de {filename}:")
                    print(data)
            except FileNotFoundError:
                print(f"Error: El archivo {filename} no existe.")
        elif operation == 'write':
            try:
                with open(filename, 'w') as file:
                    file.write(str(self.memory))
                    print(f"Datos escritos en {filename}")
            except Exception as e:
                print(f"Error al escribir en el archivo: {e}")
        return None

    def visitPrintStatement(self, ctx: gramaticaParser.PrintStatementContext):
        print("Visiting PrintStatement")
        if ctx.arguments():
            args = [self.visit(arg) for arg in ctx.arguments().expression()]
            print("Output:", *args)
        else:
            print()
        return None

    # Métodos placeholder para regresión, clasificación y agrupamiento
    def visitRegression(self, ctx: gramaticaParser.RegressionContext):
        print("Ejecutando regresión lineal...")
        # Implementa la lógica de regresión lineal aquí
        return None

    def visitClassification(self, ctx: gramaticaParser.ClassificationContext):
        print("Ejecutando clasificación con perceptrón...")
        # Implementa la lógica del perceptrón multicapa aquí
        return None

    def visitClustering(self, ctx: gramaticaParser.ClusteringContext):
        print("Ejecutando agrupamiento...")
        # Implementa la lógica de agrupamiento aquí
        return None
