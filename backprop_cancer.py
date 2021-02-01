import numpy as np
import pandas as pd 
from tensorflow import keras
from keras import layers
from keras.utils.np_utils import to_categorical 
from keras.models import Sequential
from keras.optimizers import SGD
import time

t = time.process_time()

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

from sklearn.preprocessing import MinMaxScaler, LabelEncoder
scaler = MinMaxScaler()

df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns = np.append(cancer['feature_names'], ['target']))
all_data = df_cancer.values
scaler.fit(all_data)

np.random.shuffle(all_data)

split = int(0.9 * all_data.shape[0])

x_train = all_data[:split, 0:-1]
x_test = all_data[split:, 0:-1]
y_train = all_data[:split, -1]
y_test = all_data[split:, -1]

y_train = to_categorical(y_train, num_classes = 2)
y_test = to_categorical(y_test, num_classes = 2)

Model = keras.Sequential(
    [
        keras.Input(shape = (30)),
        layers.Dense(7, activation = "relu"),
        layers.Dense(2, activation = "softmax"),
    ]
)

lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=1e-2,
    decay_steps=1000,
    decay_rate=0.9)
optimizer = keras.optimizers.Adam(learning_rate=lr_schedule)

Model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
Model.fit(x_train, y_train, epochs=100, batch_size=16)

score = Model.evaluate(x_test, y_test)
print("Test accuracy:", score[1])

elaped_time = time.process_time() - t 
print("Elapsed Time:", elaped_time)     