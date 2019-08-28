from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:密碼 @IP:Port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 創一個db物件
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    # Columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sender_id = db.Column(db.String(80))
    payload = db.Column(db.String(80), nullable=False)

    # id = Column(Integer, primary_key = True, autoincrement = True)
    # sender_id = Column(BIGINT(unsigned = True) , unique = True)
    # payload = Column(String(80), unique=True, nullable=False)

    

    def __init__(self, sender_id, payload):
        self.sender_id = sender_id
        self.payload = payload

    def __repr__(self):
        return '<User %r>' % self.payload