import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@localhost/project'
db = SQLAlchemy(app)
# 定義 User 模型


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)         # 主鍵 ID
    username = db.Column(db.String(255), nullable=False)  # 使用者名稱
    password = db.Column(db.String(255), nullable=False)  # 密碼（加密）


@app.route('/')
def index():
    db.create_all()
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
