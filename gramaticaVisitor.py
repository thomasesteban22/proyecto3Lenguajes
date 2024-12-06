# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#statement.
    def visitStatement(self, ctx:gramaticaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment.
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStatement.
    def visitPrintStatement(self, ctx:gramaticaParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Multiplicative.
    def visitMultiplicative(self, ctx:gramaticaParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Additive.
    def visitAdditive(self, ctx:gramaticaParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:gramaticaParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Subtractive.
    def visitSubtractive(self, ctx:gramaticaParser.SubtractiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#IdExpr.
    def visitIdExpr(self, ctx:gramaticaParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#NumberExpr.
    def visitNumberExpr(self, ctx:gramaticaParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Modulo.
    def visitModulo(self, ctx:gramaticaParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Exponentiation.
    def visitExponentiation(self, ctx:gramaticaParser.ExponentiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Divisional.
    def visitDivisional(self, ctx:gramaticaParser.DivisionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Parentheses.
    def visitParentheses(self, ctx:gramaticaParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#functionCall.
    def visitFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arguments.
    def visitArguments(self, ctx:gramaticaParser.ArgumentsContext):
        return self.visitChildren(ctx)



del gramaticaParser