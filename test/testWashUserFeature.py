# -*- coding: utf-8 -*-
''' Author: HZT
    Create date: 20180115
    Last modified by: HZT
    Last modified date: 20180115
    Last modified thing: 
'''
import sys
sys.path.append('..')
from washuserfeature import WashUserFeature

def main():
    washUserFeature = WashUserFeature()
    washUserFeature.run()
    print("------DONE------")

if __name__ == '__main__':
    main()