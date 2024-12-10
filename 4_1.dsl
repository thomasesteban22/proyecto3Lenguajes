

pi = 3.141592653589793;


// Definir el rango de valores de X de -2pi a 2pi con un paso de 0.1pi
X = [-2 * pi, -1.9 * pi, -1.8 * pi, -1.7 * pi, -1.6 * pi,
         -1.5 * pi, -1.4 * pi, -1.3 * pi, -1.2 * pi, -1.1 * pi,
         -pi, -0.9 * pi, -0.8 * pi, -0.7 * pi, -0.6 * pi,
         -0.5 * pi, -0.4 * pi, -0.3 * pi, -0.2 * pi, -0.1 * pi,
         0, 0.1 * pi, 0.2 * pi, 0.3 * pi, 0.4 * pi, 0.5 * pi,
         0.6 * pi, 0.7 * pi, 0.8 * pi, 0.9 * pi, pi,
         1.1 * pi, 1.2 * pi, 1.3 * pi, 1.4 * pi, 1.5 * pi,
         1.6 * pi, 1.7 * pi, 1.8 * pi, 1.9 * pi, 2 * pi];

// Definir Y_sin como el seno de cada valor de X
Y_sin = [sin(-2 * pi), sin(-1.9 * pi), sin(-1.8 * pi), sin(-1.7 * pi), sin(-1.6 * pi),
             sin(-1.5 * pi), sin(-1.4 * pi), sin(-1.3 * pi), sin(-1.2 * pi), sin(-1.1 * pi),
             sin(-pi), sin(-0.9 * pi), sin(-0.8 * pi), sin(-0.7 * pi), sin(-0.6 * pi),
             sin(-0.5 * pi), sin(-0.4 * pi), sin(-0.3 * pi), sin(-0.2 * pi), sin(-0.1 * pi),
             sin(0), sin(0.1 * pi), sin(0.2 * pi), sin(0.3 * pi), sin(0.4 * pi), sin(0.5 * pi),
             sin(0.6 * pi), sin(0.7 * pi), sin(0.8 * pi), sin(0.9 * pi), sin(pi),
             sin(1.1 * pi), sin(1.2 * pi), sin(1.3 * pi), sin(1.4 * pi), sin(1.5 * pi),
             sin(1.6 * pi), sin(1.7 * pi), sin(1.8 * pi), sin(1.9 * pi), sin(2 * pi)];

// Definir Y_cos como el coseno de cada valor de X
Y_cos = [cos(-2 * pi), cos(-1.9 * pi), cos(-1.8 * pi), cos(-1.7 * pi), cos(-1.6 * pi),
             cos(-1.5 * pi), cos(-1.4 * pi), cos(-1.3 * pi), cos(-1.2 * pi), cos(-1.1 * pi),
             cos(-pi), cos(-0.9 * pi), cos(-0.8 * pi), cos(-0.7 * pi), cos(-0.6 * pi),
             cos(-0.5 * pi), cos(-0.4 * pi), cos(-0.3 * pi), cos(-0.2 * pi), cos(-0.1 * pi),
             cos(0), cos(0.1 * pi), cos(0.2 * pi), cos(0.3 * pi), cos(0.4 * pi), cos(0.5 * pi),
             cos(0.6 * pi), cos(0.7 * pi), cos(0.8 * pi), cos(0.9 * pi), cos(pi),
             cos(1.1 * pi), cos(1.2 * pi), cos(1.3 * pi), cos(1.4 * pi), cos(1.5 * pi),
             cos(1.6 * pi), cos(1.7 * pi), cos(1.8 * pi), cos(1.9 * pi), cos(2 * pi)];

// Graficar seno con etiqueta
plot(X, Y_sin, "Seno");

// Graficar coseno con etiqueta
plot(X, Y_cos, "Coseno");
