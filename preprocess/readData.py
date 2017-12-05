# coding:utf-8
'''
    Author:minning
    Date:2017/12/4
    代码目的：读取原始数据

'''
import pandas as pd
import numpy as np


hunan_path = '../data/hunan.xlsx'
hunan = pd.read_excel(hunan_path, sep='\t', encoding='utf-8')
print hunan.shape
print hunan.head


