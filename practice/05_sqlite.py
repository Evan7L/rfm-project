"""
练习 5：CSV -> SQLite

任务：
1. 读 data/processed/clean.csv
2. 写入 SQLite：data/processed/shop.db，表名 orders
3. 用 SQL 完成三个查询：
   a. 消费金额 Top 10 客户
   b. 每月 GMV
   c. 每个国家的订单数

提示：
- sqlite3.connect
- df.to_sql
- pd.read_sql_query
"""

import pandas as pd
from pathlib import Path
import sqlite3

def load():
    BASE = Path(__file__).resolve().parent.parent
    # 把 InvoiceNo 读成字符串
    df = pd.read_csv(
        BASE / "data/processed/clean_all.csv",
        dtype={"InvoiceNo": str}
    )
    return df

def to_sqlite(df):
    BASE = Path(__file__).resolve().parent.parent
    conn = sqlite3.connect(BASE / "data" / "processed" / "shop.db")

    #写SQL
    #消费前十
    df.to_sql("orders", conn, if_exists="replace", index=False)
    n = pd.read_sql_query("SELECT COUNT(*) AS n FROM orders", conn)
    print(n)
    q1 = pd.read_sql_query("""
                           SELECT CustomerID, SUM(Revenue) AS total
                           FROM orders
                               WHERE CustomerID IS NOT NULL   --去匿名
                               GROUP BY CustomerID
                               ORDER BY total DESC
                               LIMIT 10
                           """, conn)
    print(q1)

    #GMV 上个月销售额
    q2 = pd.read_sql_query("""
                           SELECT strftime('%Y-%m', InvoiceDate) AS month, SUM(Revenue) AS gmv
                           FROM orders
                           GROUP BY month
                           ORDER BY month
                           """, conn)
    print(q2)

    #每个国家的订单数
    q3 = pd.read_sql_query("""
                           SELECT Country, COUNT(DISTINCT InvoiceNo) AS orders
                           FROM orders
                           GROUP BY Country
                           ORDER BY orders DESC
                           """, conn)
    print(q3)


    conn.close()


if __name__ == "__main__":
    df = load()
    print(df.shape)
    to_sqlite(df)