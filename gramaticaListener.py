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


    # Enter a parse tree produced by gramaticaParser#expression.
    def enterExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expression.
    def exitExpression(self, ctx:gramaticaParser.ExpressionContext):
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