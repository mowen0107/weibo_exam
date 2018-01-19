# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 修改userfeature路径
'''
import numpy as np
import pandas as pd
import pandas.errors as pderr
import copy
import errno


class WashUserFeature:
    def __init__(self):
        self.userFeatureDir = "/Users/hzt/lab/data_miming/weibo_exam/data/userfeature/"
        self.inputFilePath = self.userFeatureDir + "userfeature.txt"
        self.outputFilePath = self.userFeatureDir + "washed_userfeature.txt"

    def run(self):
        ''' 对得到的用户特征进行清洗
            可以认为互动数为0的用户对结果没有太大影响，直接从中删除
        '''
        userFeature = pd.read_csv(
            self.inputFilePath, header=0, sep='\t', encoding='utf8')
        for index in userFeature.index:
            print("------DEBUG LOG index:", index)
            avg_sum = userFeature.loc[index]['avg_sum']
            if avg_sum == 0:
                print("------DROP LOG 删除无用行:", index)
                userFeature.drop(index, axis=0, inplace=True)
        userFeature.to_csv(self.outputFilePath, index=False, sep='\t')
