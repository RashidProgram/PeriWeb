from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    POST = False
    if request.method == "POST":
        POST = True
    return render_template('index.html',post=POST)

if __name__ == "__main__":
    app.run(debug=True)