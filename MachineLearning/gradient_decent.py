# %%
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

W = np.random.randn()
b = np.random.randn()

#forward pass
X = np.array([1.5])
target = np.array([0.6]) # target

# Neuron output
y_pred = sigmoid(  W * X + b)
y = np.mean((y_pred - target) ** 2)

# backpropagation
dL_dy = 2 * (y_pred - target)
dy_dz = sigmoid_derivative(W * X + b)
dz_dW = X
dz_db = 1

# gradient of the loss with respect to the weights and bias
dL_dW = dL_dy * dy_dz * dz_dW
dL_db = dL_dy * dy_dz * dz_db

# update
learning_rate = 0.01
W -= learning_rate * dL_dW
b -= learning_rate * dL_db  

print(W, b)
# %%
