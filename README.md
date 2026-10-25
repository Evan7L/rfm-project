# rfm-project

电商用户分析：RFM 分层 + Cohort 留存

## 数据

UCI Online Retail（54 万行，英国零售商）：
https://archive.ics.uci.edu/dataset/352/online+retail

下载后放到 `data/raw/`，文件名改成 `online_retail.xlsx` 或 `online_retail.csv`。

## 目录

```
data/raw/          原始数据（不进 Git）
data/processed/    清洗后的数据
notebooks/         探索性分析
practice/          10 个练手题（按阶段做）
src/               正式脚本
reports/           图表输出
app.py             Streamlit 看板（第 13 周完成）
```

## 快速开始

```bash
pip install -r requirements.txt

# 第 8 周：先做 01，确认能读数据
python practice/01_load_data.py
```

## 10 个练手题

| 序号 | 文件 | 对应阶段 |
|---|---|---|
| 1 | 01_load_data.py | 第 8 周：读数据、体检 |
| 2 | 02_clean.py | 第 9 周：清洗 |
| 3 | 03_revenue.py | 第 10 周：月度 GMV |
| 4 | 04_groupby.py | 第 10 周：分组统计 |
| 5 | 05_sqlite.py | 第 9–10 周：入库 + SQL |
| 6 | 06_rfm.py | 第 11 周：RFM 原始值 |
| 7 | 07_rfm_score.py | 第 11 周：打分分层 |
| 8 | 08_cohort.py | 第 12 周：留存矩阵 |
| 9 | 09_plotly.py | 第 12 周：三张图 |
| 10 | 10_streamlit.py | 第 13 周：最小看板 |

## 说明

每个文件顶部有任务和提示，把 `# TODO` 换成代码，跑通就算完成。
数据列：InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country。
