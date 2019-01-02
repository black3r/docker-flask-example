from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", 'sqlite:///test.db')
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<{self.id}> {self.text}"


@app.route('/')
def hello_world():
    return 'Hello, World!'


def get_notes():
    return jsonify({
        "notes": [note.text for note in Note.query.all()],
    })


def post_notes():
    new_note = Note(text=request.get_json()['note'])
    db.session.add(new_note)
    db.session.commit()
    return get_notes()


@app.route('/notes/', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        return post_notes()
    else:
        return get_notes()
