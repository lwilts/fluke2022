import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/details/")
def details():
    return render_template("details.html")
    
@app.route("/registry/")
def registry():
    return render_template("registry.html")

@app.route("/gallery/")
def gallery():
    return render_template("gallery.html")

@app.route("/rsvp/")
def rsvp():
    return render_template("rsvp.html")

@app.route("/travel/")
def travel():
    return render_template("travel.html")

@app.route("/eatingdrinking/")
def eatingdrinking():
    return render_template("eatingdrinking.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
