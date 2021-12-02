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

@app.route("/install")
def install():
    return render_template("install.html", title="Install")

@app.route("/summary")
def summary():
    return render_template("summary.html", title="Summary")

@app.route("/conclusion")
def conclusion():
    return render_template("conclusion.html", title="Conclusion")

@app.route("/credits")
def credits():
    return render_template("credits.html", title="Credits")
