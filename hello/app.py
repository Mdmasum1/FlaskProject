from flask import Flask, render_template, request


##Here name is special variable which referrig to current file name
app = Flask(__name__)  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name = name)






