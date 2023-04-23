#Mahendra Singh Shaktawat 0827CI201103
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar100
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import BatchNormalization, Dropout
(x_train, y_train), (x_test, y_test) = cifar100.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
model = keras.Sequential(
    [
        keras.Input(shape=(32, 32, 3)),
        layers.Conv2D(16, kernel_size=(3, 3), activation="relu"),
        BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        BatchNormalization(),
        Dropout(0.5),
        layers.Dense(100, activation="softmax"),
    ]
)
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)
early_stopping = EarlyStopping(patience=3, restore_best_weights=True)
history = model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=1,
    validation_split=0.1,
    callbacks=[early_stopping],
)
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)
