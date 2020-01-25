import tensorflow as tf
from tensorflow import keras
import numpy as np

# Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Ed.
# Chapter 10: Introduction to ANNs with Keras

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
print(X_train_full.shape)
print(X_train_full.dtype)

X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                  "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

print(class_names[y_train[0]])

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(300, activation="relu"))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

model.summary()

print(model.layers)

hidden1 = model.layers[1]
print(hidden1.name)
print(model.get_layer('dense') is hidden1)

weights, biases = hidden1.get_weights()
print(weights)
print(weights.shape)

print(biases)
print(biases.shape)

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="sgd",
    metrics=["accuracy"])

history = model.fit(
    X_train, 
    y_train, 
    epochs=30,
    validation_data=(X_valid, y_valid))

model.evaluate(X_test, y_test)

X_new = X_test[:3]
y_proba = model.predict(X_new)
print(y_proba.round(2))

y_pred = model.predict_classes(X_new)
print(y_pred)
print(np.array(class_names)[y_pred])
