import random

from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from exts import mail, db
from flask_mail import Message
from flask import request
from models import EmailCaptchaModel, UserModel
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import RegisterForm, LoginForm

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


# /auth/login
@bp.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在!")
                return redirect(url_for("auth.login_user"))
            elif check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误!")
                return redirect(url_for("auth.login_user"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login_user"))


@bp.route('/loginout')
def logout_user():
    session.clear()
    return redirect('/')


@bp.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login_user"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register_user"))


@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    print(email)
    captcha = str(random.randint(1000, 9999))
    message = Message(subject="3D打印机远程管理平台·注册验证码",
                      recipients=[email],
                      body=f"您的验证码是: {captcha}")
    mail.send(message)
    # 验证码存储
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code": 200, "message": "", "data": None})


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试",
                      recipients=["danny123456123@126.com"],
                      body="测试邮件")
    mail.send(message)
    return "邮件发送成功"
