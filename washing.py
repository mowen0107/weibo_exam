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
        self.inputDir = "D:/weibo/weibo_exam/data/origin/"
        self.outputDir = "D:/weibo/weibo_exam/data/washing/"
        # self.inputDir = "/Users/hzt/lab/data_miming/weibo_data/pro3_data/"
        # self.outputDir = "/Users/hzt/lab/data_miming/weibo_data/temp/"

    def washTrainData(self):
        ''' 进行训练集的清洗
            删除mid,time,cont列(后面两个暂时用不上)
        '''
        readFilePath = self.inputDir + "weibo_train_data.txt"
        writeFilePath = self.outputDir + "washed_train_data.txt"
        nameList = ['uid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'cont']
        originTrainData = pd.read_csv(
            readFilePath, names=nameList, sep='\t', encoding='utf8')
        washedTrainData = originTrainData.drop(['mid', 'time', 'cont'], axis=1)
        washedTrainData.to_csv(
            writeFilePath, index=False, sep='\t', encoding='utf-8')

    def washTestData(self):
        ''' 进行测试集的清洗
        '''
        # readFilePath = self.inputDir + self.testDataFile
        # writeFilePath = self.outputDir + self.testDataFile
        # originTestData = self.readFile(readFilePath)
        # washedData = []
        # for line in originTestData:
        #     washedLine = self.replaceTable(line)
        #     washedData.append(washedLine)
        # self.writeFile(writeFilePath, washedData)

        pass

    def deleteWrongLines(self):
        ''' 删除无效的行
        '''
        pass
        # nameList = ['luid', 'mid', 'time', 'fcs', 'ccs', 'lcs', 'cont']
        # data = pd.read_csv(
        #     self.outputDir + self.trainDataFile, sep=',', names=nameList)
        # for index in data.index:
        #     # print("------Index:",index,data.loc[index]['fcs'])
        #     fcs = data.loc[index]['fcs']
        #     ccs = data.loc[index]['ccs']
        #     lcs = data.loc[index]['lcs']
        #     if pd.isnull(fcs) and pd.isnull(ccs) and pd.isnull(lcs):
        #         print("------NA:", index)
        #         data.drop(index, axis=0, inplace=True)
        # data.to_csv(
        #     self.outputDir + "washedTrainData.txt", index=False, sep=",")

    def addSum(self):
        ''' 求出sum并写入文件中
        '''
        filePath = self.outputDir + "washed_train_data.txt"
        newCols = ['uid', 'fcs', 'ccs', 'lcs', 'sum']
        trainData = pd.read_csv(filePath, sep='\t', header=0, encoding='utf-8')
        trainData['sum'] = trainData.apply(
            lambda x: x['fcs'] + x['ccs'] + x['lcs'], axis=1)
        trainData['fcs'] = trainData['fcs'].astype('int')
        trainData['ccs'] = trainData['ccs'].astype('int')
        trainData['lcs'] = trainData['lcs'].astype('int')
        trainData['sum'] = trainData['sum'].astype('int')
        trainData = trainData.ix[:, newCols]
        trainData.to_csv(
            self.outputDir + "washed_train_data.txt", index=False, sep="\t")

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