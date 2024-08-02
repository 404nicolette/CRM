import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="myuser",
    passwd="mypassword",
    db="myproject"
)

cursor = db.cursor()
cursor.execute("SHOW TABLES")
print("working")
db.close()
