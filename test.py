from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:密碼 @IP:Port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 創一個db物件
db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = "test"
    # Columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Test %r>' % self.name

db.create_all()