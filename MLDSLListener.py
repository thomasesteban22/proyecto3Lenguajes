# Generated from MLDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MLDSLParser import MLDSLParser
else:
    from MLDSLParser import MLDSLParser

# This class defines a complete listener for a parse tree produced by MLDSLParser.
class MLDSLListener(ParseTreeListener):

    # Enter a parse tree produced by MLDSLParser#program.
    def enterProgram(self, ctx:MLDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLDSLParser#program.
    def exitProgram(self, ctx:MLDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLDSLParser#statement.
    def enterStatement(self, ctx:MLDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by MLDSLParser#statement.
    def exitStatement(self, ctx:MLDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by MLDSLParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MLDSLParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MLDSLParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MLDSLParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MLDSLParser#assignment.
    def enterAssignment(self, ctx:MLDSLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MLDSLParser#assignment.
    def exitAssignment(self, ctx:MLDSLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MLDSLParser#mlOperation.
    def enterMlOperation(self, ctx:MLDSLParser.MlOperationContext):
        pass

    # Exit a parse tree produced by MLDSLParser#mlOperation.
    def exitMlOperation(self, ctx:MLDSLParser.MlOperationContext):
        pass


    # Enter a parse tree produced by MLDSLParser#printStatement.
    def enterPrintStatement(self, ctx:MLDSLParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MLDSLParser#printStatement.
    def exitPrintStatement(self, ctx:MLDSLParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MLDSLParser#conditional.
    def enterConditional(self, ctx:MLDSLParser.ConditionalContext):
        pass

    # Exit a parse tree produced by MLDSLParser#conditional.
    def exitConditional(self, ctx:MLDSLParser.ConditionalContext):
        pass


    # Enter a parse tree produced by MLDSLParser#condition.
    def enterCondition(self, ctx:MLDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by MLDSLParser#condition.
    def exitCondition(self, ctx:MLDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by MLDSLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:MLDSLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by MLDSLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:MLDSLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by MLDSLParser#loop.
    def enterLoop(self, ctx:MLDSLParser.LoopContext):
        pass

    # Exit a parse tree produced by MLDSLParser#loop.
    def exitLoop(self, ctx:MLDSLParser.LoopContext):
        pass


    # Enter a parse tree produced by MLDSLParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:MLDSLParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by MLDSLParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:MLDSLParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by MLDSLParser#parameterList.
    def enterParameterList(self, ctx:MLDSLParser.ParameterListContext):
        pass

    # Exit a parse tree produced by MLDSLParser#parameterList.
    def exitParameterList(self, ctx:MLDSLParser.ParameterListContext):
        pass


    # Enter a parse tree produced by MLDSLParser#argumentList.
    def enterArgumentList(self, ctx:MLDSLParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MLDSLParser#argumentList.
    def exitArgumentList(self, ctx:MLDSLParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MLDSLParser#MulExpr.
    def enterMulExpr(self, ctx:MLDSLParser.MulExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#MulExpr.
    def exitMulExpr(self, ctx:MLDSLParser.MulExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#SubExpr.
    def enterSubExpr(self, ctx:MLDSLParser.SubExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#SubExpr.
    def exitSubExpr(self, ctx:MLDSLParser.SubExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#AddExpr.
    def enterAddExpr(self, ctx:MLDSLParser.AddExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#AddExpr.
    def exitAddExpr(self, ctx:MLDSLParser.AddExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#NegateExpr.
    def enterNegateExpr(self, ctx:MLDSLParser.NegateExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#NegateExpr.
    def exitNegateExpr(self, ctx:MLDSLParser.NegateExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#PowerExpr.
    def enterPowerExpr(self, ctx:MLDSLParser.PowerExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#PowerExpr.
    def exitPowerExpr(self, ctx:MLDSLParser.PowerExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#DivExpr.
    def enterDivExpr(self, ctx:MLDSLParser.DivExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#DivExpr.
    def exitDivExpr(self, ctx:MLDSLParser.DivExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#TrigExpr.
    def enterTrigExpr(self, ctx:MLDSLParser.TrigExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#TrigExpr.
    def exitTrigExpr(self, ctx:MLDSLParser.TrigExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#NumberExpr.
    def enterNumberExpr(self, ctx:MLDSLParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#NumberExpr.
    def exitNumberExpr(self, ctx:MLDSLParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#SqrtExpr.
    def enterSqrtExpr(self, ctx:MLDSLParser.SqrtExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#SqrtExpr.
    def exitSqrtExpr(self, ctx:MLDSLParser.SqrtExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#VariableExpr.
    def enterVariableExpr(self, ctx:MLDSLParser.VariableExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#VariableExpr.
    def exitVariableExpr(self, ctx:MLDSLParser.VariableExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#ListExpr.
    def enterListExpr(self, ctx:MLDSLParser.ListExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#ListExpr.
    def exitListExpr(self, ctx:MLDSLParser.ListExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#ParenExpr.
    def enterParenExpr(self, ctx:MLDSLParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#ParenExpr.
    def exitParenExpr(self, ctx:MLDSLParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:MLDSLParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:MLDSLParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#functionCall.
    def enterFunctionCall(self, ctx:MLDSLParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MLDSLParser#functionCall.
    def exitFunctionCall(self, ctx:MLDSLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MLDSLParser#trigFunction.
    def enterTrigFunction(self, ctx:MLDSLParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by MLDSLParser#trigFunction.
    def exitTrigFunction(self, ctx:MLDSLParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by MLDSLParser#listExpression.
    def enterListExpression(self, ctx:MLDSLParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by MLDSLParser#listExpression.
    def exitListExpression(self, ctx:MLDSLParser.ListExpressionContext):
        pass


    # Enter a parse tree produced by MLDSLParser#plotStatement.
    def enterPlotStatement(self, ctx:MLDSLParser.PlotStatementContext):
        pass

    # Exit a parse tree produced by MLDSLParser#plotStatement.
    def exitPlotStatement(self, ctx:MLDSLParser.PlotStatementContext):
        pass


    # Enter a parse tree produced by MLDSLParser#fileOperation.
    def enterFileOperation(self, ctx:MLDSLParser.FileOperationContext):
        pass

    # Exit a parse tree produced by MLDSLParser#fileOperation.
    def exitFileOperation(self, ctx:MLDSLParser.FileOperationContext):
        pass


    # Enter a parse tree produced by MLDSLParser#matrixDeclaration.
    def enterMatrixDeclaration(self, ctx:MLDSLParser.MatrixDeclarationContext):
        pass

    # Exit a parse tree produced by MLDSLParser#matrixDeclaration.
    def exitMatrixDeclaration(self, ctx:MLDSLParser.MatrixDeclarationContext):
        pass


    # Enter a parse tree produced by MLDSLParser#matrixExpr.
    def enterMatrixExpr(self, ctx:MLDSLParser.MatrixExprContext):
        pass

    # Exit a parse tree produced by MLDSLParser#matrixExpr.
    def exitMatrixExpr(self, ctx:MLDSLParser.MatrixExprContext):
        pass


    # Enter a parse tree produced by MLDSLParser#matrixRows.
    def enterMatrixRows(self, ctx:MLDSLParser.MatrixRowsContext):
        pass

    # Exit a parse tree produced by MLDSLParser#matrixRows.
    def exitMatrixRows(self, ctx:MLDSLParser.MatrixRowsContext):
        pass


    # Enter a parse tree produced by MLDSLParser#matrixRow.
    def enterMatrixRow(self, ctx:MLDSLParser.MatrixRowContext):
        pass

    # Exit a parse tree produced by MLDSLParser#matrixRow.
    def exitMatrixRow(self, ctx:MLDSLParser.MatrixRowContext):
        pass


    # Enter a parse tree produced by MLDSLParser#matrixInverse.
    def enterMatrixInverse(self, ctx:MLDSLParser.MatrixInverseContext):
        pass

    # Exit a parse tree produced by MLDSLParser#matrixInverse.
    def exitMatrixInverse(self, ctx:MLDSLParser.MatrixInverseContext):
        pass


    # Enter a parse tree produced by MLDSLParser#matrixTranspose.
    def enterMatrixTranspose(self, ctx:MLDSLParser.MatrixTransposeContext):
        pass

    # Exit a parse tree produced by MLDSLParser#matrixTranspose.
    def exitMatrixTranspose(self, ctx:MLDSLParser.MatrixTransposeContext):
        pass



del MLDSLParser