import pandas as pd
import numpy as np


# 定义 Z-score 标准化函数
def z_score_standardize(data):
    mean = data.mean(axis=0)  # 计算每一列的均值
    std = data.std(axis=0)    # 计算每一列的标准差
    standardized_data = (data - mean) / std  # 标准化
    return standardized_data
"""
# 对输入数据进行 Z-score 标准化
standardized_X_data = z_score_standardize(X_data)

"""
