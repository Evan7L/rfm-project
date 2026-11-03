# 数据字典

## 文件

- `clean_all.csv`：524878 行，保留匿名订单，算 GMV 用
- `clean_rfm.csv`：392692 行，只保留有 CustomerID 的，做 RFM 用

## 字段

| 字段 | 类型 | 含义 | 处理 |
|---|---|---|---|
| InvoiceNo | 文本 | 发票号，C 开头是退货 | 已剔除 C 开头 |
| StockCode | 文本 | 商品编码 | 无 |
| Description | 文本 | 商品名 | 缺 1454 行，保留 |
| Quantity | 整数 | 数量 | 已剔除 <= 0 |
| InvoiceDate | 日期 | 开票时间 | 已转 datetime |
| UnitPrice | 小数 | 单价 | 已剔除 <= 0 |
| CustomerID | 文本 | 客户 ID，空=匿名 | 全量保留，RFM 版剔除 |
| Country | 文本 | 国家 | UK 占 91.43% |
| Revenue | 小数 | 新增，Quantity × UnitPrice | — |

## 清洗规则

1. 去掉 Quantity <= 0 和 UnitPrice <= 0
2. 去掉完全重复的行
3. InvoiceDate 转 datetime
4. RFM 版额外去掉 CustomerID 空值