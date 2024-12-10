grammar MLDSL;

program: statement* EOF;

statement
    : variableDeclaration
    | assignment
    | mlOperation
    | printStatement
    | conditional
    | loop
    | functionDeclaration
    | fileOperation
    | plotStatement
    | matrixDeclaration
    | matrixInverse
    | matrixTranspose
    ;

variableDeclaration
    : 'var' ID '=' expression ';'
    ;

assignment
    : ID '=' expression ';'
    ;

mlOperation
    : 'linearRegression' '(' ID ',' ID ',' ID ')' ';'
    | 'perceptron' '(' ID ',' ID ',' ID (',' NUMBER (',' NUMBER)?)? ')' ';'
    | 'clustering' '(' ID ',' ID (',' NUMBER)? ')' ';'
    ;

printStatement
    : 'print' '(' (expression | STRING) ')' ';'
    ;

conditional
    : 'if' '(' condition ')' '{' ifStats+=statement* '}' ('else' '{' elseStats+=statement* '}')?
    ;

condition
    : expression comparisonOperator expression
    ;

comparisonOperator
    : '>'
    | '<'
    | '=='
    | '!='
    | '>='
    | '<='
    ;

loop
    : 'for' '(' assignment condition ';' assignment ')' '{' statement* '}'
    | 'while' '(' condition ')' '{' statement* '}'
    ;

functionDeclaration
    : 'def' ID '(' parameterList? ')' '{' statement* 'return' expression ';' '}'
    ;

parameterList
    : ID (',' ID)*
    ;

argumentList
    : expression (',' expression)*
    ;

expression
    : expression '^' expression       #PowerExpr
    | expression '*' expression       #MulExpr
    | expression '/' expression       #DivExpr
    | expression '+' expression       #AddExpr
    | expression '-' expression       #SubExpr
    | '-' expression                  #NegateExpr
    | '(' expression ')'              #ParenExpr
    | NUMBER                          #NumberExpr
    | ID                              #VariableExpr
    | functionCall                    #FuncCallExpr
    | trigFunction                    #TrigExpr
    | 'sqrt' '(' expression ')'       #SqrtExpr
    | listExpression                  #ListExpr
    ;

functionCall
    : ID '(' argumentList? ')'
    ;

trigFunction
    : ('sin' | 'cos' | 'tan') '(' expression ')'
    ;

listExpression
    : '[' expression (',' expression)* ']'
    ;

plotStatement
    : 'plot' '(' ID ',' ID ')' ';'
    ;

fileOperation
    : 'read' '(' STRING ',' ID ')' ';'
    | 'write' '(' STRING ',' ID ')' ';'
    ;

matrixDeclaration
    : 'var' ID '=' 'matrix' matrixExpr ';'
    ;

matrixExpr
    : '[' matrixRows ']'
    ;

matrixRows
    : matrixRow (',' matrixRow)*
    ;

matrixRow
    : '[' expression (',' expression)* ']'
    ;

matrixInverse
    : ID '=' 'inverse' '(' ID ')' ';'
    ;

matrixTranspose
    : ID '=' 'transpose' '(' ID ')' ';'
    ;

STRING
    : '"' (~["\r\n])* '"'
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;
