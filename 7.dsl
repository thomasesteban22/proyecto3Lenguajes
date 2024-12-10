X = [[0, 0], [0, 1], [1, 0], [1, 1]];
y = [0, 1, 1, 0];

mlp_model = mlp(2, 5, 1, 0.01, 1000, X, y);

test_input = [[0, 0], [0, 1], [1, 0], [1, 1]];
result = mlp_model.predict(test_input);

log(result);
