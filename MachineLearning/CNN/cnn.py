# %% 
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np
import matplotlib.pyplot as plt


# Load the dataset
(train_images, train_labels), (test_images,
                               test_labels) = datasets.mnist.load_data()

# Assuming train_labels is your array of labels
unique_labels = np.unique(train_labels)
print("Unique labels in the training data:", unique_labels)

# %% 
# Assuming you want to print the first image
first_image = train_images[111]
# Make sure the shape is correct if needed
first_image = first_image.reshape(28, 28)

plt.imshow(first_image, cmap='gray')
plt.title(f'Label: {train_labels[111]}')
plt.colorbar()  # Optionally show the color bar
plt.show()

# %%
# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Reshape for the CNN input
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# Define the model architecture
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Add Dense layers on top
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compile and train the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(f'Test accuracy: {test_acc}')
