// Generated from gramatica.g4 by ANTLR 4.13.1

import sys

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramaticaParser}.
 */
public interface gramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(gramaticaParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(gramaticaParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(gramaticaParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(gramaticaParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(gramaticaParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(gramaticaParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#functionDef}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDef(gramaticaParser.FunctionDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#functionDef}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDef(gramaticaParser.FunctionDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(gramaticaParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(gramaticaParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(gramaticaParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(gramaticaParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(gramaticaParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(gramaticaParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#plotStatement}.
	 * @param ctx the parse tree
	 */
	void enterPlotStatement(gramaticaParser.PlotStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#plotStatement}.
	 * @param ctx the parse tree
	 */
	void exitPlotStatement(gramaticaParser.PlotStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#fileOperation}.
	 * @param ctx the parse tree
	 */
	void enterFileOperation(gramaticaParser.FileOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#fileOperation}.
	 * @param ctx the parse tree
	 */
	void exitFileOperation(gramaticaParser.FileOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#regression}.
	 * @param ctx the parse tree
	 */
	void enterRegression(gramaticaParser.RegressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#regression}.
	 * @param ctx the parse tree
	 */
	void exitRegression(gramaticaParser.RegressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#classification}.
	 * @param ctx the parse tree
	 */
	void enterClassification(gramaticaParser.ClassificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#classification}.
	 * @param ctx the parse tree
	 */
	void exitClassification(gramaticaParser.ClassificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#clustering}.
	 * @param ctx the parse tree
	 */
	void enterClustering(gramaticaParser.ClusteringContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#clustering}.
	 * @param ctx the parse tree
	 */
	void exitClustering(gramaticaParser.ClusteringContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(gramaticaParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(gramaticaParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(gramaticaParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(gramaticaParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#matrixOperation}.
	 * @param ctx the parse tree
	 */
	void enterMatrixOperation(gramaticaParser.MatrixOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#matrixOperation}.
	 * @param ctx the parse tree
	 */
	void exitMatrixOperation(gramaticaParser.MatrixOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#matrixRows}.
	 * @param ctx the parse tree
	 */
	void enterMatrixRows(gramaticaParser.MatrixRowsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#matrixRows}.
	 * @param ctx the parse tree
	 */
	void exitMatrixRows(gramaticaParser.MatrixRowsContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#matrixRow}.
	 * @param ctx the parse tree
	 */
	void enterMatrixRow(gramaticaParser.MatrixRowContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#matrixRow}.
	 * @param ctx the parse tree
	 */
	void exitMatrixRow(gramaticaParser.MatrixRowContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(gramaticaParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(gramaticaParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(gramaticaParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(gramaticaParser.ArgumentsContext ctx);
}