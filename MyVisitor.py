# MyVisitor.py

from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor
import numpy as np


class MyVisitor(gramaticaVisitor):
    def __init__(self, output_file):
        self.memory = {}
        self.output = output_file

    def visitAssignment(self, ctx: gramaticaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.memory[var_name] = value
        return value

    def visitPrintStatement(self, ctx: gramaticaParser.PrintStatementContext):
        if ctx.arguments():
            args = [self.visit(arg) for arg in ctx.arguments().expression()]
            args_str = ' '.join(map(str, args))
            self.output.write(f"{args_str}\n")
        return None

    def visitExponentiation(self, ctx: gramaticaParser.ExponentiationContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        result = left ** right
        return result

    def visitMultiplicative(self, ctx: gramaticaParser.MultiplicativeContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        elif op == '/':
            if right != 0:
                return left / right
            else:
                self.output.write("Error: División por cero\n")
                return 0
        elif op == '%':
            return left % right

    def visitDivisional(self, ctx: gramaticaParser.DivisionalContext):
        return self.visitMultiplicative(ctx)

    def visitModulo(self, ctx: gramaticaParser.ModuloContext):
        return self.visitMultiplicative(ctx)

    def visitAdditive(self, ctx: gramaticaParser.AdditiveContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        elif op == '-':
            return left - right

    def visitSubtractive(self, ctx: gramaticaParser.SubtractiveContext):
        return self.visitAdditive(ctx)

    def visitParentheses(self, ctx: gramaticaParser.ParenthesesContext):
        return self.visit(ctx.expression())

    def visitFunctionCallExpr(self, ctx: gramaticaParser.FunctionCallExprContext):
        return self.visitFunctionCall(ctx.functionCall())

    def visitFunctionCall(self, ctx: gramaticaParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.arguments():
            args = [self.visit(arg) for arg in ctx.arguments().expression()]

        if func_name == 'sin':
            return np.sin(args[0])
        elif func_name == 'cos':
            return np.cos(args[0])
        elif func_name == 'tan':
            return np.tan(args[0])
        elif func_name == 'sqrt':
            return np.sqrt(args[0])
        else:
            # Si la función no es reconocida, simplemente retorna None
            return None

    def visitNumberExpr(self, ctx: gramaticaParser.NumberExprContext):
        return float(ctx.NUMBER().getText())

    def visitIdExpr(self, ctx: gramaticaParser.IdExprContext):
        var_name = ctx.ID().getText()
        return self.memory.get(var_name, 0)
