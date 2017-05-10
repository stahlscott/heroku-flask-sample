from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Post %r>' % (self.title)
