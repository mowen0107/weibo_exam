# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 完成predict函数,增加test函数
'''
import numpy as np
import pandas as pd
import pandas.errors as pderr
import errno


class Predict():
    def __init__(self):
        self.userFeatureDir = "/Users/hzt/lab/data_miming/weibo_data/temp/userfeature/"
        self.testDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/testdata/"
        self.resultDir = "/Users/hzt/lab/data_miming/weibo_data/temp/result/"
        self.userFeatureFile = self.userFeatureDir + "washed_userfeature.txt"
        self.testDataFile = self.testDataDir + "washed_test_data.txt"
        self.resultFile = self.resultDir + "result.txt"
        self.userFeature = pd.read_csv(
            self.userFeatureFile,
            header=0,
            sep=',',
            index_col=0,
            encoding='utf-8')
        self.testData = pd.read_csv(
            self.testDataFile,
            names=['luid', 'mid', 'time', 'cont'],
            sep=',',
            encoding='utf-8')

    def test(self):
        test_luid = 'c60533fdb5278412b14379f693f77dd5'
        luid_list = list(self.userFeature.index)
        print(luid_list)
        if test_luid in luid_list:
            print("find it")

    def predict(self):
        ''' 在清洗过后的训练集中查找luid，若存在则进行预测
            若不存在则判断为0
            td前缀表示testdata，uf前缀表示userfeature
        '''
        fcs_list = []
        ccs_list = []
        lcs_list = []
        sum_list = []
        testdataIndex = self.testData.index
        uf_luid_list = list(self.userFeature.index)
        for index in testdataIndex:
            td_luid = self.testData.loc[index]['luid']
            print("------DEBUG LOG :", index, td_luid)
            pre_fcs = 0
            pre_ccs = 0
            pre_lcs = 0
            pre_sum = 0
            if td_luid in uf_luid_list:
                print("------DEBUG LOG FIND:", td_luid)
                subData = self.userFeature.loc[td_luid]
                if subData['avg_fcs'] < 1:
                    pre_fcs = subData['max_fcs'].astype(int)
                else:
                    pre_fcs = subData['avg_fcs'].astype(int)
                if subData['avg_ccs'] < 1:
                    pre_ccs = subData['max_ccs'].astype(int)
                else:
                    pre_ccs = subData['avg_ccs'].astype(int)
                if subData['avg_lcs'] < 1:
                    pre_lcs = subData['max_lcs'].astype(int)
                else:
                    pre_lcs = subData['avg_lcs'].astype(int)
                pre_sum = pre_fcs + pre_ccs + pre_lcs
            fcs_list.append(pre_fcs)
            ccs_list.append(pre_ccs)
            lcs_list.append(pre_lcs)
            sum_list.append(pre_sum)
        self.testData['fcs'] = fcs_list
        self.testData['ccs'] = ccs_list
        self.testData['lcs'] = lcs_list
        self.testData['sum'] = sum_list
        newCols = ['luid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'sum', 'cont']
        self.testData = self.testData.ix[:, newCols]
        self.testData.to_csv(
            self.resultFile, index=False, sep=",", encoding='utf-8')