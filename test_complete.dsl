// 1. Operaciones AritmÃ©ticas BÃ¡sicas
var a = 15;
var b = 3;
var c = a + b;
var d = a - b;
var e = a * b; 
var f = a / b;
var g = a % b;
var h = a ^ b;
print(c);
print(d);
print(e);
print(f);
print(g);
print(h);

// 2. Operaciones TrigonomÃ©tricas y RaÃ­z Cuadrada
var angulo = 30;
var radianes = angulo * (3.1416 / 180);
var seno = sin(radianes);
var coseno = cos(radianes);
var tangente = tan(radianes);
var raiz = sqrt(a);
print(seno);
print(coseno);
print(tangente);
print(raiz);

// 3. Operaciones con Listas y Matrices
var lista = [1, 2, 3, 4, 5];
print(lista);

var matrizA = matrix[[1, 2, 3], [4, 5, 6], [7, 8, 9]];
var matrizB = matrix[[9, 8, 7], [6, 5, 4], [3, 2, 1]];
print(matrizA);
print(matrizB);

// Suma de Matrices
var sumaMatrices = matrizA + matrizB;
print(sumaMatrices);

// Resta de Matrices
var restaMatrices = matrizA - matrizB;
print(restaMatrices);

// MultiplicaciÃ³n de Matrices
var multiplicacionMatrices = matrizA * matrizB;
print(multiplicacionMatrices);

// Transpuesta de una Matriz
var transpuestaA = transpose(matrizA);
print(transpuestaA);

// Inversa de una Matriz (Invertible)
var matrizC = matrix[[4, 7], [2, 6]];
var inversaC = inverse(matrizC);
print(inversaC);

// 4. Condicionales y Ciclos
// Condicional If-Else
var x = 10;
if (x > 5) {
    print("x es mayor que 5");
} else {
    print("x es menor o igual a 5");
}

// Ciclo While
var contador = 0;
while (contador < 3) {
    print(contador);
    contador = contador + 1;
}

// Ciclo For
for (i = 0; i < 3; i = i + 1) {
    print(i);
}

// 5. GrÃ¡ficas de Datos
// Datos para Graficar
var x_plot = [1, 2, 3, 4, 5];
var y_plot = [2, 4, 6, 8, 10];
plot(x_plot, y_plot);

// 6. Manejo de Archivos
// Escribir en un Archivo
var texto = "Esta es una prueba de escritura en archivo.";
write("output_test.txt", texto);

// Leer desde un Archivo
var contenido = read("output_test.txt");
print(contenido);

// 7. DefiniciÃ³n y Uso de Funciones
// Definir una FunciÃ³n para Sumar Dos NÃºmeros
def sumar(a, b) {
    var resultado = a + b;
    print(resultado);
}

// Llamar a la FunciÃ³n Definida
sumar(7, 8);

// 8. RegresiÃ³n Lineal
// Datos para RegresiÃ³n
var X_reg = [[1], [2], [3], [4], [5]];
var y_reg = [2, 4, 6, 8, 10];

// Realizar RegresiÃ³n Lineal
linearRegression(X_reg, y_reg, modeloRegresion);

// Mostrar Coeficientes del Modelo
print(modeloRegresion);

// 9. Clasificador con PerceptrÃ³n Multicapa
// Datos para ClasificaciÃ³n (OperaciÃ³n XOR)
var entradas = [[0,0], [0,1], [1,0], [1,1]];
var salidas = [[0], [1], [1], [0]];

// Entrenar PerceptrÃ³n Multicapa
perceptron(entradas, salidas, modeloPerceptron, 1000);

// Realizar Predicciones
var prediccion = modeloPerceptron.predict([[1, 0]]);
print(prediccion);

// 10. Agrupamiento
// Datos para Agrupamiento
var datos = [[1,2], [1,3], [10,10], [10,11]];

// Realizar Agrupamiento con k=2
clustering(datos, 2, grupos);

// Mostrar Grupos Asignados
print(grupos);
