from flask import Flask, render_template
app = Flask(__name__)


'''
Vista para la URL raiz
'''
posts = []
@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))


'''
Vista con un parámetro tipo string
para generar URL dinámicas
'''
@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


'''
Vista ejecutada por 2 URL diferentes
'''
@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)