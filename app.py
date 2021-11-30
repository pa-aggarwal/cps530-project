from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/demo")
def demo():
    return render_template("demo.html", title="Demo")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html", title="Tutorial")
