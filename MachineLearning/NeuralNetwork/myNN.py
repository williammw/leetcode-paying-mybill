import numpy as np

def initializa_params(input_size, hidden_size, output_size):
  W1 = np.random.randn(input_size, hidden_size) * 0.01
  b1 = np.zeros((hidden_size, 1))
  W2 = np.random.randn(hidden_size, output_size) * 0.01
  b2 = np.zeros((output_size , 1))
  W3 = np.random.randn(hidden_size, output_size) * 0.01
  b3 = np.zeros((output_size, 1))
  
  parameters = {
      "W1": W1,
      "b1": b1,
      "W2": W2,
      "b2": b2,
      "W3": W3,
      "b3": b3
  }
  return parameters

def relu(Z):
  return np.maximum(0, Z)

def relu_derivative(Z):
  return Z > 0


def forward_propagation(X, parameters):
    W1, b1 = parameters['W1'], parameters['b1']
    W2, b2 = parameters['W2'], parameters['b2']
    W3, b3 = parameters['W3'], parameters['b3']

    Z1 = W1.dot(X) + b1
    A1 = relu(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = relu(Z2)
    Z3 = W3.dot(A2) + b3
    A3 = Z3  # Output layer

    cache = (Z1, A1, W1, b1, Z2, A2, W2, b2, Z3, A3, W3, b3)
    return A3, cache



def compute_cost(A3, Y):
    m = Y.shape[1]
    cost = (1/m) * np.sum((A3 - Y) ** 2)
    return cost


def backward_propagation(X, Y, cache):
  """
  Compute the gradients of the neural network's parameters with respect to the cost function.

  Arguments:
  X -- input data of shape (input_size, m)
  Y -- true "label" vector of shape (output_size, m)
  cache -- tuple containing the intermediate values (Z1, A1, W1, b1, Z2, A2, W2, b2, Z3, A3, W3, b3)

  Returns:
  gradients -- dictionary containing the gradients of the parameters (dW1, db1, dW2, db2, dW3, db3)
  """

  (Z1, A1, W1, b1, Z2, A2, W2, b2, Z3, A3, W3, b3) = cache
  m = Y.shape[1]

  dZ3 = 2 * (A3 - Y)
  dW3 = dZ3.dot(A2.T) / m
  db3 = np.sum(dZ3, axis=1, keepdims=True) / m
  dA2 = W3.T.dot(dZ3)

  dZ2 = np.multiply(dA2, relu_derivative(Z2))
  dW2 = dZ2.dot(A1.T) / m
  db2 = np.sum(dZ2, axis=1, keepdims=True) / m
  dA1 = W2.T.dot(dZ2)

  dZ1 = np.multiply(dA1, relu_derivative(Z1))
  dW1 = dZ1.dot(X.T) / m
  db1 = np.sum(dZ1, axis=1, keepdims=True) / m

  gradients = {
    "dW1": dW1, "db1": db1,
    "dW2": dW2, "db2": db2,
    "dW3": dW3, "db3": db3
  }
  return gradients


def update_parameters(parameters, grads, learning_rate):
    parameters['W1'] -= learning_rate * grads['dW1']
    parameters['b1'] -= learning_rate * grads['db1']
    parameters['W2'] -= learning_rate * grads['dW2']
    parameters['b2'] -= learning_rate * grads['db2']
    parameters['W3'] -= learning_rate * grads['dW3']
    parameters['b3'] -= learning_rate * grads['db3']
    return parameters
