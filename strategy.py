#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
from sklearn.externals import joblib
import pandas as pd
import numpy as np

length = 120
my_cash_balance_lower_limit = 3000000.
asset_index = 3

def generate_datalist(datalist):
    open_price = datalist[0][:, 0]
    close_price = datalist[-1][:, 3]
    high = np.max([array[:,1] for array in datalist],axis=0)
    low = np.min([array[:,2] for array in datalist],axis=0)
    volume = np.median([array[:,-1] for array in datalist], axis=0)
    mer = np.array([open_price, high, low, close_price, volume])
    return mer

def handle_bar(timer, data, info, init_cash, transaction, detail_last_min, memory):
    position_new = detail_last_min[0]

    if(timer == 0):
        memory.data_list = list()
    if(timer % length == 0 and timer != 0):
        memory.data_list.append(data)
        bar = generate_datalist(memory.data_list)
        ex_bar = bar[:,asset_index]

        for index in range(2,4):
            clf = joblib.load('svm_models/filename_'+str(index)+'.pkl')
            value_predict = clf.predict(ex_bar.reshape(1, -1))

            if value_predict == 1:
                if detail_last_min[1] - my_cash_balance_lower_limit > 100000:
                    position_new[index] += 10

            elif value_predict == 0:
                if detail_last_min[1] - my_cash_balance_lower_limit < 100000:
                    position_new[index] -= 10
        memory.data_list = list()
    else:
        memory.data_list.append(data)

    return position_new, memory



if __name__ == '__main__':

    pass
