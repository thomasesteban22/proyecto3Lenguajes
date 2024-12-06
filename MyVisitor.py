from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor
import matplotlib.pyplot as plt
import numpy as np

class MyVisitor(gramaticaVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssignment(self, ctx: gramaticaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.memory[var_name] = value
        return value

    def visitExpression(self, ctx: gramaticaParser.ExpressionContext):
        if ctx.op:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = ctx.op.text
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
        elif ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            return self.memory.get(var_name, 0)
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        else:
            return self.visit(ctx.expression(0))

    def visitFunctionCall(self, ctx: gramaticaParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.arguments():
            args = [self.visit(arg) for arg in ctx.arguments().expression()]
        if func_name == 'sin':
            return np.sin(args[0])
        elif func_name == 'cos':
            return np.cos(args[0])
        elif func_name == 'sqrt':
            return np.sqrt(args[0])
        # Agrega más funciones según sea necesario
        return 0

    def visitPlotStatement(self, ctx: gramaticaParser.PlotStatementContext):
        args = [self.visit(expr) for expr in ctx.expression()]
        plt.plot(args)
        plt.show()
        return None

    def visitFileOperation(self, ctx: gramaticaParser.FileOperationContext):
        operation = ctx.children[0].getText()
        filename = ctx.STRING().getText().strip('"')
        if operation == 'read':
            with open(filename, 'r') as file:
                data = file.read()
                print(f"Contenido de {filename}:")
                print(data)
        elif operation == 'write':
            with open(filename, 'w') as file:
                file.write(str(self.memory))
                print(f"Datos escritos en {filename}")
        return None

    # Implementa otros métodos para manejar condicionales, bucles, etc.

    # Placeholder methods for regression, classification, and clustering
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