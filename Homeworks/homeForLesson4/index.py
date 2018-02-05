from flask import Flask, render_template, request
from models import db, Person

app = Flask(__name__)


@app.before_request
def before_request():
    try:
        db.connect()
    except:
        return


@app.route("/")
def home():
    return render_template('index.html', persons=persons)


@app.route("/persons/")
def persons():
    persons = Person.select()
    return render_template('person.html', persons=persons)


@app.route('/post/', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form.get('name', 'Гость')
        year = request.form.get('year', 2000)
        male = request.form.get('male', False)
        print(male)
        Person.create(name=name, year=year, male=male)
    return render_template('post.html')


@app.after_request
def after_request(response):
    db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)

