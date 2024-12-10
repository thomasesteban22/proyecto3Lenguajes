// test_regression.dsl

var X = [[1],[2],[3],[4],[5]];
var y = [2,4,6,8,10];
linearRegression(X, y, lrModel);

// Solo imprime el modelo, no sus propiedades mediante '.'
// El visitor imprime detalles del modelo en print
print(lrModel);

var predInput = [[6]];
var pred = lrModel.predict(predInput); // No está definido en gramática el punto, define mejor una función DSL predict(model, data);
// Por ahora, asume no puedes predecir con notación punto.
// Cambia a algo como: // var result = predict(lrModel, predInput); y define la función en la gramática y el visitor.
