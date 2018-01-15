# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180114
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 增加sum字段
'''
import pandas as pd
import numpy as np
from numpy import nan as NA


class Washing():
    ''' 对训练集和测试集进行清洗
        校正或者删除错误的行
    '''

    def __init__(self):
        self.originPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/pro3_data/"
        self.outputPath = "C:/Users/yl/Desktop/data_mining/Task3/weibo_data/temp/"
        # self.originPath = "/Users/hzt/lab/data_miming/weibo_data/pro3_data/"
        # self.outputPath = "/Users/hzt/lab/data_miming/weibo_data/temp/"
        self.trainDataFile = "weibo_train_data2.txt"
        self.testDataFile = "weibo_predict_data.txt"

    def washTrainData(self):
        ''' 进行训练集的清洗
        '''
        readFilePath = self.originPath + self.trainDataFile
        writeFilePath = self.outputPath + self.trainDataFile
        originTrainData = self.readFile(readFilePath)
        washedData = []
        for line in originTrainData:
            washedLine = self.replaceTable(line)
            washedData.append(washedLine)
        self.writeFile(writeFilePath, washedData)
        self.deleteWrongLines()
        print("------DONE------")

    def washTestData(self):
        ''' 进行测试集的清洗
        '''
        readFilePath = self.originPath + self.testDataFile
        writeFilePath = self.outputPath + self.testDataFile
        originTestData = self.readFile(readFilePath)
        washedData = []
        for line in originTestData:
            washedLine = self.replaceTable(line)
            washedData.append(washedLine)
        self.writeFile(writeFilePath, washedData)
        print("------DONE------")
        pass

    def deleteWrongLines(self):
        ''' 删除无效的行
        '''
        nameList = ['luid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'cont']
        data = pd.read_csv(
            self.outputPath + self.trainDataFile, sep=',', names=nameList)
        for index in data.index:
            # print("------Index:",index,data.loc[index]['fcs'])
            fcs = data.loc[index]['fcs']
            ccs = data.loc[index]['ccs']
            lcs = data.loc[index]['lcs']
            if pd.isnull(fcs) and pd.isnull(ccs) and pd.isnull(lcs):
                print("------NA:", index)
                data.drop(index, axis=0, inplace=True)
        data.to_csv(
            self.outputPath + "washedTrainData.txt", index=False, sep=",")

    def addSum(self):
        ''' 求出sum并写入文件中
        '''
        filePath = self.outputPath + "washedTrainData.txt"
        newCols = ['luid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'sum', 'cont']
        trainData = pd.read_csv(filePath, sep=',', header=0)
        trainData['sum'] = trainData.apply(
            lambda x: x['fcs'] + x['ccs'] + x['lcs'], axis=1)
        trainData['fcs'] = trainData['fcs'].astype('int')
        trainData['ccs'] = trainData['ccs'].astype('int')
        trainData['lcs'] = trainData['lcs'].astype('int')
        trainData['sum'] = trainData['sum'].astype('int')
        trainData = trainData.ix[:, newCols]
        trainData.to_csv(self.outputPath + "washedTrainData.txt", index=False, sep=",")

    def readFile(self, filePath):
        ''' 读文件操作，返回一个很大的string
        '''
        originTrainData = None
        originFile = None
        try:
            originFile = open(filePath, 'r', encoding='utf-8')
            originTrainData = originFile.readlines()
        except IOError as e:
            print("------ERROR LOG:", e)
            return None
        finally:
            if originFile != None:
                originFile.close()
        return originTrainData

    def writeFile(self, filePath, washedData):
        ''' 写文件操作
        '''
        try:
            # w+,进行读写操作，文件不存在就创建，先清空再写
            washedFile = open(filePath, 'w+', encoding='utf-8')
            washedFile.writelines(washedData)
        except IOError as e:
            print("------ERROR LOG:", e)

    def replaceTable(self, string):
        ''' 替换掉'\t',很多行都有这个问题，导致不能正确把各个特征值分开
        '''
        resultStr = string.replace('\t', ',')
        # print("------After replace:\n",resultStr)
        return resultStr