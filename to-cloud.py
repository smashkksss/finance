import mysql.connector
import json

# 从json文件中读取公司数据
with open('company_data.json', 'r') as f:
    company_data = json.load(f)

# 连接到Google Cloud的MySQL数据库
cnx = mysql.connector.connect(
    user='your_username', 
    password='your_password',
    host='your_instance_ip', 
    database='your_database'
)

cursor = cnx.cursor()

# 创建数据表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS company_data (
        company VARCHAR(10),
        date DATE,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT
    )
""")

# 插入公司数据
for company, data in company_data.items():
    for date, values in data['Open'].items():
        cursor.execute("""
            INSERT INTO company_data (company, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (company, date, values, data['High'][date], data['Low'][date], data['Close'][date], data['Volume'][date]))

# 提交事务
cnx.commit()

# 关闭连接
cursor.close()
cnx.close()
