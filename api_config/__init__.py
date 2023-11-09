from flask import (Flask)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask('MyApp')
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/tienda_libros"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)