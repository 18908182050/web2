import os

class Config:
    # 连接 SQLite 数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example.db'  # 数据库文件路径
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用修改跟踪
