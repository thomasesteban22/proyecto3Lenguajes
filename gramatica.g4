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

expression
    : expression op=('*' | '/' | '%') expression
    | expression op=('+' | '-') expression
    | '(' expression ')'
    | functionCall
    | matrixOperation
    | NUMBER
    | ID
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