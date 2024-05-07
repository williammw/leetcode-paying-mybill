# %%
import random
import torch
import math

# %% 


class Value:
  def __init__(self, data, _children=(), _op='', label=''):
    self.data = data
    self.grad = 0
    self._backward = lambda: None
    self._prev = set(_children)
    self._op = _op
    self.label = label

  # dunder method, for string representation of the object
  def __repr__(self):
    return f"Value({self.data})"

  def __add__(self, other):
    out = Value(self.data + other.data, (self, other), '+')

    def _backward():
      self.grad += 1.0 * out.grad
      other.grad += 1.0 * out.grad
    out._backward = _backward

    return out

  def __mul__(self, other):
    out = Value(self.data * other.data, (self, other), '*')

    def _backward():
      self.grad += other.data * out.grad
      other.grad += self.data * out.grad
    out._backward = _backward
    return out

  def tanh(self):
    x = self.data
    t = (math.exp(2*x) - 1)/(math.exp(2*x) + 1)
    out = Value(t, (self,), 'tanh')

    def _backward():
      self.grad += (1 - t**2) * out.grad
    out._backward = _backward
    return out


# %%
x1 = torch.tensor([2.0], requires_grad=True)  ; x1.requires_grad = True
x2 = torch.tensor([0.0], requires_grad=True)  ; x2.requires_grad = True
w1 = torch.tensor([-3.0], requires_grad=True) ; w1.requires_grad = True
w2 = torch.tensor([1.0], requires_grad=True)  ; w2.requires_grad = True

b = torch.tensor([6.8812725870195432], requires_grad=True)  ; b.requires_grad = True
n = x1*w1 + x2*w2 + b
o = torch.tanh(n)

print(o.data.item())
o.backward()
print('----')
print('x1', x1.grad.item())
print('x2', x2.grad.item())
print('w1', w1.grad.item())
print('w2', w2.grad.item())
# %%

class Neuron:
  def __init__(self, nin):
    self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
    self.b = Value(random.uniform(-1,1))


  def __call__(self, x):
    # w * x + b forward pass
    act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
    out = act.tanh()
    return out

class Layer:
  def __init__(self, nin, m):
    # nin: number of inputs
    # m: number of neurons
    self.neurons = [Neuron(nin) for _ in range(m)]
  
  def __call__(self, x):
    inputs = [Value(xi) if not isinstance(xi, Value) else xi for xi in x]
    return [neuron(inputs) for neuron in self.neurons]

class MLP:

  def __init__(self, nin, nouts):
    sz = [nin] + nouts
    self.layers = [Layer(a, b) for a, b in zip(sz[:-1], sz[1:])]

  def __call__(self, x):
    for layer in self.layers:
      x = layer(x)
    return x
  

# Example usage
x = [2.0, 3.0, -1.0]  # Input values
n = MLP(3, [4, 4, 1]) # 3 input, 1 output with 2 hidden layers of 4 neurons each
# %%
xs = [
  [2.0, 3.0, -1.0],
  [3.0, -0.0, 0.5],
  [0.5, 1.0, 1.0],
  [1.0,1.0, -1.0]
]
ys = [1.0,-1.0,-1.0, 1.0]
ypred = [n(x) for x in xs]
ypred
# %%
[(yout - ygt) **2 for ygt, yout in zip(ys, ypred)]
# %%
