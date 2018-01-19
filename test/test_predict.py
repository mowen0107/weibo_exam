# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 完成predict函数,增加test函数
'''
import sys
sys.path.append('..')
from predict import Predict


def main():
    predict = Predict()
    predict.predict()
    # predict.test()


if __name__ == '__main__':
    main()