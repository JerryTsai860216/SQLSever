from re import S
import pyodbc
import pandas as pd 

#login DB

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER="Server name";DATABASE="DB name";UID ="account";PWD="password"')
cnxn =cnxn.cursor()

#執行SQL Query

cursor.execute("sql query")

rows =cursor.fetchall()

#確認查詢總筆數
a = len(rows)
print(f'總筆數：{a}')

#遍歷查詢結果
for row in rows:
    print(row.欄位名稱,row.欄位名稱)

cnxn.close()
