# https://github.com/karpathy/micrograd/blob/master/micrograd/nn.py
#  %%
import math
import numpy as np
import matplotlib.pyplot as plt

# %%
def f(x):
    return 3*x**2 - 4*x + 5

xs = np.arange(-5,5, 0.25)
ys = f(xs)
plt.plot(xs, ys)


# %%
h = 0.0000000001
x = 3.1
# when x = 3.0 the slope is 14, because 3*2*3 - 4 = 14
# positive slope moves upward on a graph from left to right
# negative slope moves downward on a graph from left to right
# (f(x + h) - f(x)) / h

# %%
a = 2.0
b = -3.0
c = 10.0
d = a*b + c
print(d)
# %%
h = 0.0001

a = 2.0
b = -3.0
c = 10.0
d = a*b + c
d1 = a * b  + c
b += h
d2 = a * b + c
print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1) / h)

# %%
class Value:
  def __init__(self, data, _children=(), _op='', label=''):
    self.data = data
    self.grad = 0
    self._prev = set(_children)
    self._op = _op
    self.label = label
  
  # dunder method, for string representation of the object
  def __repr__(self):
    return f"Value({self.data})"
  
  def __add__(self, other):
    out = Value(self.data + other.data, (self, other), '+')
    return out
  
  def __mul__(self, other):
    out = Value(self.data * other.data, (self, other), '*')
    return out
  
  def exp(self):
    x = self.data
    t =(math.exp(2*x) - 1)/(math.exp(2*x) + 1)
    out = Value(t, (self,), 'tanh')
    return out
  
  
  

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a*b; e.label = 'e'
d = e + c; d.label = 'd'
f = Value(-2.0, label='f')
L = d * f; L.label = 'L'
L
# d._prev
# d._op
#a*b + c
#a.__mul__(b).__add__(c)

# %%
from graphviz import Digraph


def trace(root):
  # builds a set of all nodes and edges in a graph
  nodes, edges = set(), set()

  def build(v):
    if v not in nodes:
      nodes.add(v)
      for child in v._prev:
        edges.add((child, v))
        build(child)
  build(root)
  return nodes, edges


def draw_dot(root):
  dot = Digraph(format='svg', graph_attr={
                'rankdir': 'LR'})  # LR = left to right

  nodes, edges = trace(root)
  for n in nodes:
    uid = str(id(n))
    # for any value in the graph, create a rectangular ('record') node for it
    dot.node(name=uid, label="{ %s | data %.4f | grad %.4f }" % (
        n.label, n.data, n.grad), shape='record')
    if n._op:
      # if this value is a result of some operation, create an op node for it
      dot.node(name=uid + n._op, label=n._op)
      # and connect this node to it
      dot.edge(uid + n._op, uid)

  for n1, n2 in edges:
    # connect n1 to the op node of n2
    dot.edge(str(id(n1)), str(id(n2)) + n2._op)

  return dot

# %%

# the graph 'grad' mean, the derivative of the value (example 'L') change
# by amount of 'h', how does 'L' changes, 

# L = d * f
# dL/dd =?f
# (f(x+h) - f(x)) / h
# (d*f + h*f - d*f) / h
# (h*f) / h
# f 
# %% 

# dL / de = -2.0
# %%


def lol():
  h = 0.001
  a = Value(2.0, label='a')
  b = Value(-3.0, label='b')
  c = Value(10.0, label='c')
  e = a*b;e.label = 'e'
  d = e + c;d.label = 'd'
  f = Value(-2.0, label='f')
  L = d * f;L.label = 'L'
  L1 = L.data

  a = Value(2.0 , label='a')
  b = Value(-3.0, label='b')
  b.data += h
  c = Value(10.0, label='c')
  e = a*b; e.label = 'e'
  d = e + c; d.label = 'd'
  f = Value(-2.0 , label='f')
  L = d * f; L.label = 'L'
  L2 = L.data 

  print((L2-L1)/h)

lol()

# %%
draw_dot(L) 

# %%
'''
WANT
dL / dc  = (dL / dd) * (dd / dc)
Know
dL / dd 
dd / dc
'''
# a.grad = -2.0 * -3.0 # de/da = value of b
# b.grad = -2.0 * 2.0 # de/db = value of a

# %%
# input x1,x2
x1 = Value(2.0, label='x1')
x2 = Value(0.0, label='x2')
# weight w1w2
w1 = Value(-3.0, label='w1')
w2 = Value(1.0, label='w2')
# bias b
b = Value(6.8813751, label='b')
# x1*w1 + x2*w2 + b
x1w1 = x1 * w1; x1w1.label = 'x1w1'
x2w2 = x2 * w2; x2w2.label = 'x2w2'
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label = 'x1w1 + x2w2'
n = x1w1x2w2 + b; n.label = 'n'
o =n.exp(); o.label = 'o'


# %%
o.grad = 1;n.grad =0.5;b.grad = 0.5
x1w1x2w2.grad = 0.5
x1w1.grad = 0.5
x2w2.grad = 0.5
x2.grad = w2.data * x2w2.grad
w2.grad = x2.data * x2w2.grad
x1.grad = w1.data * x1w1.grad
w1.grad = x1.data * x1w1.grad
# %%
draw_dot(o)

# %%
# o = tanh(n)
# do/dn = 1 - o**2
1 - o.data**2
# %%
