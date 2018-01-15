# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180113
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 添加用户分布分析
'''
import numpy as np
import pandas as pd
import pandas.errors as pderr
import copy
import errno


class Preprocessor:
    ''' 对数据进行预处理，了解大致情况
    '''

    def __init__(self):
        self.trainDataDir = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        # self.trainDataDir = "/Users/hzt/lab/data_miming/weibo_data/temp/"
        self.trainDataFile = "washedTrainData.txt"
        self.trainData = self.readTrainData()

    def readTrainData(self):
        ''' 读取训练集文件,返回pandas格式的Dataframe
        '''
        data = None
        filePath = self.trainDataDir + self.trainDataFile
        try:
            data = pd.read_csv(filePath, encoding='utf8', header=0)
            print("------Length of data:", len(data))
        except OSError as e:
            print("------ERROR LOG 打开训练集数据出错:", e)
            print("------找不到" + filePath + "文件")
            return None
        return data

    def getUserFeature(self):
        ''' 得到用户特征，包括各项数值的极值、平均值
                luid 用户id
                count 出现的频次
                max_fcs 最大转发量
                min_fcs 最小转发量
                avg_fcs 平均转发量
                max_ccs 最大评论数
                min_ccs 最小评论数
                avg_ccs 平均评论数
                max_lcs 最大赞数
                min_lcs 最小赞数
                avg_lcs 平均赞数
                max_sum 最大互动数
                min_sum 最小互动数
                avg_sum 平均互动数
                above_avg_rate 高于平均值的概率
            并写入userfeature.txt
        '''
        fileName = "userfeature.txt"
        filePath = self.trainDataDir + fileName
        trainData = copy.deepcopy(self.trainData)
        userCount = trainData['luid'].value_counts()
        userList = copy.deepcopy(userCount.index)
        userCount.to_csv(
            self.trainDataDir + "usercount.txt", index=True, sep=',')
        userFeature = pd.read_csv(
            self.trainDataDir + "usercount.txt",
            names=['luid', 'count'],
            sep=',')
        max_fcs_list = []
        min_fcs_list = []
        avg_fcs_list = []
        max_ccs_list = []
        min_ccs_list = []
        avg_ccs_list = []
        max_lcs_list = []
        min_lcs_list = []
        avg_lcs_list = []
        max_sum_list = []
        min_sum_list = []
        avg_sum_list = []
        i = 0
        for user in userList:
            # 筛选出luid相同的行
            print("------DEBUG LOG luid:", i, user)
            subData = trainData.loc[(trainData['luid'] == user)]
            max_fcs = subData['fcs'].max()
            min_fcs = subData['fcs'].min()
            avg_fcs = subData['fcs'].mean()
            max_ccs = subData['ccs'].max()
            min_ccs = subData['ccs'].min()
            avg_ccs = subData['ccs'].mean()
            max_lcs = subData['lcs'].max()
            min_lcs = subData['lcs'].min()
            avg_lcs = subData['lcs'].mean()
            max_sum = subData['sum'].max()
            min_sum = subData['sum'].min()
            avg_sum = subData['sum'].mean()
            max_fcs_list.append(max_fcs)
            min_fcs_list.append(min_fcs)
            avg_fcs_list.append(avg_fcs)
            max_ccs_list.append(max_ccs)
            min_ccs_list.append(min_ccs)
            avg_ccs_list.append(avg_ccs)
            max_lcs_list.append(max_lcs)
            min_lcs_list.append(min_lcs)
            avg_lcs_list.append(avg_lcs)
            max_sum_list.append(max_sum)
            min_sum_list.append(min_sum)
            avg_sum_list.append(avg_sum)
            i += 1
        userFeature['max_fcs'] = max_fcs_list
        userFeature['min_fcs'] = min_fcs_list
        userFeature['avg_fcs'] = avg_fcs_list
        userFeature['max_ccs'] = max_ccs_list
        userFeature['min_ccs'] = min_ccs_list
        userFeature['avg_ccs'] = avg_ccs_list
        userFeature['max_lcs'] = max_lcs_list
        userFeature['min_lcs'] = min_lcs_list
        userFeature['avg_lcs'] = avg_lcs_list
        userFeature['max_sum'] = max_sum_list
        userFeature['min_sum'] = min_sum_list
        userFeature['avg_sum'] = avg_sum_list
        userFeature.to_csv(
            self.trainDataDir + "userfeature.txt", index=False, sep=',')
        return userFeature
