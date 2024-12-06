# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment.
    def enterAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment.
    def exitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printStatement.
    def enterPrintStatement(self, ctx:gramaticaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printStatement.
    def exitPrintStatement(self, ctx:gramaticaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Multiplicative.
    def enterMultiplicative(self, ctx:gramaticaParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Multiplicative.
    def exitMultiplicative(self, ctx:gramaticaParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Additive.
    def enterAdditive(self, ctx:gramaticaParser.AdditiveContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Additive.
    def exitAdditive(self, ctx:gramaticaParser.AdditiveContext):
        pass


    # Enter a parse tree produced by gramaticaParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:gramaticaParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:gramaticaParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Subtractive.
    def enterSubtractive(self, ctx:gramaticaParser.SubtractiveContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Subtractive.
    def exitSubtractive(self, ctx:gramaticaParser.SubtractiveContext):
        pass


    # Enter a parse tree produced by gramaticaParser#IdExpr.
    def enterIdExpr(self, ctx:gramaticaParser.IdExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#IdExpr.
    def exitIdExpr(self, ctx:gramaticaParser.IdExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#NumberExpr.
    def enterNumberExpr(self, ctx:gramaticaParser.NumberExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#NumberExpr.
    def exitNumberExpr(self, ctx:gramaticaParser.NumberExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Modulo.
    def enterModulo(self, ctx:gramaticaParser.ModuloContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Modulo.
    def exitModulo(self, ctx:gramaticaParser.ModuloContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Exponentiation.
    def enterExponentiation(self, ctx:gramaticaParser.ExponentiationContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Exponentiation.
    def exitExponentiation(self, ctx:gramaticaParser.ExponentiationContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Divisional.
    def enterDivisional(self, ctx:gramaticaParser.DivisionalContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Divisional.
    def exitDivisional(self, ctx:gramaticaParser.DivisionalContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Parentheses.
    def enterParentheses(self, ctx:gramaticaParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Parentheses.
    def exitParentheses(self, ctx:gramaticaParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#functionCall.
    def enterFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by gramaticaParser#functionCall.
    def exitFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arguments.
    def enterArguments(self, ctx:gramaticaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arguments.
    def exitArguments(self, ctx:gramaticaParser.ArgumentsContext):
        pass



del gramaticaParser