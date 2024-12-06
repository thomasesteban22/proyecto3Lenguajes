# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

import sys


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


    # Visit a parse tree produced by gramaticaParser#functionDef.
    def visitFunctionDef(self, ctx:gramaticaParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ifStatement.
    def visitIfStatement(self, ctx:gramaticaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#whileStatement.
    def visitWhileStatement(self, ctx:gramaticaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#forStatement.
    def visitForStatement(self, ctx:gramaticaParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#plotStatement.
    def visitPlotStatement(self, ctx:gramaticaParser.PlotStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fileOperation.
    def visitFileOperation(self, ctx:gramaticaParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#regression.
    def visitRegression(self, ctx:gramaticaParser.RegressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#classification.
    def visitClassification(self, ctx:gramaticaParser.ClassificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#clustering.
    def visitClustering(self, ctx:gramaticaParser.ClusteringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expression.
    def visitExpression(self, ctx:gramaticaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#functionCall.
    def visitFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#matrixOperation.
    def visitMatrixOperation(self, ctx:gramaticaParser.MatrixOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#matrixRows.
    def visitMatrixRows(self, ctx:gramaticaParser.MatrixRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#matrixRow.
    def visitMatrixRow(self, ctx:gramaticaParser.MatrixRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#parameters.
    def visitParameters(self, ctx:gramaticaParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arguments.
    def visitArguments(self, ctx:gramaticaParser.ArgumentsContext):
        return self.visitChildren(ctx)



del gramaticaParser