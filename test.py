import mysql.connector

conn=mysql.connector.connect(host='localhost',password='pass',user='root')

if conn.is_connected():
    print("Set aai")