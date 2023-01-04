import jwt, datetime, os
from flask import Flask, request
#from flask_mysqldb import MySQL

import mysql.connector
server = Flask(__name__)
#mysql = MySQL(server)

server.config["MYSQL_HOST"] = "127.0.0.1"
server.config["MYSQL_USER"] = "auth_user"
server.config["MYSQL_DB"] =  "auth"
server.config["MYSQL_PORT"] = "3306"
server.config["MYSQL_PASSWORD"]= "Auth123"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="auth_user",
  password="Auth123",
  database = "auth",
  port="3306"
)
print(mydb)
cur =  mydb.cursor()
print(cur)
user_name = "georgio@email.com"

tex = "SELECT email, password FROM user WHERE email = %(usr_name)s "
cur.execute(tex,{"usr_name" : user_name})
res = cur.fetchone()
print(res)

