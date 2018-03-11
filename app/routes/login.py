from flask import Blueprint, render_template, redirect,request, jsonify
from app.auth.auths import Auth
from .. import common

login = Blueprint('login',__name__)

@login.route('/token', methods=['POST'])
def token():
    """
    用户登录
    :return: json
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if (not username or not password):
        return jsonify(common.falseReturn('', '用户名和密码不能为空'))
    else:
        return Auth.authenticate(Auth, username, password)











