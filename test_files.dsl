// test_files.dsl CORREGIDO

var texto = "Hola, esto es una prueba de escritura.";
write("archivo_salida.txt", texto);

var contenido = "vacio";
read("archivo_salida.txt", contenido);
print(contenido);
