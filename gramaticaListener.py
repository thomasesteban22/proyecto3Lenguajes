# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

import sys


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


    # Enter a parse tree produced by gramaticaParser#functionDef.
    def enterFunctionDef(self, ctx:gramaticaParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by gramaticaParser#functionDef.
    def exitFunctionDef(self, ctx:gramaticaParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ifStatement.
    def enterIfStatement(self, ctx:gramaticaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ifStatement.
    def exitIfStatement(self, ctx:gramaticaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#whileStatement.
    def enterWhileStatement(self, ctx:gramaticaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#whileStatement.
    def exitWhileStatement(self, ctx:gramaticaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#forStatement.
    def enterForStatement(self, ctx:gramaticaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#forStatement.
    def exitForStatement(self, ctx:gramaticaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#plotStatement.
    def enterPlotStatement(self, ctx:gramaticaParser.PlotStatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#plotStatement.
    def exitPlotStatement(self, ctx:gramaticaParser.PlotStatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#fileOperation.
    def enterFileOperation(self, ctx:gramaticaParser.FileOperationContext):
        pass

    # Exit a parse tree produced by gramaticaParser#fileOperation.
    def exitFileOperation(self, ctx:gramaticaParser.FileOperationContext):
        pass


    # Enter a parse tree produced by gramaticaParser#regression.
    def enterRegression(self, ctx:gramaticaParser.RegressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#regression.
    def exitRegression(self, ctx:gramaticaParser.RegressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#classification.
    def enterClassification(self, ctx:gramaticaParser.ClassificationContext):
        pass

    # Exit a parse tree produced by gramaticaParser#classification.
    def exitClassification(self, ctx:gramaticaParser.ClassificationContext):
        pass


    # Enter a parse tree produced by gramaticaParser#clustering.
    def enterClustering(self, ctx:gramaticaParser.ClusteringContext):
        pass

    # Exit a parse tree produced by gramaticaParser#clustering.
    def exitClustering(self, ctx:gramaticaParser.ClusteringContext):
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


    # Enter a parse tree produced by gramaticaParser#MatrixOperationExpr.
    def enterMatrixOperationExpr(self, ctx:gramaticaParser.MatrixOperationExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#MatrixOperationExpr.
    def exitMatrixOperationExpr(self, ctx:gramaticaParser.MatrixOperationExprContext):
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


    # Enter a parse tree produced by gramaticaParser#matrixOperation.
    def enterMatrixOperation(self, ctx:gramaticaParser.MatrixOperationContext):
        pass

    # Exit a parse tree produced by gramaticaParser#matrixOperation.
    def exitMatrixOperation(self, ctx:gramaticaParser.MatrixOperationContext):
        pass


    # Enter a parse tree produced by gramaticaParser#matrixRows.
    def enterMatrixRows(self, ctx:gramaticaParser.MatrixRowsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#matrixRows.
    def exitMatrixRows(self, ctx:gramaticaParser.MatrixRowsContext):
        pass


    # Enter a parse tree produced by gramaticaParser#matrixRow.
    def enterMatrixRow(self, ctx:gramaticaParser.MatrixRowContext):
        pass

    # Exit a parse tree produced by gramaticaParser#matrixRow.
    def exitMatrixRow(self, ctx:gramaticaParser.MatrixRowContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parameters.
    def enterParameters(self, ctx:gramaticaParser.ParametersContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parameters.
    def exitParameters(self, ctx:gramaticaParser.ParametersContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arguments.
    def enterArguments(self, ctx:gramaticaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arguments.
    def exitArguments(self, ctx:gramaticaParser.ArgumentsContext):
        pass



del gramaticaParser