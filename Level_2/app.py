from flask import Flask, request, jsonify, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import csv


app = Flask(__name__)
app.secret_key = "Hello"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    image_file = db.Column(db.String(255), default=None)
  

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/addnew", methods=['POST'])
def addnew():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    age = request.form['age']
    file_path = request.form['file-path']

    post = users(first_name=first_name, last_name=last_name, age=int(age), image_file = file_path)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/data")
def data():

    min_age = request.args.get('min_age', type=int, default=0)
    max_age = request.args.get('max_age', type=int, default=1000)

    is_image_exists = request.args.get('is_image_exists', type=str)
    
    if is_image_exists == "False":
        rows = users.query.filter_by(image_file="")

    elif is_image_exists == "True":
        rows = users.query.filter(users.image_file!="").all()

    else:
        rows = users.query.filter(min_age <= users.age).filter(users.age <= max_age).all()

    arr = []

    for row in rows:
        datas = {}

        datas["id"] = row.user_id
        datas["first_name"] = row.first_name
        datas["last_name"] = row.last_name
        datas["age"] = row.age
        datas["image_file"] = row.image_file

        arr.append(datas)

    result = jsonify(arr)
    return result


if __name__ == '__main__':
    app.run(debug=True)
