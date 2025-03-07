from flask import Flask
from flask_mysqldb import MySQL
from config import SECRET_KEY, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_HOST

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DATABASE
app.config['MYSQL_HOST'] = MYSQL_HOST

mysql = MySQL(app)

# Import routes at the end to avoid circular import
from app import routes