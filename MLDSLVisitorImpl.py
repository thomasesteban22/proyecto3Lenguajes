# MLDSLVisitorImpl.py
import math
import numpy as np
import matplotlib.pyplot as plt
import re

from MLDSLParser import MLDSLParser
from MLDSLVisitor import MLDSLVisitor

class LinearRegressionManual:
    def __init__(self):
        self.coefficients = None
        self.intercept = None
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        self.intercept = theta_best[0]
        self.coefficients = theta_best[1:]
    def predict(self, X):
        X = np.array(X)
        return self.intercept + X @ self.coefficients

class MultiLayerPerceptron:
    def __init__(self, input_size, hidden_size=5, output_size=1, learning_rate=0.01, epochs=1000):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.lr = learning_rate
        self.epochs = epochs
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros(output_size)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def forward(self, X):
        self.Z1 = X @ self.W1 + self.b1
        self.A1 = self.sigmoid(self.Z1)
        self.Z2 = self.A1 @ self.W2 + self.b2
        self.A2 = self.sigmoid(self.Z2)
        return self.A2

    def backward(self, X, y, output):
        error = output - y
        dW2 = self.A1.T @ error
        db2 = np.sum(error, axis=0)
        dA1 = error @ self.W2.T
        dZ1 = dA1 * self.A1 * (1 - self.A1)
        dW1 = X.T @ dZ1
        db1 = np.sum(dZ1, axis=0)

        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

    def train(self, X, y):
        X = np.array(X)
        y = np.array(y).reshape(-1,1)
        for _ in range(self.epochs):
            output = self.forward(X)
            self.backward(X, y, output)

    def predict(self, X):
        X = np.array(X)
        out = self.forward(X)
        return (out > 0.5).astype(int)

class KMeansManual:
    def __init__(self, k=3, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = None

    def fit(self, X):
        X = np.array(X)
        indices = np.random.choice(X.shape[0], self.k, replace=False)
        self.centroids = X[indices]

        for _ in range(self.max_iterations):
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)
            new_centroids = np.array([
                X[labels==i].mean(axis=0) if np.any(labels==i) else self.centroids[i]
                for i in range(self.k)
            ])
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids
        return self.centroids, labels

    def predict(self, X):
        X = np.array(X)
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels

