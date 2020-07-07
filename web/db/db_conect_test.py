## 导入psycopg2包
import psycopg2
## 连接到一个给定的数据库
conn = psycopg2.connect(database="zktest", user="GOTRACK20200324",
                        password="GOTRACK0324", host="gotrack.czckjds55umy.rds.cn-northwest-1.amazonaws.com.cn", port="5432")
## 建立游标，用来执行数据库操作
cursor = conn.cursor()

## 执行SQL命令
# cursor.execute("DROP TABLE test_conn")
cursor.execute("CREATE TABLE test_conn(id int, name text)")
cursor.execute("INSERT INTO test_conn values(1,'haha')")

## 提交SQL命令
conn.commit()

## 执行SQL SELECT命令
cursor.execute("select * from test_conn")

## 获取SELECT返回的元组
rows = cursor.fetchall()
for row in rows:
    print('id = ',row[0], 'name = ', row[1], '\n')

## 关闭游标
cursor.close()

## 关闭数据库连接
conn.close()