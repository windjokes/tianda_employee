# *.* coding = utf-8 *.*

#https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection

# import sqlite3
# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
#
# #Create table
# c.execute('''CREATE TABLE stocks
#              (date  text,
#               trans text,
#               symol text,
#               qty   real,
#               price real)''')
#
# #Insert a row of data
# c.execute("INSERT INTO stocks VALUES ("
#           "'2016-01-05', 'BUY', 'RHAT', 100, 35.14)")
#
# #Save (commit) the changes
# conn.commit()
#
# #We can also close the connection if we are done with it.
# #Just be sure any changes have been committed or they will be lost.
# conn.close()

# Never do this -- insecure!
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
#Do this instead
#接收一个tuple,用‘？’来代替%s
# t=('RHAT',)
# c.execute("SELECT * FROM stocks WHERE symbol=?", t)
# print(c.fetchone())
    #sqlite3.OperationalError: no such column: symbol

#Larger example that inserts many records at a time
# purchases = [('2016-03-28','BUY','IBM', 1000, 45.00),
#              ('2006-04-05','BUY','MSFI', 1000, 72.00),
#              ('2006-04-06','BUY','IBM', 500, 53.00),
#              ]
# c.executemany("INSERT INTO stocks VALUES (?,?,?,?,?)", purchases)
# conn.commit()
#
# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#     print(row)


#A minimal SQLite shell for experiments
import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ''

print ("Enter your SQL commands to execute in sqlite3.")
print ("Enter a blank line to exit.")

while True:
    line = input()
    if line == '':
        break
    buffer +=line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchone())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()




