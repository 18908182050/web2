from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User  # 确保导入db和User模型

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')  # 获取密码
        action = request.form.get('action')  # 获取表单的操作类型

        if action == 'register':
            # 注册用户
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('user.html', username=username, message="Registration successful!")

        elif action == 'login':
            # 验证用户
            user = User.query.filter_by(username=username).first()
            if user and user.password == password:  # 直接比较密码
                return render_template('user.html', username=username, message="Login successful!")
            else:
                return render_template('user.html', username=None, error="用户或者密码错误，请重新输入")

    return render_template('user.html', username=None, error=None)
