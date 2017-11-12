#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import h5py
import numpy as np


def data():
    data_path = '/Users/wendyti/PycharmProjects/try_one/Data/'

    # info_name = "information.csv"
    # info_path = data_path + info_name
    # info = pd.read_csv(info_path, encoding='utf-8')

    data_name_1_1 = "data_format1_20170717_20170915.h5"
    data_name_1_2 = "data_format1_20170918_20170922.h5"
    data_name_1_3 = "data_format1_20170925_20170929.h5"
    data_name_1_4 = "data_format1_20171009_20171013.h5"
    data_name_1_5 = "data_format1_20171016_20171020.h5"
    data_name_1_6 = "data_format1_20171023_20171027.h5"

    data_path_1_1 = data_path + data_name_1_1
    data_path_1_2 = data_path + data_name_1_2
    data_path_1_3 = data_path + data_name_1_3
    data_path_1_4 = data_path + data_name_1_4
    data_path_1_5 = data_path + data_name_1_5
    data_path_1_6 = data_path + data_name_1_6

    btData_1_1 = h5py.File(data_path_1_1, mode='r')
    btData_1_2 = h5py.File(data_path_1_2, mode='r')
    btData_1_3 = h5py.File(data_path_1_3, mode='r')
    btData_1_4 = h5py.File(data_path_1_4, mode='r')
    btData_1_5 = h5py.File(data_path_1_5, mode='r')
    btData_1_6 = h5py.File(data_path_1_6, mode='r')

    keys_1_1 = list(btData_1_1.keys())

    data_list = []
    for i in keys_1_1:

        data_cur_min_1 = np.array((list(btData_1_1[i].values()))[3])
        data_cur_min_2 = np.array((list(btData_1_2[i].values()))[3])
        data_cur_min_3 = np.array((list(btData_1_3[i].values()))[3])
        data_cur_min_4 = np.array((list(btData_1_4[i].values()))[3])
        data_cur_min_5 = np.array((list(btData_1_5[i].values()))[3])
        data_cur_min_6 = np.array((list(btData_1_6[i].values()))[3])
        # if i == keys_1_1[0]:
        #     print(data_cur_min_1.shape)
        #     print(data_cur_min_2.shape)
        #     print(data_cur_min_3.shape)
        #     print(data_cur_min_4.shape)
        #     print(data_cur_min_5.shape)
        #     print(data_cur_min_6.shape)
        data = np.vstack((data_cur_min_1, data_cur_min_2))
        data = np.vstack((data, data_cur_min_3))
        data = np.vstack((data, data_cur_min_4))
        data = np.vstack((data, data_cur_min_5))
        data = np.vstack((data, data_cur_min_6))
        data_list.append(pd.DataFrame(data))

    return data_list











