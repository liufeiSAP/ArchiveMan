from flask import Blueprint, render_template, redirect,request
from app import db, app
from app.auth.auths import Auth
from app.dao.userDao import UserDao
from app.models.models import User
user = Blueprint('user',__name__)

@app.before_request
def before_request():
    Auth.identify(Auth,request )

@user.route('/index')
def index():
    return render_template('user/index.html')

@user.route('/add/',methods=['POST'])
def add():
    p_user = request.form.get('username',None)
    p_email = request.form.get('email',None)
    p_password = request.form.get('password',None)
    p_type = request.form.get('type', None)

    if not p_user or not p_email or not p_password or not p_type:
        return 'input error'
    # 增加
    newobj = User(username=p_user, email=p_email, password=p_password, type = p_type)
    userDao = UserDao()
    userDao.add(newobj)

@user.route('/delete/<username>', methods=['GET'])
def delete(username):
    userDao = UserDao()
    userDao.delete(username)

@user.route('/update/',methods=['POST'])
def update():
    p_user = request.form.get('username', None)
    p_email = request.form.get('email', None)
    p_password = request.form.get('password', None)
    p_type = request.form.get('type', None)
    if not p_user or not p_email or not p_password or not p_type:
        return 'input error'

    newobj = User(username=p_user, email=p_email, password=p_password, type=p_type)
    userDao = UserDao()
    userDao.update(p_user, p_password, p_email, p_type)

@user.route('/search/<username>', methods=['GET'])
def search(username):
    userDao = UserDao()
    user = userDao.search(username)
    return user.username
