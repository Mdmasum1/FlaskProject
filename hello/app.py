from flask import Flask, render_template, request


##Here name is special variable which referrig to current file name
app = Flask(__name__)  

@app.route("/")
def index():
    return "hello, world"