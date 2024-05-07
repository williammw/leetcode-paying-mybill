# %%
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNeuralNet(nn.Module):
  def __init__(self):
    # Call the parent class constructor
    super(SimpleNeuralNet, self).__init__()
    # Hidden layer 1 (3,4) 3 means input size and 4 means output size
    self.hidden1 = nn.Linear(3, 4)
    # Hidden layer 2 
    self.hidden2 = nn.Linear(4, 4)
    # Output layer
    self.output = nn.Linear(4, 1)
    # Activation function
    self.relu = nn.ReLU()

  def forward(self, x):
    # Forward pass through the network 
    # self.rele is the activation function 
    x = self.relu(self.hidden1(x))
    x = self.relu(self.hidden2(x))

    x = self.output(x) 

    return x
  

# Create a model
net = SimpleNeuralNet()

# define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

# Example data 
# torch.randn(10, 3) means 10 samples and 3 features
inputs = torch.randn(10, 3)
targets = torch.randn(10, 1) # 10 samples and 1 output

# Validation dataset
val_inputs = torch.randn(20, 3)  # 20 validation examples
val_targets = torch.randn(20, 1)  # Corresponding targets

num_epochs = 500

for epoch in range(num_epochs):

  net.train()  # Explicitly setting the training mode
  # Forward pass
  outputs = net(inputs)
  loss = criterion(outputs, targets)

  # Backward pass
  optimizer.zero_grad()

  # Compute gradients 
  loss.backward()
  # Update the weights
  optimizer.step()

  net.eval() # Set the network to evaluation mode
  with torch.no_grad():  # Gradient computation is not needed for validation
    # Validation loss
    val_outputs = net(val_inputs)
    val_loss = criterion(val_outputs, val_targets)

  # Print loss every 50 epochs
    if (epoch+1) % 50 == 0:
        print(
            f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}, Val Loss: {val_loss.item():.4f}')
# %%
