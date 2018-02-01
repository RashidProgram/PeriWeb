from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/hello/<user>')
def hello_user(user):
    return "hello {0}".format(user)

if __name__ == "__main__":
    app.run()