class MLDSLVisitorImpl(MLDSLVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.current_function = None
        self.return_value = None

    def getVar(self, name):
        if name not in self.variables:
            print(f"Error: La variable '{name}' no está definida.")
            return 0
        return self.variables[name]

    def visitAddExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left + right

    def visitSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left - right

    def visitMulExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left * right

    def visitDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if right == 0:
            print("Error: División por cero.")
            return 0
        return left / right

    def visitPowerExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left ** right

    def visitNegateExpr(self, ctx):
        value = self.visit(ctx.expression())
        return -value

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitNumberExpr(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitVariableExpr(self, ctx):
        var_name = ctx.ID().getText()
        return self.getVar(var_name)

    def visitFuncCallExpr(self, ctx):
        return self.visit(ctx.functionCall())

    def visitTrigExpr(self, ctx):
        func = ctx.trigFunction().getChild(0).getText()
        arg = self.visit(ctx.trigFunction().expression())
        if func == 'sin':
            return math.sin(arg)
        elif func == 'cos':
            return math.cos(arg)
        elif func == 'tan':
            return math.tan(arg)

    def visitSqrtExpr(self, ctx):
        value = self.visit(ctx.expression())
        return math.sqrt(value)

    def visitListExpr(self, ctx):
        le_ctx = ctx.listExpression()
        elems = [self.visit(e) for e in le_ctx.expression()]
        return elems

    def visitVariableDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        if self.current_function:
            self.return_value = value
        else:
            self.variables[var_name] = value
        return value

    def visitConditional(self, ctx):
        cond = self.visit(ctx.condition())
        # ifStats son las sentencias del if
        if cond:
            if ctx.ifStats:
                for s in ctx.ifStats:
                    self.visit(s)
        else:
            if ctx.elseStats:
                for s in ctx.elseStats:
                    self.visit(s)
        return None

    def visitCondition(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '>=':
            return left >= right
        elif op == '<=':
            return left <= right
        return False

    def visitLoop(self, ctx):
        keyword = ctx.getChild(0).getText()
        if keyword == 'for':
            self.visit(ctx.assignment(0))
            while self.visit(ctx.condition()):
                for s in ctx.statement():
                    self.visit(s)
                self.visit(ctx.assignment(1))
        elif keyword == 'while':
            while self.visit(ctx.condition()):
                for s in ctx.statement():
                    self.visit(s)
        return None

    def visitFunctionDeclaration(self, ctx):
        func_name = ctx.ID().getText()
        params = []
        if ctx.parameterList():
            params = [p.getText() for p in ctx.parameterList().ID()]
        body = ctx.statement()
        return_expr = ctx.expression()
        self.functions[func_name] = (params, body, return_expr)
        return None

    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        args = []
        if ctx.argumentList():
            args = [self.visit(a) for a in ctx.argumentList().expression()]
        if func_name in self.functions:
            params, body, return_expr = self.functions[func_name]
            if len(args) != len(params):
                print(f"Error: la función '{func_name}' espera {len(params)} args, recibió {len(args)}.")
                return 0
            old_vars = self.variables.copy()
            self.current_function = func_name
            for param, arg in zip(params, args):
                self.variables[param] = arg
            for s in body:
                self.visit(s)
            ret = self.visit(return_expr)
            self.variables = old_vars
            self.current_function = None
            return ret
        else:
            print(f"Error: la función '{func_name}' no está definida.")
            return 0

    def visitPlotStatement(self, ctx):
        x_var = ctx.ID(0).getText()
        y_var = ctx.ID(1).getText()
        x_data = self.getVar(x_var)
        y_data = self.getVar(y_var)
        if isinstance(x_data, list) and isinstance(y_data, list):
            plt.plot(x_data, y_data)
            plt.savefig("grafica.png")
            plt.close()
            print("Gráfica guardada en grafica.png")
        else:
            print("Error: Los datos para graficar deben ser listas numéricas.")
        return None

    def visitFileOperation(self, ctx):
        op = ctx.getChild(0).getText()
        if op == 'read':
            filename = ctx.STRING().getText().strip('"')
            var_name = ctx.ID().getText()
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.variables[var_name] = content
            except FileNotFoundError:
                print(f"Error: el archivo '{filename}' no se encontró.")
        elif op == 'write':
            filename = ctx.STRING().getText().strip('"')
            var_name = ctx.ID().getText()
            content = self.variables.get(var_name, '')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(content))
        return None

    def visitMatrixDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        m = self.visit(ctx.matrixExpr())
        self.variables[var_name] = m
        return m

    def visitMatrixExpr(self, ctx):
        rows = ctx.matrixRows().matrixRow()
        matrix = [self.visit(r) for r in rows]
        return np.array(matrix)

    def visitMatrixRow(self, ctx):
        elems = [self.visit(e) for e in ctx.expression()]
        return elems

    def visitMatrixInverse(self, ctx):
        var_name = ctx.ID(0).getText()
        mat_name = ctx.ID(1).getText()
        mat = self.getVar(mat_name)
        if isinstance(mat, np.ndarray):
            try:
                inv = np.linalg.inv(mat)
                self.variables[var_name] = inv
            except np.linalg.LinAlgError:
                print(f"Error: la matriz '{mat_name}' no es invertible.")
        else:
            print(f"Error: '{mat_name}' no es una matriz.")
        return None

    def visitMatrixTranspose(self, ctx):
        var_name = ctx.ID(0).getText()
        mat_name = ctx.ID(1).getText()
        mat = self.getVar(mat_name)
        if isinstance(mat, np.ndarray):
            self.variables[var_name] = mat.T
        else:
            print(f"Error: '{mat_name}' no es una matriz.")
        return None

    def visitMlOperation(self, ctx):
        op = ctx.getChild(0).getText()
        if op == 'linearRegression':
            X_var = ctx.ID(0).getText()
            y_var = ctx.ID(1).getText()
            model_var = ctx.ID(2).getText()
            X = self.getVar(X_var)
            y = self.getVar(y_var)
            if isinstance(X, list) and isinstance(y, list):
                model = LinearRegressionManual()
                model.fit(X, y)
                self.variables[model_var] = model
        elif op == 'perceptron':
            X_var = ctx.ID(0).getText()
            y_var = ctx.ID(1).getText()
            model_var = ctx.ID(2).getText()
            X = self.getVar(X_var)
            y = self.getVar(y_var)
            lr = 0.01
            epochs = 1000
            if ctx.NUMBER(0):
                lr = float(ctx.NUMBER(0).getText())
            if ctx.NUMBER(1):
                epochs = int(ctx.NUMBER(1).getText())
            if isinstance(X, list) and isinstance(y, list) and len(X)>0 and isinstance(X[0], list):
                input_size = len(X[0])
                model = MultiLayerPerceptron(input_size=input_size, learning_rate=lr, epochs=epochs)
                model.train(X, y)
                self.variables[model_var] = model
        elif op == 'clustering':
            X_var = ctx.ID(0).getText()
            model_var = ctx.ID(1).getText()
            k = 3
            if ctx.NUMBER():
                k = int(ctx.NUMBER(0).getText())
            X = self.getVar(X_var)
            if isinstance(X, list):
                model = KMeansManual(k=k)
                centroids, labels = model.fit(X)
                self.variables[model_var] = {'centroids': centroids, 'labels': labels}
        return None

    def visitPrintStatement(self, ctx):
        if ctx.expression():
            val = self.visit(ctx.expression())
            if isinstance(val, LinearRegressionManual):
                print("LinearRegressionModel:", "coeff=", val.coefficients, "intercept=", val.intercept)
            elif isinstance(val, MultiLayerPerceptron):
                print("MultiLayerPerceptron Model (no propiedades definidas)")
            elif isinstance(val, dict) and 'centroids' in val and 'labels' in val:
                print("KMeansModel:", val)
            else:
                print(val)
        else:
            txt = ctx.STRING().getText().strip('"')
            print(txt)
        return None
