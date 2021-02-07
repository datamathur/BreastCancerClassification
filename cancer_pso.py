from nn import relu, sigmoid, tanh, softmax
from nn.model import Model
from nn.layers import Layer
from nn.losses import CrossEntropyLoss, BinaryCrossEntropyLoss
from nn.pipeline import DataLoader
import numpy as np
import pandas as pd
import time

t = time.process_time()

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

from sklearn.preprocessing import MinMaxScaler
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

def one_hot(y, depth=10):
    y_1hot = np.zeros((y.shape[0], depth))
    y_1hot[np.arange(y.shape[0]), y] = 1
    return y_1hot

y_train = one_hot(y_train.astype('int'), depth=2)
y_test = one_hot(y_test.astype('int'), depth=2)

def accuracy(y, y_hat):
    y = np.argmax(y, axis=1)
    y_hat = np.argmax(y_hat, axis=1)

    return np.mean(y==y_hat)

model = Model()
model.add_layer(Layer(30, 7, relu)))
model.add_layer(Layer(7, 2, softmax))

model.compile(CrossEntropyLoss, DataLoader, accuracy, batches_per_epoch=(x_train.shape[0]//16)+1, n_workers=12)
model.fit(X=x_train, y=y_train, epochs=100)
y_hat = model.predict(x_test)

print('Accuracy on test:', accuracy(y_test, y_hat))

elaped_time = time.process_time() - t 
print("Elapsed Time:", elaped_time)
