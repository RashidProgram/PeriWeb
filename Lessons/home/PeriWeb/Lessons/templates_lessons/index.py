from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    context = {
        'authon': "Тененбаум",
        'books': [
            {
                "title": "Архитектура компьютера",
                "pages": 1020
            },
            {
                "title": "Компьютерные сети",
                "pages": 1120
            }
        ]
    }
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True)