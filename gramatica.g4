grammar gramatica;

// Regla de inicio
program
    : statement* EOF
    ;

// Declaraciones
statement
    : assignment
    | printStatement
    | ';' // Ignorar declaraciones vacías
    ;

// Asignación de variables
assignment
    : ID '=' expression ';'
    ;

// Declaración print
printStatement
    : 'print' '(' arguments? ')' ';'
    ;

// Expresiones aritméticas con precedencia adecuada
expression
    : expression '^' expression    # Exponentiation
    | expression '*' expression    # Multiplicative
    | expression '/' expression    # Divisional
    | expression '%' expression    # Modulo
    | expression '+' expression    # Additive
    | expression '-' expression    # Subtractive
    | '(' expression ')'           # Parentheses
    | functionCall                 # FunctionCallExpr
    | ID                           # IdExpr
    | NUMBER                       # NumberExpr
    ;

// Llamadas a funciones
functionCall
    : ID '(' arguments? ')'
    ;

// Argumentos para funciones y print
arguments
    : expression (',' expression)*
    ;

// Tokens
ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;
