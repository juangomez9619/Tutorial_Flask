from forms import SignupForm, PostForm
from flask import Flask, render_template, request, redirect, url_for
from flask.signals import signals_available

from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'


login_manager = LoginManager()

'''
Vista para la URL raiz
'''
posts = []
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


'''
Vista con un parámetro tipo string
para generar URL dinámicas
'''
@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


'''
Vista para mostrar el formulario 
de inicio de sesión
'''
@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)


'''
Vista para crear nuevos post, procesando su formulario
'''
@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)
        return redirect(url_for('index'))
    return render_template("admin/post_form.html", form=form)