from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User
from sqlalchemy.exc import IntegrityError  # 用于捕捉数据库唯一性约束错误

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        action = request.form.get('action')

        if action == 'register':
            new_user = User(username=username, password=password)
            try:
                db.session.add(new_user)
                db.session.commit()
                return render_template('user.html', username=username, message="Registration successful!")
            except IntegrityError:
                db.session.rollback()  # 回滚会话以处理错误
                return render_template('user.html', username=None, error="该用户名已被注册，请尝试其他用户名。")

        elif action == 'login':
            user = User.query.filter_by(username=username).first()
            if user and user.password == password:
                return render_template('user.html', username=username, message="Login successful!")
            else:
                return render_template('user.html', username=None, error="用户或者密码错误，请重新输入。")

    return render_template('user.html', username=None, error=None)
