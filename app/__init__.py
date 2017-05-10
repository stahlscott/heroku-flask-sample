from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')  # heroku provided postgres server
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models.post import Post


@app.route('/')
def index():
    text = 'Hello World!'
    return render_template('index.html', text=text)


@app.route('/posts')
def posts():
    posts = Post.query.order_by(desc(Post.id)).all()
    return render_template('posts.html', posts=posts)
