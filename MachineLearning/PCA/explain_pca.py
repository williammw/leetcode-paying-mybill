''' 
explain PCA once and for all
PCA is a dimensionality reduction 
while preserving as much variability as possible. 
It's particularly useful in preprocessing high-dimensional 
data before applying machine learning algorithms, 
enhancing visualizations, or reducing noise.

PCA is sensitive to the variance of the data.
real-world example using PCA such as  image compression,  face recognition, and data visualization.
'''


# %%
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# %%
