from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pievienot")
def pievienot():
    return render_template("pievienot.html")

@app.route("/atzimes")
def atzimes():
    return render_template("atzimes.html")



if __name__ == '__main__':
    app.run(port = 5000)