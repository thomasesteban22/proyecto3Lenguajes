# Generated from gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,36,8,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,69,8,4,10,4,12,4,72,
        9,4,1,5,1,5,1,5,3,5,77,8,5,1,5,1,5,1,6,1,6,1,6,5,6,84,8,6,10,6,12,
        6,87,9,6,1,6,0,1,8,7,0,2,4,6,8,10,12,0,0,96,0,17,1,0,0,0,2,25,1,
        0,0,0,4,27,1,0,0,0,6,32,1,0,0,0,8,48,1,0,0,0,10,73,1,0,0,0,12,80,
        1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,
        17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,
        0,0,22,26,3,4,2,0,23,26,3,6,3,0,24,26,5,1,0,0,25,22,1,0,0,0,25,23,
        1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,5,13,0,0,28,29,5,2,0,0,
        29,30,3,8,4,0,30,31,5,1,0,0,31,5,1,0,0,0,32,33,5,3,0,0,33,35,5,4,
        0,0,34,36,3,12,6,0,35,34,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,
        38,5,5,0,0,38,39,5,1,0,0,39,7,1,0,0,0,40,41,6,4,-1,0,41,42,5,4,0,
        0,42,43,3,8,4,0,43,44,5,5,0,0,44,49,1,0,0,0,45,49,3,10,5,0,46,49,
        5,13,0,0,47,49,5,14,0,0,48,40,1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,
        0,48,47,1,0,0,0,49,70,1,0,0,0,50,51,10,10,0,0,51,52,5,6,0,0,52,69,
        3,8,4,11,53,54,10,9,0,0,54,55,5,7,0,0,55,69,3,8,4,10,56,57,10,8,
        0,0,57,58,5,8,0,0,58,69,3,8,4,9,59,60,10,7,0,0,60,61,5,9,0,0,61,
        69,3,8,4,8,62,63,10,6,0,0,63,64,5,10,0,0,64,69,3,8,4,7,65,66,10,
        5,0,0,66,67,5,11,0,0,67,69,3,8,4,6,68,50,1,0,0,0,68,53,1,0,0,0,68,
        56,1,0,0,0,68,59,1,0,0,0,68,62,1,0,0,0,68,65,1,0,0,0,69,72,1,0,0,
        0,70,68,1,0,0,0,70,71,1,0,0,0,71,9,1,0,0,0,72,70,1,0,0,0,73,74,5,
        13,0,0,74,76,5,4,0,0,75,77,3,12,6,0,76,75,1,0,0,0,76,77,1,0,0,0,
        77,78,1,0,0,0,78,79,5,5,0,0,79,11,1,0,0,0,80,85,3,8,4,0,81,82,5,
        12,0,0,82,84,3,8,4,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,
        86,1,0,0,0,86,13,1,0,0,0,87,85,1,0,0,0,8,17,25,35,48,68,70,76,85
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'print'", "'('", "')'", 
                     "'^'", "'*'", "'/'", "'%'", "'+'", "'-'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_printStatement = 3
    RULE_expression = 4
    RULE_functionCall = 5
    RULE_arguments = 6

    ruleNames =  [ "program", "statement", "assignment", "printStatement", 
                   "expression", "functionCall", "arguments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ID=13
    NUMBER=14
    WS=15
    COMMENT=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8202) != 0):
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(gramaticaParser.AssignmentContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(gramaticaParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.printStatement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(gramaticaParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramaticaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(gramaticaParser.ID)
            self.state = 28
            self.match(gramaticaParser.T__1)
            self.state = 29
            self.expression(0)
            self.state = 30
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguments(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = gramaticaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(gramaticaParser.T__2)
            self.state = 33
            self.match(gramaticaParser.T__3)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 24592) != 0):
                self.state = 34
                self.arguments()


            self.state = 37
            self.match(gramaticaParser.T__4)
            self.state = 38
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicativeContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(gramaticaParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubtractiveContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtractive" ):
                listener.enterSubtractive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtractive" ):
                listener.exitSubtractive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtractive" ):
                return visitor.visitSubtractive(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModuloContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo" ):
                listener.enterModulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo" ):
                listener.exitModulo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
            else:
                return visitor.visitChildren(self)


    class ExponentiationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentiation" ):
                listener.enterExponentiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentiation" ):
                listener.exitExponentiation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponentiation" ):
                return visitor.visitExponentiation(self)
            else:
                return visitor.visitChildren(self)


    class DivisionalContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivisional" ):
                listener.enterDivisional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivisional" ):
                listener.exitDivisional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivisional" ):
                return visitor.visitDivisional(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(gramaticaParser.T__3)
                self.state = 42
                self.expression(0)
                self.state = 43
                self.match(gramaticaParser.T__4)
                pass

            elif la_ == 2:
                localctx = gramaticaParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.functionCall()
                pass

            elif la_ == 3:
                localctx = gramaticaParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(gramaticaParser.NUMBER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExponentiationContext(self, gramaticaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 51
                        self.match(gramaticaParser.T__5)
                        self.state = 52
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.MultiplicativeContext(self, gramaticaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 54
                        self.match(gramaticaParser.T__6)
                        self.state = 55
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.DivisionalContext(self, gramaticaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 57
                        self.match(gramaticaParser.T__7)
                        self.state = 58
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = gramaticaParser.ModuloContext(self, gramaticaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 60
                        self.match(gramaticaParser.T__8)
                        self.state = 61
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = gramaticaParser.AdditiveContext(self, gramaticaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 62
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 63
                        self.match(gramaticaParser.T__9)
                        self.state = 64
                        self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = gramaticaParser.SubtractiveContext(self, gramaticaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        self.match(gramaticaParser.T__10)
                        self.state = 67
                        self.expression(6)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def arguments(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = gramaticaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(gramaticaParser.ID)
            self.state = 74
            self.match(gramaticaParser.T__3)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 24592) != 0):
                self.state = 75
                self.arguments()


            self.state = 78
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = gramaticaParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.expression(0)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 81
                self.match(gramaticaParser.T__11)
                self.state = 82
                self.expression(0)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




