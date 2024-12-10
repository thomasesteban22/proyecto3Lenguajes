// test_conditionals.dsl

var x = 10;
if (x > 5) {
    print("x es mayor que 5");
} else {
    print("x es menor o igual a 5");
}

var contador = 0;
while (contador < 3) {
    print(contador);
    contador = contador + 1;
}

for (i = 0; i < 3; i = i + 1) {
    print(i);
}
