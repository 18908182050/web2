from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 主键id
    username = db.Column(db.String(50), unique=True, nullable=False)  # 唯一用户名
    password = db.Column(db.String(255), nullable=False)  # 密码字段

    def __repr__(self):
        return f'<User {self.username}>'  # 便于调试，输出用户的字符串表示
