#Mahendra Singh Shaktawat 0827CI201103
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers, optimizers
X = np.random.rand(1000, 10)
y = np.random.randint(0, 2, (1000, 1))
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer=optimizers.RMSprop(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X, y, epochs=20, validation_split=0.2)
test_loss, test_acc = model.evaluate(X, y, verbose=0)
print('Test accuracy:', test_acc)
