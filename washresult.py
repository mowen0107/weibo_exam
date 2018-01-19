# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180119
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 创建文件
'''
import numpy as np
import pandas as pd
import pandas.errors as pderr
import errno


class WashResult():
    def __init__(self):
        self.resultDir = "/Users/hzt/lab/data_miming/weibo_exam/data/result/"
        self.inputFile = self.resultDir + "result.txt"
        self.outputFile = self.resultDir + "submit_temp.txt"
        self.submitFile = self.resultDir + "submit.txt"
        self.resultData = pd.read_csv(
            self.inputFile, header=0, sep='\t', encoding='utf-8')

    def dropCols(self):
        submitTempData = self.resultData.drop(['time', 'sum', 'cont'], axis=1)
        submitTempData.to_csv(
            self.outputFile,
            sep='\t',
            index=False,
            header=None,
            encoding='utf-8')

    def replaceRep(self):
        submitData = []
        submitTempData = self.readFile(self.outputFile)
        if submitTempData is not None:
            for line in submitTempData:
                dataList = line.split('\t')
                submitLine = dataList[0] + '\t' + dataList[1] + '\t'
                submitLine += dataList[2] + ',' + dataList[3] + ','
                submitLine += dataList[4]
                submitData.append(submitLine)
            self.writeFile(self.submitFile, submitData)
            print("------DONE------")
        else:
            print("------ERROR------")

    def readFile(self, filePath):
        ''' 读文件操作，返回一个很大的string
        '''
        submitTempFile = None
        submitTempData = None
        try:
            submitTempFile = open(self.outputFile, 'r', encoding='utf-8')
            submitTempData = submitTempFile.readlines()
        except IOError as e:
            print("------ERROR LOG:", e)
            return None
        finally:
            if submitTempFile is not None:
                submitTempFile.close()
        return submitTempData

    def writeFile(self, filePath, submitData):
        ''' 写文件操作
        '''
        try:
            # w+,进行读写操作，文件不存在就创建，先清空再写
            submitFile = open(filePath, 'w+', encoding='utf-8')
            submitFile.writelines(submitData)
        except IOError as e:
            print("------ERROR LOG:", e)
