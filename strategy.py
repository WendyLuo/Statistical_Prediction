#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Created on Mon Sep 18 15:27:48 2017

@author: MAngO
"""

# import pandas as pd
# import h5py
# import os
# import numpy as np
#
# os.chdir('/Users/wendyti/PycharmProjects/wendy_strategy')
# import svm
# import read_data
#
# cls_global = []
# my_cash_balance_lower_limit = 3000000.
# asset_index = 2
#
#
# def train():
#     data_list = read_data.data()
#     for i in range(13):
#         global cls_global
#         data_train, value_train = svm.load_data(data_list[i])
#         svm_classifier = svm.get_classifier(data_train, value_train)
#         cls_global.append(svm_classifier)
#     return cls_global
#
#
# def handle_bar(timer, data, info, init_cash, transaction, detail_last_min, memory):
#     train()
#     position_new = detail_last_min[0]
#
#     for index in range(len(cls_global)):
#         # data[index] = data[index].reshape(1, -1)
#         value_predict = cls_global[index].predict(data[index].reshape(1, -1))
#         print('***')
#         print(value_predict)
#         if value_predict == 1:
#             if detail_last_min[1] > my_cash_balance_lower_limit:
#                 position_new[asset_index] += 10.
#
#         elif value_predict == 0:
#             if detail_last_min[1] > my_cash_balance_lower_limit:
#                 position_new[asset_index] -= 10.
#
#     return position_new, memory
#
#
# if __name__ == '__main__':
#     # data_list = read_data.data()
#     # cls_global= []
#     # for i in range(13):
#     #     data_train, value_train = svm.load_data(data_list[i])
#     #     svm_classifier = svm.get_classifier(data_train, value_train)
#     #     cls_global.append(svm_classifier)
#     #
#     # train()
#     pass
import read_data
import svm_model
from sklearn.externals import joblib


my_cash_balance_lower_limit = 3000000.
asset_index = 2


def train():
    pass


def handle_bar(timer, data, info, init_cash, transaction, detail_last_min, memory):
    position_new = detail_last_min[0]

    for index in range(13):
        # data[index] = data[index].reshape(1, -1)
        clf = joblib.load('/Users/wendyti/PycharmProjects/wendy_strategy/svm_models/filename_'+str(index)+'.pkl')
        value_predict = clf.predict(data[index].reshape(1, -1))
        if value_predict == 1:
            if detail_last_min[1] > my_cash_balance_lower_limit:
                position_new[asset_index] += 10.

        elif value_predict == 0:
            if detail_last_min[1] > my_cash_balance_lower_limit:
                position_new[asset_index] -= 10.

    return position_new, memory


if __name__ == '__main__':

    data_list = read_data.data()
    for i in range(13):
        data_train, value_train = svm_model.load_data(data_list[i])
        svm_classifier = svm_model.get_classifier(data_train, value_train)
        # print(type(svm_classifier))
        joblib.dump(svm_classifier, 'svm_models/filename_'+str(i)+'.pkl')
