grammar gramatica;

@header {
import sys
}

@parser::members {
    from gramaticaVisitor import gramaticaVisitor
}

program
    : statement* EOF
    ;

statement
    : assignment
    | functionDef
    | ifStatement
    | whileStatement
    | forStatement
    | plotStatement
    | fileOperation
    | regression
    | classification
    | clustering
    | printStatement
    | ';'
    ;

assignment
    : ID '=' expression ';'
    ;

functionDef
    : 'def' ID '(' parameters? ')' '{' statement* '}'
    ;

ifStatement
    : 'if' '(' expression ')' '{' statement* '}'
      ( 'else' '{' statement* '}' )?
    ;

whileStatement
    : 'while' '(' expression ')' '{' statement* '}'
    ;

forStatement
    : 'for' '(' assignment expression ';' expression ')' '{' statement* '}'
    ;

plotStatement
    : 'plot' '(' expression (',' expression)* ')' ';'
    ;

fileOperation
    : ('read' | 'write') '(' STRING ')' ';'
    ;

regression
    : 'linearRegression' '(' parameters? ')' ';'
    ;

classification
    : 'perceptron' '(' parameters? ')' ';'
    ;

clustering
    : 'clustering' '(' parameters? ')' ';'
    ;

printStatement
    : 'print' '(' arguments? ')' ';'
    ;

expression
    : expression '^' expression    # Exponentiation
    | expression '*' expression    # Multiplicative
    | expression '/' expression    # Divisional
    | expression '%' expression    # Modulo
    | expression '+' expression    # Additive
    | expression '-' expression    # Subtractive
    | '(' expression ')'           # Parentheses
    | functionCall                 # FunctionCallExpr
    | matrixOperation              # MatrixOperationExpr
    | NUMBER                       # NumberExpr
    | ID                           # IdExpr
    ;

functionCall
    : ID '(' arguments? ')'
    ;

matrixOperation
    : 'matrix' '[' matrixRows ']'
    ;

matrixRows
    : matrixRow (',' matrixRow)*
    ;

matrixRow
    : '[' NUMBER (',' NUMBER)* ']'
    ;

parameters
    : ID (',' ID)*
    ;

arguments
    : expression (',' expression)*
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

STRING
    : '"' (~["\r\n])* '"'
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
