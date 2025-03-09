from flask import Flask
from flask_mysqldb import MySQL
from config import SECRET_KEY, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_HOST
import MySQLdb.cursors

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DATABASE
app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

from app import routes