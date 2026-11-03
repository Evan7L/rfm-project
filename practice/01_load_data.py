"""
练习 1：读数据，做体检

任务：
1. 找到 data/raw 下的 CSV 或 Excel
2. 读进来，打印 shape、列名、dtypes
3. 打印每列缺失值数量
4. 打印前 5 行
"""

import pandas as pd
from pathlib import Path
def load_data():
    BASE = Path(__file__).resolve().parent.parent
    df = pd.read_csv(BASE / "data" / "raw" / "online_retail.csv")
    print(df.shape)
    print(df.columns)
    print(df.dtypes)
    print(df.isna().sum())
    print(df.describe())
    print(df.head())

if __name__ == "__main__":
    load_data()