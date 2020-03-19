
# -------------------------------------------------------------------------------
# 0. IMPORT LIBRARIES
# -------------------------------------------------------------------------------


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------------------------------
# 2. PREPARE THE DATA
# -------------------------------------------------------------------------------


# Generate the dataset

X_train = np.arange(10).reshape((10, 1))
y_train = np.array([1.0, 1.3, 3.1, 2.0, 5.0, 6.3, 6.6, 7.4, 8.0, 9.0])


# Plot the dataset

plt.plot(X_train, y_train, 'o',)
plt.xlabel('x')
plt.ylabel('y')


# Standardize the features

X_train_norm = (X_train - np.mean(X_train)) / np.std(X_train)


# Create a dataset

ds_train_orig = tf.data.Dataset.from_tensor_slices((tf.cast(X_train_norm, tf.float32), tf.cast(y_train, tf.float32)))


# Instantiate a Model by subclassing the Model class

class MyModel(tf.keras.Model):

    # Define the layers

    def __init__(self):

        super(MyModel, self).__init__()

        self.w = tf.Variable(0.0, name='weight')
        self.b = tf.Variable(0.0, name='bias')

    # Implement the forward pass

    def call(self, x):

        return self.w * x + self.b


# Instantiate a subclassed model

model = MyModel()


# Build the model based on input shapes received

model.build(input_shape=(None, 1))


# Print the model summary

model.summary()


# Define the loss function

def loss_fn(y_true, y_pred):

    return tf.reduce_mean(tf.square(y_true - y_pred))


# Testing the function:

yt = tf.convert_to_tensor([1.0])
yp = tf.convert_to_tensor([1.5])

print(loss_fn(yt, yp))


# Train the model

def train(model, inputs, outputs, learning_rate):

    with tf.GradientTape() as tape:

        current_loss = loss_fn(model(inputs), outputs)

# -------------------------------------------------------------------------------
# 5. GENERAL
# -------------------------------------------------------------------------------


# Show plots

plt.show()
