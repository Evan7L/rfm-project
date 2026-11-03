"""
练习 2：清洗

规则：
1. 去掉 CustomerID 为空的行
2. 去掉 Quantity <= 0 的行（退货/损坏）
3. 去掉 UnitPrice <= 0 的行
4. 去掉完全重复的行
5. 加一列 Revenue = Quantity * UnitPrice
6. 存到 data/processed/clean.csv

输出：清洗前后行数对比
"""

import pandas as pd
from pathlib import Path

def clean_data():
    BASE = Path(__file__).resolve().parent.parent
    raw_path = BASE / "data" / "raw" / "online_retail.csv"
    df = pd.read_csv(raw_path)
    raw_count = len(df)

    # 过滤 Quantity > 0、UnitPrice > 0
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    # 去重
    df = df.drop_duplicates()
    # 新增Revenue
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    # 日期转时间类型
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # 保存全量 clean_all
    all_path = BASE / "data" / "processed" / "clean_all.csv"
    df.to_csv(all_path, index=False)
    all_count = len(df)

    # 剔除CustomerID空值，得到RFM用数据
    df_rfm = df.dropna(subset=['CustomerID'])
    rfm_path = BASE / "data" / "processed" / "clean_rfm.csv"
    df_rfm.to_csv(rfm_path, index=False)
    rfm_count = len(df_rfm)

    # 打印行数对比
    print(f"原始行数：{raw_count}")
    print(f"clean_all 行数：{all_count}")
    print(f"clean_rfm 行数：{rfm_count}")

if __name__ == "__main__":
    clean_data()
