from flask import Flask, render_template, request


##Here name is special variable which referrig to current file name
app = Flask(__name__)  

@app.route("/")
def index():
    name = request.args.get("name", "world")
    #name = request.args["name"]
    
    return render_template("index.html", name=name)

