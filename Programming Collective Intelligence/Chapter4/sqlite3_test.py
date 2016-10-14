import sqlite3


##conn=sqlite3.connect('test.db')
##cursor=conn.cursor()
##cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
##cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
##print cursor.rowcount
##cursor.close()
##conn.commit()
##conn.close()

##conn=sqlite3.connect('test.db')
##cursor=conn.cursor()
##cursor.execute('select * from user where id=?', '1')
##values=cursor.fetchall()
##print values
##cursor.close()
##conn.close()

##conn=sqlite3.connect('test1.db')
##cursor=conn.cursor()
##cursor.execute('create table urllist(url)')
##cursor.execute('create table wordlist(word)')
##cursor.execute('create table wordlocation(urlid,wordid,location)')
##cursor.execute('create index wordidx on wordlist(word)')
##cursor.execute('create index urlidx on urllist(url)')
##print cursor.rowcount
##conn.commit()
##cursor.close()
##conn.close()

conn=sqlite3.connect('test1.db')
cursor=conn.cursor()
cursor.execute('select * from urllist')
cursor.execute('insert into urllist (id, name) values (\'1\', \'Michael\')')
values=cursor.fetchall()
print values
cursor.close()
conn.close()
