# Generated from gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys

def serializedATN():
    return [
        4,1,31,245,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,58,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,69,8,3,1,
        3,1,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,5,4,87,8,4,10,4,12,4,90,9,4,1,4,1,4,1,4,1,4,5,4,96,8,4,10,
        4,12,4,99,9,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,110,8,
        5,10,5,12,5,113,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,126,8,6,10,6,12,6,129,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,138,
        8,7,10,7,12,7,141,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,3,9,155,8,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,163,8,10,1,10,
        1,10,1,10,1,11,1,11,1,11,3,11,171,8,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,185,8,12,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,193,8,12,10,12,12,12,196,9,12,1,13,1,13,1,13,
        3,13,201,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        5,15,213,8,15,10,15,12,15,216,9,15,1,16,1,16,1,16,1,16,5,16,222,
        8,16,10,16,12,16,225,9,16,1,16,1,16,1,17,1,17,1,17,5,17,232,8,17,
        10,17,12,17,235,9,17,1,18,1,18,1,18,5,18,240,8,18,10,18,12,18,243,
        9,18,1,18,0,1,24,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,0,3,1,0,14,15,1,0,19,21,1,0,22,23,258,0,41,1,0,0,0,2,57,1,
        0,0,0,4,59,1,0,0,0,6,64,1,0,0,0,8,80,1,0,0,0,10,103,1,0,0,0,12,116,
        1,0,0,0,14,132,1,0,0,0,16,145,1,0,0,0,18,151,1,0,0,0,20,159,1,0,
        0,0,22,167,1,0,0,0,24,184,1,0,0,0,26,197,1,0,0,0,28,204,1,0,0,0,
        30,209,1,0,0,0,32,217,1,0,0,0,34,228,1,0,0,0,36,236,1,0,0,0,38,40,
        3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,
        42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,58,3,4,
        2,0,47,58,3,6,3,0,48,58,3,8,4,0,49,58,3,10,5,0,50,58,3,12,6,0,51,
        58,3,14,7,0,52,58,3,16,8,0,53,58,3,18,9,0,54,58,3,20,10,0,55,58,
        3,22,11,0,56,58,5,1,0,0,57,46,1,0,0,0,57,47,1,0,0,0,57,48,1,0,0,
        0,57,49,1,0,0,0,57,50,1,0,0,0,57,51,1,0,0,0,57,52,1,0,0,0,57,53,
        1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,3,1,0,0,0,59,
        60,5,27,0,0,60,61,5,2,0,0,61,62,3,24,12,0,62,63,5,1,0,0,63,5,1,0,
        0,0,64,65,5,3,0,0,65,66,5,27,0,0,66,68,5,4,0,0,67,69,3,34,17,0,68,
        67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,5,0,0,71,75,5,6,0,
        0,72,74,3,2,1,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,
        1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,7,0,0,79,7,1,0,0,0,80,
        81,5,8,0,0,81,82,5,4,0,0,82,83,3,24,12,0,83,84,5,5,0,0,84,88,5,6,
        0,0,85,87,3,2,1,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,
        1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,101,5,7,0,0,92,93,5,9,0,0,
        93,97,5,6,0,0,94,96,3,2,1,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,
        0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,102,5,7,0,0,
        101,92,1,0,0,0,101,102,1,0,0,0,102,9,1,0,0,0,103,104,5,10,0,0,104,
        105,5,4,0,0,105,106,3,24,12,0,106,107,5,5,0,0,107,111,5,6,0,0,108,
        110,3,2,1,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,
        112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,115,5,7,0,0,115,
        11,1,0,0,0,116,117,5,11,0,0,117,118,5,4,0,0,118,119,3,4,2,0,119,
        120,3,24,12,0,120,121,5,1,0,0,121,122,3,24,12,0,122,123,5,5,0,0,
        123,127,5,6,0,0,124,126,3,2,1,0,125,124,1,0,0,0,126,129,1,0,0,0,
        127,125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,
        130,131,5,7,0,0,131,13,1,0,0,0,132,133,5,12,0,0,133,134,5,4,0,0,
        134,139,3,24,12,0,135,136,5,13,0,0,136,138,3,24,12,0,137,135,1,0,
        0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,
        0,0,141,139,1,0,0,0,142,143,5,5,0,0,143,144,5,1,0,0,144,15,1,0,0,
        0,145,146,7,0,0,0,146,147,5,4,0,0,147,148,5,29,0,0,148,149,5,5,0,
        0,149,150,5,1,0,0,150,17,1,0,0,0,151,152,5,16,0,0,152,154,5,4,0,
        0,153,155,3,34,17,0,154,153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,
        0,0,156,157,5,5,0,0,157,158,5,1,0,0,158,19,1,0,0,0,159,160,5,17,
        0,0,160,162,5,4,0,0,161,163,3,34,17,0,162,161,1,0,0,0,162,163,1,
        0,0,0,163,164,1,0,0,0,164,165,5,5,0,0,165,166,5,1,0,0,166,21,1,0,
        0,0,167,168,5,18,0,0,168,170,5,4,0,0,169,171,3,34,17,0,170,169,1,
        0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,5,5,0,0,173,174,5,
        1,0,0,174,23,1,0,0,0,175,176,6,12,-1,0,176,177,5,4,0,0,177,178,3,
        24,12,0,178,179,5,5,0,0,179,185,1,0,0,0,180,185,3,26,13,0,181,185,
        3,28,14,0,182,185,5,28,0,0,183,185,5,27,0,0,184,175,1,0,0,0,184,
        180,1,0,0,0,184,181,1,0,0,0,184,182,1,0,0,0,184,183,1,0,0,0,185,
        194,1,0,0,0,186,187,10,7,0,0,187,188,7,1,0,0,188,193,3,24,12,8,189,
        190,10,6,0,0,190,191,7,2,0,0,191,193,3,24,12,7,192,186,1,0,0,0,192,
        189,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,
        25,1,0,0,0,196,194,1,0,0,0,197,198,5,27,0,0,198,200,5,4,0,0,199,
        201,3,36,18,0,200,199,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,
        203,5,5,0,0,203,27,1,0,0,0,204,205,5,24,0,0,205,206,5,25,0,0,206,
        207,3,30,15,0,207,208,5,26,0,0,208,29,1,0,0,0,209,214,3,32,16,0,
        210,211,5,13,0,0,211,213,3,32,16,0,212,210,1,0,0,0,213,216,1,0,0,
        0,214,212,1,0,0,0,214,215,1,0,0,0,215,31,1,0,0,0,216,214,1,0,0,0,
        217,218,5,25,0,0,218,223,5,28,0,0,219,220,5,13,0,0,220,222,5,28,
        0,0,221,219,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,
        0,0,224,226,1,0,0,0,225,223,1,0,0,0,226,227,5,26,0,0,227,33,1,0,
        0,0,228,233,5,27,0,0,229,230,5,13,0,0,230,232,5,27,0,0,231,229,1,
        0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,35,1,0,
        0,0,235,233,1,0,0,0,236,241,3,24,12,0,237,238,5,13,0,0,238,240,3,
        24,12,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,
        1,0,0,0,242,37,1,0,0,0,243,241,1,0,0,0,21,41,57,68,75,88,97,101,
        111,127,139,154,162,170,184,192,194,200,214,223,233,241
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'def'", "'('", "')'", "'{'", 
                     "'}'", "'if'", "'else'", "'while'", "'for'", "'plot'", 
                     "','", "'read'", "'write'", "'linearRegression'", "'perceptron'", 
                     "'clustering'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'matrix'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "STRING", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_functionDef = 3
    RULE_ifStatement = 4
    RULE_whileStatement = 5
    RULE_forStatement = 6
    RULE_plotStatement = 7
    RULE_fileOperation = 8
    RULE_regression = 9
    RULE_classification = 10
    RULE_clustering = 11
    RULE_expression = 12
    RULE_functionCall = 13
    RULE_matrixOperation = 14
    RULE_matrixRows = 15
    RULE_matrixRow = 16
    RULE_parameters = 17
    RULE_arguments = 18

    ruleNames =  [ "program", "statement", "assignment", "functionDef", 
                   "ifStatement", "whileStatement", "forStatement", "plotStatement", 
                   "fileOperation", "regression", "classification", "clustering", 
                   "expression", "functionCall", "matrixOperation", "matrixRows", 
                   "matrixRow", "parameters", "arguments" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    ID=27
    NUMBER=28
    STRING=29
    COMMENT=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        from gramaticaVisitor import gramaticaVisitor



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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134733066) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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


        def functionDef(self):
            return self.getTypedRuleContext(gramaticaParser.FunctionDefContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(gramaticaParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(gramaticaParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(gramaticaParser.ForStatementContext,0)


        def plotStatement(self):
            return self.getTypedRuleContext(gramaticaParser.PlotStatementContext,0)


        def fileOperation(self):
            return self.getTypedRuleContext(gramaticaParser.FileOperationContext,0)


        def regression(self):
            return self.getTypedRuleContext(gramaticaParser.RegressionContext,0)


        def classification(self):
            return self.getTypedRuleContext(gramaticaParser.ClassificationContext,0)


        def clustering(self):
            return self.getTypedRuleContext(gramaticaParser.ClusteringContext,0)


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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.functionDef()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.ifStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.whileStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.forStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.plotStatement()
                pass
            elif token in [14, 15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.fileOperation()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.regression()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.classification()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 10)
                self.state = 55
                self.clustering()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 11)
                self.state = 56
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
            self.state = 59
            self.match(gramaticaParser.ID)
            self.state = 60
            self.match(gramaticaParser.T__1)
            self.state = 61
            self.expression(0)
            self.state = 62
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def parameters(self):
            return self.getTypedRuleContext(gramaticaParser.ParametersContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = gramaticaParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(gramaticaParser.T__2)
            self.state = 65
            self.match(gramaticaParser.ID)
            self.state = 66
            self.match(gramaticaParser.T__3)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 67
                self.parameters()


            self.state = 70
            self.match(gramaticaParser.T__4)
            self.state = 71
            self.match(gramaticaParser.T__5)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134733066) != 0):
                self.state = 72
                self.statement()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramaticaParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(gramaticaParser.T__7)
            self.state = 81
            self.match(gramaticaParser.T__3)
            self.state = 82
            self.expression(0)
            self.state = 83
            self.match(gramaticaParser.T__4)
            self.state = 84
            self.match(gramaticaParser.T__5)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134733066) != 0):
                self.state = 85
                self.statement()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(gramaticaParser.T__6)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 92
                self.match(gramaticaParser.T__8)
                self.state = 93
                self.match(gramaticaParser.T__5)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134733066) != 0):
                    self.state = 94
                    self.statement()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.match(gramaticaParser.T__6)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = gramaticaParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(gramaticaParser.T__9)
            self.state = 104
            self.match(gramaticaParser.T__3)
            self.state = 105
            self.expression(0)
            self.state = 106
            self.match(gramaticaParser.T__4)
            self.state = 107
            self.match(gramaticaParser.T__5)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134733066) != 0):
                self.state = 108
                self.statement()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(gramaticaParser.AssignmentContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramaticaParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(gramaticaParser.T__10)
            self.state = 117
            self.match(gramaticaParser.T__3)
            self.state = 118
            self.assignment()
            self.state = 119
            self.expression(0)
            self.state = 120
            self.match(gramaticaParser.T__0)
            self.state = 121
            self.expression(0)
            self.state = 122
            self.match(gramaticaParser.T__4)
            self.state = 123
            self.match(gramaticaParser.T__5)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134733066) != 0):
                self.state = 124
                self.statement()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(gramaticaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotStatementContext(ParserRuleContext):
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
            return gramaticaParser.RULE_plotStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlotStatement" ):
                listener.enterPlotStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlotStatement" ):
                listener.exitPlotStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlotStatement" ):
                return visitor.visitPlotStatement(self)
            else:
                return visitor.visitChildren(self)




    def plotStatement(self):

        localctx = gramaticaParser.PlotStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_plotStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(gramaticaParser.T__11)
            self.state = 133
            self.match(gramaticaParser.T__3)
            self.state = 134
            self.expression(0)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 135
                self.match(gramaticaParser.T__12)
                self.state = 136
                self.expression(0)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(gramaticaParser.T__4)
            self.state = 143
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_fileOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileOperation" ):
                listener.enterFileOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileOperation" ):
                listener.exitFileOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileOperation" ):
                return visitor.visitFileOperation(self)
            else:
                return visitor.visitChildren(self)




    def fileOperation(self):

        localctx = gramaticaParser.FileOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fileOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            self.match(gramaticaParser.T__3)
            self.state = 147
            self.match(gramaticaParser.STRING)
            self.state = 148
            self.match(gramaticaParser.T__4)
            self.state = 149
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(gramaticaParser.ParametersContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_regression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegression" ):
                listener.enterRegression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegression" ):
                listener.exitRegression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegression" ):
                return visitor.visitRegression(self)
            else:
                return visitor.visitChildren(self)




    def regression(self):

        localctx = gramaticaParser.RegressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_regression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(gramaticaParser.T__15)
            self.state = 152
            self.match(gramaticaParser.T__3)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 153
                self.parameters()


            self.state = 156
            self.match(gramaticaParser.T__4)
            self.state = 157
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(gramaticaParser.ParametersContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_classification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassification" ):
                listener.enterClassification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassification" ):
                listener.exitClassification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassification" ):
                return visitor.visitClassification(self)
            else:
                return visitor.visitChildren(self)




    def classification(self):

        localctx = gramaticaParser.ClassificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_classification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(gramaticaParser.T__16)
            self.state = 160
            self.match(gramaticaParser.T__3)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 161
                self.parameters()


            self.state = 164
            self.match(gramaticaParser.T__4)
            self.state = 165
            self.match(gramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClusteringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(gramaticaParser.ParametersContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_clustering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClustering" ):
                listener.enterClustering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClustering" ):
                listener.exitClustering(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClustering" ):
                return visitor.visitClustering(self)
            else:
                return visitor.visitChildren(self)




    def clustering(self):

        localctx = gramaticaParser.ClusteringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_clustering)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(gramaticaParser.T__17)
            self.state = 168
            self.match(gramaticaParser.T__3)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 169
                self.parameters()


            self.state = 172
            self.match(gramaticaParser.T__4)
            self.state = 173
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
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def functionCall(self):
            return self.getTypedRuleContext(gramaticaParser.FunctionCallContext,0)


        def matrixOperation(self):
            return self.getTypedRuleContext(gramaticaParser.MatrixOperationContext,0)


        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(gramaticaParser.T__3)
                self.state = 177
                self.expression(0)
                self.state = 178
                self.match(gramaticaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 180
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 181
                self.matrixOperation()
                pass

            elif la_ == 4:
                self.state = 182
                self.match(gramaticaParser.NUMBER)
                pass

            elif la_ == 5:
                self.state = 183
                self.match(gramaticaParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 192
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 187
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 190
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expression(7)
                        pass

             
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(gramaticaParser.ID)
            self.state = 198
            self.match(gramaticaParser.T__3)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 419430416) != 0):
                self.state = 199
                self.arguments()


            self.state = 202
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixRows(self):
            return self.getTypedRuleContext(gramaticaParser.MatrixRowsContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_matrixOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixOperation" ):
                listener.enterMatrixOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixOperation" ):
                listener.exitMatrixOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixOperation" ):
                return visitor.visitMatrixOperation(self)
            else:
                return visitor.visitChildren(self)




    def matrixOperation(self):

        localctx = gramaticaParser.MatrixOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_matrixOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(gramaticaParser.T__23)
            self.state = 205
            self.match(gramaticaParser.T__24)
            self.state = 206
            self.matrixRows()
            self.state = 207
            self.match(gramaticaParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixRowsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixRow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.MatrixRowContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.MatrixRowContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_matrixRows

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixRows" ):
                listener.enterMatrixRows(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixRows" ):
                listener.exitMatrixRows(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixRows" ):
                return visitor.visitMatrixRows(self)
            else:
                return visitor.visitChildren(self)




    def matrixRows(self):

        localctx = gramaticaParser.MatrixRowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_matrixRows)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.matrixRow()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 210
                self.match(gramaticaParser.T__12)
                self.state = 211
                self.matrixRow()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMBER)
            else:
                return self.getToken(gramaticaParser.NUMBER, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_matrixRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixRow" ):
                listener.enterMatrixRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixRow" ):
                listener.exitMatrixRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixRow" ):
                return visitor.visitMatrixRow(self)
            else:
                return visitor.visitChildren(self)




    def matrixRow(self):

        localctx = gramaticaParser.MatrixRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_matrixRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(gramaticaParser.T__24)
            self.state = 218
            self.match(gramaticaParser.NUMBER)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 219
                self.match(gramaticaParser.T__12)
                self.state = 220
                self.match(gramaticaParser.NUMBER)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.match(gramaticaParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = gramaticaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(gramaticaParser.ID)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 229
                self.match(gramaticaParser.T__12)
                self.state = 230
                self.match(gramaticaParser.ID)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 36, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expression(0)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 237
                self.match(gramaticaParser.T__12)
                self.state = 238
                self.expression(0)
                self.state = 243
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
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         




