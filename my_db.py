import sqlite3

connection = sqlite3.connect("users_db.db")

cursor = connection.cursor()
# --------------------------------------------------- database queries ----------------------------------------------

user = (1,'yazan', "123")
insert_query = "insert into users values (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (1,'piano', "123"),
    (3,'gun', "123")
]
insert_many_query = "insert into users values(?,?,?)"
cursor.executemany(insert_many_query,users)

select_query = 'select * from users'
users_list = list(cursor.execute(select_query))

connection.commit()
connection.close()