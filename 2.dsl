// test_matrices.dsl CORREGIDO

var A = matrix[[1,2],[3,4]];
var B = matrix[[5,6],[7,8]];

var suma = matrix[[ (1+5),(2+6)],[(3+7),(4+8)]];
print(suma);

var resta = matrix[[ (1-5),(2-6)],[(3-7),(4-8)]];
print(resta);

var mult = matrix[[ (1*5+2*7),(1*6+2*8)],
                  [(3*5+4*7),(3*6+4*8)]];
print(mult);

// Ahora Ainv y Atrans sin 'var', y con la sintaxis correcta
Ainv = inverse(A);
print(Ainv);

Atrans = transpose(A);
print(Atrans);

