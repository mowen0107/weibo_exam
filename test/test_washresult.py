# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180119
    Last modified by: HZT
    Last modified date: 20180119
    Last modified thing: 创建文件
'''
import sys
sys.path.append('..')
from washresult import WashResult


def main():
    washResult = WashResult()
    washResult.dropCols()
    washResult.replaceRep()


if __name__ == '__main__':
    main()