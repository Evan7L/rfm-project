"""
练习 6：RFM 原始值

任务：
1. 读 clean.csv
2. 以数据里最大日期为“今天”
3. 按 CustomerID 计算：
   R = 今天 - 最近购买日期（天）
   F = 订单数（InvoiceNo 去重）
   M = Revenue 总和
4. 输出 data/processed/rfm.csv

提示：
- groupby.agg
- max() / nunique()
- (today - date).dt.days
"""

# TODO: 在这里写代码


if __name__ == "__main__":
    pass
