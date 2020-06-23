import psycopg2

conn = psycopg2.connect(database="zktest", user="GOTRACK20200324", password="GOTRACK0324",
                        host="gotrack.czckjds55umy.rds.cn-northwest-1.amazonaws.com.cn", port="5432")

print("Opened database successfully")
