#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import h5py
import numpy as np

import pandas as pd
# from pandas import Series, DataFrame
from sklearn import svm


train = 15
correct = 0
train_original = train
i = 0


def load_data(future_data):

    future_data = future_data.astype(float)

    value = pd.Series(future_data[0].shift(-1)-future_data[3].shift(-1),index=future_data.index)
    value[value >= 0] = 0
    value[value < 0] = 1

    L = len(future_data)
    data_train = future_data[0:L-1]
    value_train = value[0:L-1]

    return data_train, value_train

# Get future_data['Next_Open'], and value(表示升降情况，1为升，0为降)


def get_classifier(data_train, value_train):
    classifier = svm.SVC()
    classifier.fit(data_train, value_train)
    print('get classifier')

    return classifier








