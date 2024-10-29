import sqlite3
from flask import Flask, render_template, request
from dati import pievienot_skolenu


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        vards = request.form['name']
        uzvards = request.form['lastname']
        pievienot_skolenu(vards, uzvards)
        dati = vards+" "+uzvards

        return render_template("index.html", aizsutitais = dati)
    
    # Get metode
    return render_template("index.html")

@app.route("/pievienot")
def pievienot():
    return render_template("pievienot.html")

@app.route("/atzimes")
def atzimes():
    return render_template("atzimes.html")



if __name__ == '__main__':
    app.run(port = 5000)