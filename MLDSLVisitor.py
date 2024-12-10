# Generated from MLDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MLDSLParser import MLDSLParser
else:
    from MLDSLParser import MLDSLParser

# This class defines a complete generic visitor for a parse tree produced by MLDSLParser.

class MLDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MLDSLParser#program.
    def visitProgram(self, ctx:MLDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#statement.
    def visitStatement(self, ctx:MLDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MLDSLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#assignment.
    def visitAssignment(self, ctx:MLDSLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#mlOperation.
    def visitMlOperation(self, ctx:MLDSLParser.MlOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#printStatement.
    def visitPrintStatement(self, ctx:MLDSLParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#conditional.
    def visitConditional(self, ctx:MLDSLParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#condition.
    def visitCondition(self, ctx:MLDSLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:MLDSLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#loop.
    def visitLoop(self, ctx:MLDSLParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MLDSLParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#parameterList.
    def visitParameterList(self, ctx:MLDSLParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#argumentList.
    def visitArgumentList(self, ctx:MLDSLParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#MulExpr.
    def visitMulExpr(self, ctx:MLDSLParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#SubExpr.
    def visitSubExpr(self, ctx:MLDSLParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#AddExpr.
    def visitAddExpr(self, ctx:MLDSLParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#NegateExpr.
    def visitNegateExpr(self, ctx:MLDSLParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#PowerExpr.
    def visitPowerExpr(self, ctx:MLDSLParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#DivExpr.
    def visitDivExpr(self, ctx:MLDSLParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#TrigExpr.
    def visitTrigExpr(self, ctx:MLDSLParser.TrigExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#NumberExpr.
    def visitNumberExpr(self, ctx:MLDSLParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#SqrtExpr.
    def visitSqrtExpr(self, ctx:MLDSLParser.SqrtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#VariableExpr.
    def visitVariableExpr(self, ctx:MLDSLParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#ListExpr.
    def visitListExpr(self, ctx:MLDSLParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#ParenExpr.
    def visitParenExpr(self, ctx:MLDSLParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:MLDSLParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#functionCall.
    def visitFunctionCall(self, ctx:MLDSLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#trigFunction.
    def visitTrigFunction(self, ctx:MLDSLParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#listExpression.
    def visitListExpression(self, ctx:MLDSLParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#plotStatement.
    def visitPlotStatement(self, ctx:MLDSLParser.PlotStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#fileOperation.
    def visitFileOperation(self, ctx:MLDSLParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#matrixDeclaration.
    def visitMatrixDeclaration(self, ctx:MLDSLParser.MatrixDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#matrixExpr.
    def visitMatrixExpr(self, ctx:MLDSLParser.MatrixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#matrixRows.
    def visitMatrixRows(self, ctx:MLDSLParser.MatrixRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#matrixRow.
    def visitMatrixRow(self, ctx:MLDSLParser.MatrixRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#matrixInverse.
    def visitMatrixInverse(self, ctx:MLDSLParser.MatrixInverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLDSLParser#matrixTranspose.
    def visitMatrixTranspose(self, ctx:MLDSLParser.MatrixTransposeContext):
        return self.visitChildren(ctx)



del MLDSLParser