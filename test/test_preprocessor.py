# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180114
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 
'''
import sys
sys.path.append('..')
from preprocessor import Preprocessor

def main():
    preprocessor = Preprocessor()
    preprocessor.getUserFeature()
    print("------DONE------")

if __name__ == '__main__':
    main()