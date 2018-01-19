# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180114
    Last modified by: HZT
    Last modified date: 20180114
    Last modified thing: 
'''
import matplotlib.pyplot as plt


class PlotGraph:
    ''' 用来画图的类
    '''

    def __init__(self):
        pass

    def plot(self):
        xdata = [1, 2, 3]
        ydata = [4, 5, 6]
        plt.plot(xdata, ydata)
        plt.xlabel('Plot Number')
        plt.ylabel('Important var')
        plt.title("plot test")
        plt.show()
