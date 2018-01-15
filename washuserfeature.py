# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 
'''
import numpy as np
import pandas as pd
import pandas.errors as pderr
import copy
import errno


class WashUserFeature:
    def __init__(self):
        self.trainDataDir = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        # self.trainDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/"
        self.inputFilePath = self.trainDataDir + "userfeature.txt"
        self.outputFilePath = self.trainDataDir + "washeduserfeature.txt"

    def run(self):
        ''' 对得到的用户特征进行清洗
            可以认为互动数为0的用户对结果没有太大影响，直接从中删除
        '''
        userFeature = pd.read_csv(
            self.inputFilePath, header=0, sep=',', encoding='utf8')
        for index in userFeature.index:
            print("------DEBUG LOG index:", index)
            avg_sum = userFeature.loc[index]['avg_sum']
            if avg_sum == 0:
                print("------DROP LOG 删除无用行:", index)
                userFeature.drop(index, axis=0, inplace=True)
        userFeature.to_csv(self.outputFilePath, index=False, sep=',')
