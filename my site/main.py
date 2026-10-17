from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
app.run(debug=True)

@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!</h1>"