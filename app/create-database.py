import mysql.connector

my_db = mysql.connector.connect(
 host="localhost",
 user="root", 
 passwd="************"
 )


#faz os comandos pra gente
my_cursor = my_db.cursor()

#my_cursor.execute("create database products")
#my_cursor.execute("use products")
#my_cursor.execute("create table products( id int primary key auto_increment, name varchar(50) not null, price varchar(5) not null, type varchar(50))")
