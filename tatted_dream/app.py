from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('./index.html')


@app.route("/bookAppointment", methods=["POST"])
def book_appointment():
    pass
