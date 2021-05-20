from flask import Flask
from flask import request
from flask import render_template

from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    # n = min(int(request.args.get("count", 100)), 100)
    # text = ""
    # for i in range(n):
    #     text += "<p>Hello, World!</p>"
    username = request.args.get("username", "User")
    users = ['Rosalia', 'Adrianna', 'Victoria']
    return render_template("index.html", title="hello world!", username=username, users=users)


@app.route("/users/")
def users():
    a = 10
    b = 20
    return f"Empty {a}<br>example {b}"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


if __name__ == '__main__':
    app.run(debug=True)
