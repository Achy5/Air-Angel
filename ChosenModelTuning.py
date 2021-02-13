import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor

csv = pd.read_csv("NONANSSUMMEDANDREADY.csv")

x = csv[["AirTemp","Press","UMR"]]
y = csv[["NO","NO2","O3","PM10"]]

xscaler = StandardScaler()
yscaler = StandardScaler()

xscaler.fit(x)
yscaler.fit(y)

xsc = xscaler.transform(x)
xsccont = np.ascontiguousarray(xsc)
ysc = yscaler.transform(y)
ysccont = np.ascontiguousarray(ysc)

xtrain, xtest, ytrain, ytest = train_test_split(
    xsccont, ysccont, test_size=0.2)

regr = MLPRegressor(hidden_layer_sizes = (10,), activation = 'tanh', solver ='sgd',
                   learning_rate = 'adaptive')

regr.fit(xtrain,ytrain)
