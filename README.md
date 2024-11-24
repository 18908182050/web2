# User Registration and Login System

这是一个简单的用户注册和登录系统，使用 Flask 框架构建。该项目允许用户注册新账户，并通过用户名和密码进行登录。

## 项目结构
├── .idea
├── blueprints
├── instance
├── static
├── templates
├── app.py
├── config.py
├── models.py
├── requirements.txt
└── README.md

- `app.py`: 应用的主入口文件。
- `config.py`: 配置sqllite数据库文件
- `models.py`: 数据模型，定义数据库中的 User 模型。
- `requirements.txt`: 项目所需的 Python 库。
- `templates/`: 存放 HTML 模板的目录。
- `static/`: 存放静态文件的目录，如 CSS 和 JavaScript。
- `blueprints/`: 存放 Flask 蓝图的目录，用于组织视图和路由。

## 安装和运行

1. 克隆此仓库：

   ```bash
   git clone https://github.com/your_username/project_name.git
   cd project_name
