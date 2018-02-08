from flask import Blueprint, render_template, redirect,request
from app import db
from .models import User
user = Blueprint('user',__name__)

@user.route('/index')
def index():
    return render_template('user/index.html')

@user.route('/add/',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        p_user = request.form.get('username',None)
        p_email = request.form.get('email',None)
        p_password = request.form.get('password',None)

        if not p_user or not p_email or not p_password:
            return 'input error'

        # 增加
        newobj = User(username=p_user, email=p_email, password=p_password)
        db.session.add(newobj)
        db.session.commit()

        users = User.query.all()
        return render_template('user/add.html',users=users)
    users = User.query.all()

    # 更改
    user = db.session.query(User).filter_by(username="ewew").first()
    user.password = "99999999"
    db.session.commit()

    # 查询
    users = db.session.query(User).filter(User.username == 'ewew')

    # 删除
    user = db.session.query(User).filter_by(username="ewew").first()
    db.session.delete(user)
    db.session.commit()

    return render_template('hello.html',users=users)

@user.route('/show')
def show():
    return 'user_show'