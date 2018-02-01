#-*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)

authors = [
    {
        'name': 'Тененбаум',
        'books_count': 3
    },
    {
        'name': 'Флэнеген',
        'books_count': 2
    },
    {
        'name': 'Самерфилд',
        'books_count': 5
    },
]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/books/')
def books():
    context = {
        'author': 'Тененбаум',
        'books': [
            {
                'title': 'Архитектура компьютера',
                'pages': 820
            },
            {
                'title': 'Компьютерные сети',
                'pages': 1020
            },
            #Задание 1
            {
                'name': 'КНИГАНИОЧЕМ',
                'books_count': -22
            }
        ]
    }
    return render_template('books.html', **context)


@app.route('/contact/')
@app.route('/contact/<phone>')
def contact(phone=None):
    if phone is None:
        phone = '656565'
    return 'Мой телефон ' + phone


# Задание 3
@app.route("/my/")
def my():
    return render_template("my.html")

#Задание 4 и 5
@app.route('/authors/')
def fAuthors():
    global authors
    return render_template("authors.html", author=authors)


if __name__ == '__main__':
    app.run(debug=True)
