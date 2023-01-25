from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm
from models import QuestionModel
from exts import db


bp = Blueprint("qa", __name__, url_prefix="/")


# https://127.0.0.1:80
@bp.route('/')
def index():
    return render_template("index.html")


@bp.route('/qa/public', methods=['GET', 'POST'])
def public_question():
    if request.method == 'GET':
        return render_template("qa.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # TODO： 跳转到问答详情页
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))
